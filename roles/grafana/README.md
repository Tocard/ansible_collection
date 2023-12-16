Grafana
=========

Install grafana on linux

Requirements
------------

None

Role Variables
--------------

```yaml
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
---
#==================================================================
# GRAFANA
#==================================================================
- hosts: grafana
  roles:
    - role: tocard.utils.user
      user_name: grafana
      user_group: grafana
    - role: tocard.utils.filesystem
      filesystem_list: "{{ grafana_filesystem_list }}"
      tags:
        - filesystem
        - grafana
    - role: grafana
      tags:
        - grafana
```

License
-------

BSD

