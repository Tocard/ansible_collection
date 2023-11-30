Loki
=========

Install Loki on linux

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
# Loki
#==================================================================
- hosts: gorgons
  roles:
    - role: tocard.utils.user
      user_name: "{{ loki_owner }}"
      user_group: "{{ loki_group }}"
    - role: loki
      tags:
        - loki
```

License
-------

BSD

