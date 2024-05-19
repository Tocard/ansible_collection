from __future__ import absolute_import, division, print_function
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

import hvac
from hvac.exceptions import VaultError, InvalidPath, InvalidRequest

import random
import string
import os

__metaclass__ = type

DOCUMENTATION = """
  name: auto_pass
  author: douceur
  version_added: '2.9'  # for collections, use the collection version, not the Ansible version
  short_description: read secret from hashicorp, or create if not exist
  description:
      - This lookup returns the contents of hashicorp vault or create it if it does not exist and return it
  options:
    _terms:
      description: path(s) of secret in vault
      type: string
      required: True
    key:
      description:
            - key under path to harvest, if omitted, will return the wholes keys
      type: string
    mount_point:
      description:
            - if you wanna specify a custom mount point, default is from kyss_mount_point variable
      type: string
    force_renew:
      description:
            - if key specified, and this one set to true, will force renew password
      type: bool
  notes:
    - this lookup uses env variable REQUESTS_CA_BUNDLE
"""

display = Display()


class HVAC:
    def __init__(self):
        self.cacerts = os.getenv("REQUESTS_CA_BUNDLE")
        self.client = self.init_hvac_client()

    def init_hvac_client(self):
        try:
            self.client = hvac.Client(url=os.getenv("hashi_vault_url"), token=os.getenv('VAULT_TOKEN'),
                                      verify=self.cacerts)
        except VaultError as e:
            raise AnsibleError("Unable to init hvac client for address {}", os.getenv("hashi_vault_url"), e)

    def read_path(self, mount_point: str, path: str) -> dict:
        try:
            data = self.client.secrets.kv.v2.read_secret_version(
                path=path, mount_point=mount_point)
            secret = data["data"]["data"]
            return secret
        except InvalidPath:
            display.warning("path {} does not exist yet".format(path))
            return {}
        except VaultError as e:
            display.warning("{}".format(e))
            raise AnsibleError("Unable to read vault path {} at mount point {}".format(path, mount_point), e)

    def create_or_update_secret(self, mount_point: str, path: str, secret: dict):
        try:
            self.client.secrets.kv.v2.create_or_update_secret(
                path=path, secret=secret, mount_point=mount_point)
            display.vvv("secrets have been created or updated in path {}".format(path))
            return True
        except InvalidRequest as e:
            display.warning(f"secrets not updated in path {path} because of invalid request {e}")
            return False
        except AnsibleParserError as e:
            raise AnsibleError("{}, {}, {}, {}".format(mount_point, path, secret, e))


class LookupModule(LookupBase):
    mount_point = None
    path = None
    field = None
    key = None
    length_password = 32
    force_renew = False
    hvac_wrapper = None

    def password_generator(self) -> str:
        letters = string.ascii_letters + string.digits + "-_"
        return "".join(random.choice(letters) for _ in range(self.length_password))

    def config(self, terms: list, variables: dict = None, **kwargs: dict):
        self.set_options(var_options=variables, direct=kwargs)
        self.path = "{}".format(terms[0])
        if ":" in self.path:
            parts = self.path.split(":", 1)
            self.path = parts[0]
            self.field = parts[1]
        if self.get_option("key") is not None:
            self.key = self.get_option("key")
        if self.get_option("mount_point") is not None:
            self.mount_point = self.get_option("mount_point")
        else:
            self.mount_point = variables["hashi_mount_point_api"]
        if self.get_option("force_renew") is not None:
            self.force_renew = self.get_option("force_renew")

        self.hvac_wrapper = HVAC()

    def run(self, terms: list, variables: dict = None, **kwargs: dict) -> list:
        self.config(terms, variables, **kwargs)
        while True:
            secrets = self.hvac_wrapper.read_path(self.mount_point, self.path)
            if self.key is not None and (self.key not in secrets or self.force_renew is True):
                display.vvv("key is missing or force_renew")
                secrets[self.key] = self.password_generator()
                if not self.hvac_wrapper.create_or_update_secret(self.mount_point, self.path, secrets):
                    display.vvv(f"update for key {self.key} failed, let's check")
                    new_secrets, new_version, new_meta = self.hvac_wrapper.read_path(self.mount_point, self.path)
                    if self.key not in new_secrets:
                        display.vvv(f"{self.key} is still absent, retry")
                        continue
                    if self.force_renew and secrets.get(self.key, None) == new_secrets[self.key]:
                        display.vvv(f"{self.key} was not renewed, retry")
                        continue
                    display.vvv("new version of secret is valid, use it")
                    secrets = new_secrets
                    break
            else:
                break
        if self.field:
            return [secrets[self.field]]
        else:
            return [secrets]
