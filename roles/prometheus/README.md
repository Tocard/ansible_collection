prometheus
=========

Install Prometheus on linux

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
---
#==================================================================
# prometheus
#==================================================================
- hosts: gorgons
  roles:
    - role: tocard.utils.user
      user_name: "{{ prometheus_owner }}"
      user_group: "{{ prometheus_group }}"
    - role: prometheus
      tags:
        - prometheus
```

License
-------

BSD

