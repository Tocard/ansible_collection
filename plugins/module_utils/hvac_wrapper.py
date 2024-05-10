
from hvac.exceptions import VaultError, InvalidPath, InvalidRequest
import hvac
from ansible.module_utils.basic import AnsibleModule
from ansible.utils.display import Display
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.common import yaml

display = Display()


class VaultWrapper:
    def __init__(self, username, password, vault_addr, vault_mount_point, vault_path):
        self.vault_addr = vault_addr
        self.username = username
        self.password = password
        self.mount_point = vault_mount_point
        self.path = vault_path
        self.init_hvac_client()
    client = None

    def init_hvac_client(self):
        self.client = hvac.Client(url=self.vault_addr)
        self.client.auth.userpass.login(username=self.username, password=self.password)

    def read_path(self) -> dict:
        try:
            data = self.client.secrets.kv.v2.read_secret_version(
                path=self.path, mount_point=self.mount_point)
            secret = data['data']['data']
            return secret
        except InvalidPath:
            display.warning("path {}/{} does not exist yet".format(self.mount_point, self.path))
            return {}
        except VaultError as e:
            display.warning("{}".format(e))
            raise AnsibleError("Unable to read vault path {} at mount point {}".format(self.path, self.mount_point), e)

    def create_or_update_secret(self, secret: dict):
        try:
            self.client.secrets.kv.v2.create_or_update_secret(
                path=self.path, secret=secret, mount_point=self.mount_point)
            display.warning("secrets have been created or updated in path {}".format(self.path))
            return True
        except InvalidRequest as e:
            display.warning(f"secrets not updated in path {self.path} because of invalid request {e}")
            return False
        except AnsibleParserError as e:
            raise AnsibleError("{}, {}, {}, {}".format(self.mount_point, self.path, secret, e))

