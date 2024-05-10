Cosmos_node
=========

Install cosmos node with

- ability to import wallet from vault
- ability to import validator privkey from vault

Requirements
------------

None

Role Variables
--------------

```yaml
```

Dependencies
------------

```
dependencies:
  - name: tocard.utils.user
    user_name: "{{ cosmos_node_user }}"
    user_group: "{{ cosmos_node_group }}"
  - name: tocard.utils.filesystem
    filesystem_list: "{{ filebeat_filesystem_list }}"
```

Example Playbook
----------------

```yaml
---
## --------------------------------------------------------------------
## Filebeat
## --------------------------------------------------------------------
- hosts: filebeat
  tags:
    - filebeat
  roles:
    - role: tocard.utils.filebeat



```

License
-------

BSD

