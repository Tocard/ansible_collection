Metricbeat
=========

Install metricbeat on linux

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
## --------------------------------------------------------------------
## Metricbeat
## --------------------------------------------------------------------
- hosts: metricbeat
  tags:
    - metricbeat
  roles:
    - role: tocard.utils.filesystem
      filesystem_list: "{{ metricbeat_filesystem_list }}"
    - role: metricbeat



```

License
-------

BSD

