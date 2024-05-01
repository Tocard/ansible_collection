#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: freebox_dhcp

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
from ansible.module_utils import hvac_wrapper

import requests
import hashlib
import hmac

display = Display()


class Freebox(hvac_wrapper.VaultWrapper):
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
    session_token = None
    challenge = None

    def check_if_app_is_ok(self):
        endpoint = '{}/login/authorize/{}'.format(self.freebox_url, self.track_id)
        resp = requests.get(endpoint)
        status = resp.json()['result']['status']
        while status == 'pending':
            resp = requests.get(endpoint)
            status = resp.json()['result']['status']

    def create_or_get_token(self):
        secrets = self.read_path()
        if 'token' in secrets:
            self.app_token = secrets['token']
            return
        elif self.app_token is not None:
            return
        endpoint = '{}/login/authorize/'.format(self.freebox_url)
        data = {
            'app_id': self.app_id,
            'app_name': self.app_name,
            'app_version': self.app_version,
            'device_name': self.device_name
        }

        resp = requests.post(endpoint, json=data)
        self.track_id = resp.json()['result']['track_id']
        self.check_if_app_is_ok()
        if resp.status_code == 200:
            self.app_token = resp.json()['result']['app_token']
            self.create_or_update_secret({'token': self.app_token})
            return
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


