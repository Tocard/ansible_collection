Streamr Node
=========

Install Streamr on linux

Requirements
------------

```


```

None

Role Variables
--------------

```yaml
streamr_operator_contract_adress: "0x25f83066055bc49395ffa782325f1f19c59e1358"
streamr_node_priv_key: "0xreplace_with_your_own_key_but_consider_about_using_vault"

streamr_node_version: v100.0.0-testnet-one.2

streamr_node_port_min: 32200 # change if you want to change port
streamr_node_port_max: 32200
```

If you plan (and you should) use lvm keep it like this and overide stuff. simply put it to false will disable feature
````yaml
streamr_filesystem_enabled: true
streamr_virtual_group_name: data_virtual
streamr_lv_data_size: 10G
streamr_lv_log_size: 1G
streamr_filesystem_list:
  - lv: lv_streamr_data
    vg: "{{ streamr_virtual_group_name }}"
    size: "{{ streamr_lv_data_size }}"
    path: "{{ streamr_install_dir }}"
    owner: "{{ streamr_user }}"
    group: "{{ streamr_group }}"
    mode: "0750"
    fstype: xfs
    force: false
    shrink: false
  - lv: lv_streamr_log
    vg: "{{ streamr_virtual_group_name }}"
    size: "{{ streamr_lv_log_size }}"
    path: "{{ streamr_log_dir }}"
    owner: "{{ streamr_user }}"
    group: "{{ streamr_group }}"
    mode: "0750"
    fstype: xfs
    force: false
    shrink: false

````

swapping this to true will install metricbeat and send metrics vps health over time to my monitoring stack.
Your server will show up here
https://mythologic.fr/d/QX3P3t7iz/olympus-os-overview?orgId=7&refresh=5s

This is an experimental feature subject to evole (like adding node monitoring feature)
````yaml
streamr_supervision_enabled: false

````

Dependencies
------------

````shell
ansible-galaxy collection install community.general
ansible-galaxy role install morgangraphics.ansible_role_nvm
````

```yml
dependencies:
  - name: tocard.utils.user
  - name: tocard.utils.filesystem
  - name: morgangraphics.nvm
```

Example Playbook
----------------

```yaml
---

#==================================================================
# Streamr
#==================================================================

- hosts: streamr
  roles:
    - role: tocard.utils.user.streamr
      tags:
        - streamr

```

License
-------

BSD

