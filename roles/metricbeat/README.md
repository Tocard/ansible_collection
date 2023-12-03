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

```
dependencies:
  - name: tocard.utils.filesystem
    filesystem_list: "{{ metricbeat_filesystem_list }}"
```

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
    - role: tocard.utils.metricbeat



```

License
-------

BSD

