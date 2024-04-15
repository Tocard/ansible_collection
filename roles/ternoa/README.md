Ternoa
=========

Install ternoa on linux.

It will use filesystem if enabled or raw disk.

Requirements
------------

None

Role Variables
--------------

```yaml
---

ternoa_node_install_enabled: true
ternoa_node_filesystem_enabled: true


```

Dependencies
------------

Theses dependencies are from the collection itself.

````yaml
dependencies:
  - name: tocard.utils.user
    user_name: "{{ ternoa_owner }}"
    user_group: "{{ ternoa_group }}"
    tags: ['user']

  - name: tocard.utils.filesystem
    filesystem_list: "{{ ternoa_node_filesystem_list }}"
    when: ternoa_node_filesystem_enabled and ternoa_node_install_enabled
    tags: ['filesystem']

````


Example Playbook
----------------

```yaml
---
#==================================================================
# ternoa Automatic Deployment
#==================================================================
- hosts: ternoa
  roles:
    - role: tocard.utils.ternoa
      tags:
        - ternoa

```

License
-------

BSD

