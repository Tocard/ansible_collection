Filebeat
=========

Install filebeat on linux

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

