Subspace
=========

Install subspace on linux

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
# Chimera-Zeta-Subspace
#==================================================================
- hosts: subspace
  roles:
    - role: tocard.utils.filesystem
      filesystem_list: "{{ subspace_node_filesystem_list | union(subspace_farmer_filesystem_list) }}"
      tags:
        - subspace
    - role: subspace
      tags:
        - subspace
```

License
-------

BSD

