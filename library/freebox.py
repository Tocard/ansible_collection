#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: freebox

short_description: This module wrap some endpoint of freebox (illiad internet provider)
version_added: "2.9"

description: It will allow you to handle static lease, dynamic, & port forwarding

options:
      app_id:
        description: The app id (display & identifiaction purpose only)
        type: str
        default: fr.freebox.integration
      app_name:
        description: The app Name (display & identifiaction purpose only)
        type: str
        default: freebox_ansible
      app_token:
        description: Token get at the first connexion & approval, if not present it will be harvested and set to vault
        type: str
      app_version:
        description: The app version (used for modification should be updated anytime you change something)
        type: str
        default: 0.1
      device_name:
        description: This is the device name (display & identifiaction purpose only)
        type: str
        default: ansible_integration
      freebox_url:
        description: Change it if you use a custom freebox url
        type: str
        default: http://mafreebox.freebox.fr/api/v8
      vault_username:
        description: Vault user to connect on hashicorp vault (app_token storage)
        required: true
        type: str
      vault_password:
        description: Vault password to connect on hashicorp vault (app_token storage)
        required: true
        type: str
      vault_url:
        description: Vault url to connect on hashicorp vault (app_token storage)
        required: true
        type: str
      vault_path:
        description: vault secret path to read/set
        required: true
        type: str
      vault_mount_point:
        description: vault mountpoint to use
        required: true
        type: str
author:
    - Douceur (@Tocard)
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.utils.display import Display
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.common import yaml
from hvac.exceptions import VaultError, InvalidPath, InvalidRequest

import requests
import hashlib
import hmac
import hvac
import os

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
            display.warning(secret)
            return secret
        except InvalidPath:
            display.warning("path {} does not exist yet".format(self.path))
            return {}
        except VaultError as e:
            display.warning("{}".format(e))
            raise AnsibleError("Unable to read vault path {} at mount point {}".format(self.path, self.mount_point), e)

    def create_or_update_secret(self, secret: dict):
        try:
            self.client.secrets.kv.v2.create_or_update_secret(
                path=self.path, secret=secret, mount_point=self.mount_point)
            display.vvv("secrets have been created or updated in path {}".format(self.path))
            return True
        except InvalidRequest as e:
            display.warning(f"secrets not updated in path {self.path} because of invalid request {e}")
            return False
        except AnsibleParserError as e:
            raise AnsibleError("{}, {}, {}, {}".format(self.mount_point, self.path, secret, e))


