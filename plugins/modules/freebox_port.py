#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: freebox_port

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
from ansible.module_utils import freebox_base
from ansible.module_utils.common import yaml

import requests

display = Display()


class FreeboxPort(freebox_base.Freebox):
    def __init__(self, app_id, app_name, app_version, device_name, freebox_url, username, password,
                 vault_addr, vault_mount_point, vault_path, app_token=None):
        super().__init__(app_id, app_name, app_version, device_name, freebox_url, app_token, username, password,
                         vault_addr, vault_mount_point, vault_path)

    def get_all_port_forwarding(self):
        endpoint = '{}/fw/redir/'.format(self.freebox_url)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        ports = resp.json()['result']
        return ports

    def get_port_forwarding(self, port_id: int):
        endpoint = '{}/fw/redir/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        port = resp.json()['result']
        return port

    def update_port_forwarding(self, port_id: int):
        endpoint = '{}/fw/redir/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        port = resp.json()['result']
        return port

    def delete_port_forwarding(self, port_id: int):
        endpoint = '{}/fw/redir/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.delete(endpoint, headers=headers)
        port = resp.json()['result']
        return port

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
        return port

    ##### PORT INCOMING #####

    def get_all_port_incoming(self):
        endpoint = '{}/fw/incoming/'.format(self.freebox_url)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        ports = resp.json()['result']
        return ports

    def get_port_incoming(self, port_id: int):
        endpoint = '{}/fw/incoming/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        port = resp.json()['result']
        return port

    def update_port_incoming(self, port_id: int):
        endpoint = '{}/fw/incoming/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.get(endpoint, headers=headers)
        port = resp.json()['result']
        return port

    def delete_port_incoming(self, port_id: int):
        endpoint = '{}/fw/incoming/{}'.format(self.freebox_url, port_id)
        headers = {
            'X-Fbx-App-Auth': self.session_token
        }
        resp = requests.delete(endpoint, headers=headers)
        port = resp.json()['result']
        return port

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
        return port


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

    client = FreeboxPort(app_id=module.params['app_id'], app_name=module.params['app_name'],
                         app_version=module.params['app_version'], device_name=module.params['device_name'],
                         freebox_url=module.params['freebox_url'],
                         app_token=module.params['app_token'], username=module.params["vault_username"],
                         password=module.params["vault_password"],
                         vault_addr=module.params["vault_url"], vault_mount_point=module.params["vault_mount_point"],
                         vault_path=module.params["vault_path"])

    client.create_or_get_token()
    client.get_challenge()
    client.create_session()
    result['original_message'] = client.get_all_port_forwarding()
    result['message'] = client.get_all_port_forwarding()

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
