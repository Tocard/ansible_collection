Filesystem
=========

This role will allow you to create filesystem with lvm or create filesystem for the whole disk.

Requirements
------------

None

Role Variables
--------------

```yaml
kibana_filesystem_list:
  - lv: lv_kibana_data
    vg: "{{ custom_vg_name }}"
    size: 1G
    path: "{{ kibana_data_dir }}"
    owner: "{{ kibana_owner}}"
    group: "{{ kibana_group}}"
    mode: "0750"
    fstype: xfs
    force: false
    shrink: false

```

Dependencies
------------

None

Example Playbook
----------------

```yaml
    - role: filesystem
      filesystem_list: "{{ kibana_filesystem_list }}"
```

License
-------

BSD