class Freebox(VaultWrapper):
    def __init__(self, app_id, app_name, app_version, device_name, freebox_url, username, password,
                 vault_addr, vault_mount_point, vault_path, app_token=None):
        super().__init__(username, password, vault_addr, vault_mount_point, vault_path)
        self.app_token = app_token
        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self.device_name = device_name
        self.freebox_url = freebox_url
    track_id = None

        ##### AUTH #####


    def check_if_app_is_ok(self):
        endpoint = '{}/login/authorize/{}'.format(self.freebox_url, self.track_id)
        resp = requests.get(endpoint)
        status = resp.json()['result']['status']
        while status == 'pending':
            resp = requests.get(endpoint)
            status = resp.json()['result']['status']


    def create_or_get_token(self) -> None:
        if self.app_token is not None:
            return None
        endpoint = '{}/login/authorize/'.format(self.freebox_url)
        data = {
            'app_id': self.app_id,
            'app_name': self.app_name,
            'app_version': self.app_version,
            'device_name': self.device_name
        }

        resp = requests.post(endpoint, json=data)
        self.track_id = resp.json()['result']['track_id']
        secrets = self.read_path()
        display.warning('{}'.format(secrets))
        self.check_if_app_is_ok()
        if resp.status_code == 200:
            self.app_token = resp.json()['result']['app_token']
            return None
        else:
            raise AnsibleError('Authorization Error:', resp.status_code, resp.text)


    def get_challenge(self):
        endpoint = '{}/login/'.format(self.freebox_url)
        resp = requests.get(endpoint)
        self.challenge = resp.json()['result']['challenge']


    def create_session(self):
        token_bytes = bytes(self.app_token, 'latin-1')
        challenge_bytes = bytes(self.challenge, 'latin-1')
        password = hmac.new(token_bytes, challenge_bytes, hashlib.sha1).hexdigest()
        endpoint = '{}/login/session/'.format(self.freebox_url)
        data = {
            'app_id': self.app_id,
            'password': password,
            'app_version': self.app_version
        }

        resp = requests.Session().post(endpoint, json=data).json()
        self.session_token = resp['result']['session_token']

        ##### DHCP #####


    def get_static_lease(self):
        endpoint = '{}/dhcp/static_lease/'.format(self.freebox_url)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        lan = resp.json()['result']
        return lan


    def update_static_lease(self, mac: str, data: dict):
        # {
        #     'comment': '',
        #  'hostname': 'Pc de r0ro',
        #  'id': '00:DE:AD:B0:0B:55',
        #  'host': {
        #      [...]
        #  },
        #  'ip': '192.168.1.1'
        #
        #  }
        endpoint = '{}/dhcp/static_lease/{}'.format(self.freebox_url, mac)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.put(endpoint, headers=headers, json=data)
        # TODO: end it
        lan = resp.json()['result']


    def create_static_lease(self, mac: str, data: dict):
        # {
        #    'ip': '192.168.1.222',
        #    'mac': '00:00:00:11:11:11'
        # }
        endpoint = '{}/dhcp/static_lease/{}'.format(self.freebox_url, mac)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.post(endpoint, headers=headers, json=data)
        lease = resp.json()['result']


    def delete_static_lease(self, mac: str):
        endpoint = '{}/dhcp/static_lease/{}'.format(self.freebox_url, mac)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.delete(endpoint, headers=headers)
        # TODO: end it
        lan = resp.json()['result']


    def get_dynamic_lease(self):
        endpoint = '{}/dhcp/dynamic_lease/'.format(self.freebox_url)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        lan = resp.json()['result']


    ##### PORT FORWARDING #####

    def get_all_port_forwarding(self):
        endpoint = '{}/fw/redir/'.format(self.freebox_url)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        ports = resp.json()['result']


    def get_port_forwarding(self, port_id: int):
        endpoint = '{}/fw/redir/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        port = resp.json()['result']


    def update_port_forwarding(self, port_id: int):
        endpoint = '{}/fw/redir/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        port = resp.json()['result']


    def delete_port_forwarding(self, port_id: int):
        endpoint = '{}/fw/redir/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.delete(endpoint, headers=headers)
        port = resp.json()['result']


    def create_port_forwarding(self, data: int):
        # {
        #     'enabled': true,
        #     'comment': 'test',
        #     'lan_port': 4242,
        #     'wan_port_end': 4242,
        #     'wan_port_start': 4242,
        #     'lan_ip': '192.168.1.42',
        #     'ip_proto': 'tcp',
        #     'src_ip': '0.0.0.0'
        # }
        endpoint = '{}/fw/redir/'.format(self.freebox_url)
        headers = {
            'X-Fbx-App-Auth': self.session_token

        }
        resp = requests.post(endpoint, headers=headers)
        port = resp.json()['result']


    ##### PORT INCOMING #####

    def get_all_port_incoming(self):
        endpoint = '{}/fw/incoming/'.format(self.freebox_url)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        ports = resp.json()['result']


    def get_port_incoming(self, port_id: int):
        endpoint = '{}/fw/incoming/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        port = resp.json()['result']


    def update_port_incoming(self, port_id: int):
        endpoint = '{}/fw/incoming/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        port = resp.json()['result']


    def delete_port_incoming(self, port_id: int):
        endpoint = '{}/fw/incoming/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.delete(endpoint, headers=headers)
        port = resp.json()['result']


    def create_port_incoming(self, data: int):
        # {
        #     'enabled': true,
        #     'comment': 'test',
        #     'lan_port': 4242,
        #     'wan_port_end': 4242,
        #     'wan_port_start': 4242,
        #     'lan_ip': '192.168.1.42',
        #     'ip_proto': 'tcp',
        #     'src_ip': '0.0.0.0'
        # }
        endpoint = '{}/fw/incoming/'.format(self.freebox_url)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.post(endpoint, headers=headers)
        port = resp.json()['result']


def run_module():
    module_args = dict(
        app_id=dict(type='str', default='fr.freebox.integration'),
        app_name=dict(type='str', default='freebox_ansible)'),
        app_token=dict(type='str'),
        app_version=dict(type='str', default='0.1'),
        device_name=dict(type='str', default='ansible_integration'),
        freebox_url=dict(type='str', default='http://mafreebox.freebox.fr/api/v8'),
        vault_username=dict(type='str', required=True),
        vault_password=dict(type='str', required=True),
        vault_url=dict(type='str', required=True),
        vault_path=dict(type='str', required=True),
        vault_mount_point=dict(type='str', required=True),

    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    result['original_message'] = 'orginal_message'
    result['message'] = 'goodbye'

    client = Freebox(app_id=module.params['app_id'], app_name=module.params['app_name'],
                     app_version=module.params['app_version'], device_name=module.params['device_name'],
                     freebox_url=module.params['freebox_url'],
                     app_token=module.params['app_token'], username=module.params["vault_username"],
                     password=module.params["vault_password"],
                     vault_addr=module.params["vault_url"], vault_mount_point=module.params["vault_mount_point"],
                     vault_path=module.params["vault_path"])

    client.create_or_get_token()
    client.get_challenge()
    client.create_session()
    sample = client.get_static_lease()
    display.warning(sample)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
