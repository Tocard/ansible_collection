Subspace
=========

Install subspace on linux.

This role can install farmer, node or operator as linux services.
It will use filesystem if enabled or raw disk.

Requirements
------------

None

Role Variables
--------------

```yaml
---

subspace_node_install_enabled: true
subspace_node_filesystem_enabled: true

subspace_operator_install_enabled: false
subspace_operator_filesystem_enabled: false

subspace_farmer_install_enabled: true
subspace_farmer_filesystem_enable: true

subspace_farmer_disks:
  - path=/mnt/subspace_001,size=1.8T
  - path=/mnt/subspace_002,size=1.8T
  - path=/mnt/subspace_003,size=900G
  - path=/mnt/hydras_alpha_fikwot4T_baie_top_left/alpha,size=3.7T
  - path={{ subspace_farmer_install_path }}/ssd,size=800G
  - path={{ subspace_farmer_install_path }}/nvme,size=900G




```

Dependencies
------------

Theses dependencies are from the collection itself.

````yaml
dependencies:
  - name: tocard.utils.user
    user_name: "{{ subspace_owner }}"
    user_group: "{{ subspace_group }}"
    tags: ['user']

  - name: tocard.utils.filesystem
    filesystem_list: "{{ subspace_node_filesystem_list }}"
    when: subspace_node_filesystem_enabled and subspace_node_install_enabled
    tags: ['filesystem']

  - name: tocard.utils.filesystem
    filesystem_list: "{{ subspace_operator_filesystem_list }}"
    when: subspace_operator_filesystem_enabled and subspace_operator_install_enabled
    tags: ['filesystem']

  - name: tocard.utils.filesystem
    filesystem_list: "{{ subspace_farmer_filesystem_list }}"
    when: subspace_farmer_filesystem_enabled and subspace_farmer_install_enabled
    tags: ['filesystem']
````


Example Playbook
----------------

```yaml
---
#==================================================================
# Subspace Automatic Deployment
#==================================================================
- hosts: subspace
  roles:
    - role: tocard.utils.subspace
      tags:
        - subspace

```

License
-------

BSD

