Vault
=========

Install vault on linux

Requirements
------------

None

Role Variables
--------------

```yaml
```

Dependencies
------------

Ig you want to use ssl, you must provide them into

````yaml
ssl_minimal_file:
  - src: "/etc/letsencrypt/live/{{ ansible_host }}/cert.pem"
    dest: /etc/vault.d/cert.pem
    user: vault
  - src: "/etc/letsencrypt/live/{{ ansible_host }}/chain.pem"
    dest: /etc/vault.d/chain.pem
    user: vault
  - src: "/etc/letsencrypt/live/{{ ansible_host }}/fullchain.pem"
    dest: /etc/vault.d/fullchain.pem
    user: vault
  - src: "/etc/letsencrypt/live/{{ ansible_host }}/privkey.pem"
    dest: /etc/vault.d/privkey.pem
    user: vault
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

