Vault
=========

Install vault on linux

Requirements
------------

You need to pass context for cerbot or disable ssl to run it. If vault is already up, you should have the context for certbot into vault itself.

Role Variables
--------------

```yaml
```

Dependencies
------------

Ig you want to use ssl, you must provide them into

````yaml

````

if you want to use the same pattern, use cerbot role https://galaxy.ansible.com/ui/repo/published/tocard/utils/content/

Example Playbook
----------------

```yaml
---
## --------------------------------------------------------------------
## vault
## --------------------------------------------------------------------
- hosts: vault
  tags:
    - vault
  roles:
    - role: tocard.utils.user
      user_name: "{{ vault_user }}"
      user_group: "{{ vault_group }}"
    - role: tocard.utils.filesystem
      filesystem_list: "{{ vault_filesystem_list }}"
      tags:
        - vault
    - role: vault
      tags:
        - vault

```

License
-------

BSD

