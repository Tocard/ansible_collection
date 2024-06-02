# subspace

this role simply install & configure subspace node & farmer

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [subspace_farmer_plot_size](#subspace_farmer_plot_size)
  - [subspace_binary](#subspace_binary)
  - [subspace_chain_id](#subspace_chain_id)
  - [subspace_custom_become_method](#subspace_custom_become_method)
  - [subspace_donwload_binary](#subspace_donwload_binary)
  - [subspace_extra_package](#subspace_extra_package)
  - [subspace_farmer_binary_name](#subspace_farmer_binary_name)
  - [subspace_farmer_binary_path](#subspace_farmer_binary_path)
  - [subspace_farmer_binary_url](#subspace_farmer_binary_url)
  - [subspace_farmer_directories](#subspace_farmer_directories)
  - [subspace_farmer_filesystem_enabled](#subspace_farmer_filesystem_enabled)
  - [subspace_farmer_filesystem_list](#subspace_farmer_filesystem_list)
  - [subspace_farmer_install_enabled](#subspace_farmer_install_enabled)
  - [subspace_farmer_install_path](#subspace_farmer_install_path)
  - [subspace_farmer_log_file](#subspace_farmer_log_file)
  - [subspace_farmer_log_folder](#subspace_farmer_log_folder)
  - [subspace_farmer_logrotate_file](#subspace_farmer_logrotate_file)
  - [subspace_farmer_node_rpc_url](#subspace_farmer_node_rpc_url)
  - [subspace_farmer_port](#subspace_farmer_port)
  - [subspace_farmer_templates](#subspace_farmer_templates)
  - [subspace_farmer_wallet_adress](#subspace_farmer_wallet_adress)
  - [subspace_github_url](#subspace_github_url)
  - [subspace_group](#subspace_group)
  - [subspace_install_path](#subspace_install_path)
  - [subspace_log_path_to_watch](#subspace_log_path_to_watch)
  - [subspace_logrotate_folder](#subspace_logrotate_folder)
  - [subspace_node_binary_name](#subspace_node_binary_name)
  - [subspace_node_binary_path](#subspace_node_binary_path)
  - [subspace_node_binary_url](#subspace_node_binary_url)
  - [subspace_node_directories](#subspace_node_directories)
  - [subspace_node_dsn_port](#subspace_node_dsn_port)
  - [subspace_node_filesystem_enabled](#subspace_node_filesystem_enabled)
  - [subspace_node_filesystem_list](#subspace_node_filesystem_list)
  - [subspace_node_install_enabled](#subspace_node_install_enabled)
  - [subspace_node_install_path](#subspace_node_install_path)
  - [subspace_node_log_file](#subspace_node_log_file)
  - [subspace_node_log_folder](#subspace_node_log_folder)
  - [subspace_node_logrotate_file](#subspace_node_logrotate_file)
  - [subspace_node_p2p_port](#subspace_node_p2p_port)
  - [subspace_node_prometheus_port](#subspace_node_prometheus_port)
  - [subspace_node_templates](#subspace_node_templates)
  - [subspace_operator_binary_name](#subspace_operator_binary_name)
  - [subspace_operator_binary_path](#subspace_operator_binary_path)
  - [subspace_operator_binary_url](#subspace_operator_binary_url)
  - [subspace_operator_directories](#subspace_operator_directories)
  - [subspace_operator_dsn_port](#subspace_operator_dsn_port)
  - [subspace_operator_filesystem_enabled](#subspace_operator_filesystem_enabled)
  - [subspace_operator_filesystem_list](#subspace_operator_filesystem_list)
  - [subspace_operator_install_enabled](#subspace_operator_install_enabled)
  - [subspace_operator_install_path](#subspace_operator_install_path)
  - [subspace_operator_log_file](#subspace_operator_log_file)
  - [subspace_operator_log_folder](#subspace_operator_log_folder)
  - [subspace_operator_logrotate_file](#subspace_operator_logrotate_file)
  - [subspace_operator_p2p_port](#subspace_operator_p2p_port)
  - [subspace_operator_prometheus_port](#subspace_operator_prometheus_port)
  - [subspace_operator_templates](#subspace_operator_templates)
  - [subspace_owner](#subspace_owner)
  - [subspace_snapshot](#subspace_snapshot)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### subspace_farmer_plot_size

#### Default value

```YAML
subspace_farmer_plot_size: 10g
```

### subspace_binary

#### Default value

```YAML
subspace_binary: ubuntu-x86_64-skylake
```

### subspace_chain_id

#### Default value

```YAML
subspace_chain_id: gemini-3h
```

### subspace_custom_become_method

#### Default value

```YAML
subspace_custom_become_method: sudo
```

### subspace_donwload_binary

#### Default value

```YAML
subspace_donwload_binary: true
```

### subspace_extra_package

#### Default value

```YAML
subspace_extra_package:
  - libgomp1
  - nginx
  - logrotate
```

### subspace_farmer_binary_name

#### Default value

```YAML
subspace_farmer_binary_name: subspace_farmer
```

### subspace_farmer_binary_path

#### Default value

```YAML
subspace_farmer_binary_path: /usr/bin/{{ subspace_farmer_binary_name}}
```

### subspace_farmer_binary_url

#### Default value

```YAML
subspace_farmer_binary_url: '{{ subspace_github_url }}/{{ subspace_snapshot }}/subspace-farmer-{{
  subspace_binary }}-{{ subspace_snapshot}}'
```

### subspace_farmer_directories

#### Default value

```YAML
subspace_farmer_directories:
  - path: '{{ subspace_farmer_install_path }}'
  - path: '{{ subspace_farmer_log_folder }}'
  - path: '{{ subspace_farmer_install_path }}/ssd'
  - path: '{{ subspace_farmer_install_path }}/nvme'
```

### subspace_farmer_filesystem_enabled

#### Default value

```YAML
subspace_farmer_filesystem_enabled: true
```

### subspace_farmer_filesystem_list

#### Default value

```YAML
subspace_farmer_filesystem_list:
  - lv: lv_subspace_farmer_log
    vg: '{{ custom_vg_name }}'
    size: 2g
    path: '{{ subspace_farmer_log_folder }}'
    owner: '{{ subspace_owner }}'
    group: '{{ subspace_group }}'
```

### subspace_farmer_install_enabled

#### Default value

```YAML
subspace_farmer_install_enabled: true
```

### subspace_farmer_install_path

#### Default value

```YAML
subspace_farmer_install_path: '{{ subspace_install_path }}/farmer'
```

### subspace_farmer_log_file

#### Default value

```YAML
subspace_farmer_log_file: farmer.log
```

### subspace_farmer_log_folder

#### Default value

```YAML
subspace_farmer_log_folder: /var/log/chimera/subspace_farmer
```

### subspace_farmer_logrotate_file

#### Default value

```YAML
subspace_farmer_logrotate_file: subspace_farmer
```

### subspace_farmer_node_rpc_url

#### Default value

```YAML
subspace_farmer_node_rpc_url: ws://127.0.0.1:9944
```

### subspace_farmer_port

#### Default value

```YAML
subspace_farmer_port: 30533
```

### subspace_farmer_templates

#### Default value

```YAML
subspace_farmer_templates:
  - src: subspace_farmer.service.j2
    dest: /etc/systemd/system/subspace_farmer.service
    mode: '0640'
  - src: subspace_farmer.j2
    dest: '{{ subspace_logrotate_folder }}/{{ subspace_farmer_logrotate_file }}'
```

### subspace_farmer_wallet_adress

#### Default value

```YAML
subspace_farmer_wallet_adress: "{{ lookup('hashi_vault', hashi_subspace_path ~ '/wallet:moz
  ' ~ hashi_connect) }}"
```

### subspace_github_url

#### Default value

```YAML
subspace_github_url: https://github.com/subspace/subspace/releases/download
```

### subspace_group

#### Default value

```YAML
subspace_group: chimera
```

### subspace_install_path

#### Default value

```YAML
subspace_install_path: /opt/chimera
```

### subspace_log_path_to_watch

#### Default value

```YAML
subspace_log_path_to_watch: []
```

### subspace_logrotate_folder

#### Default value

```YAML
subspace_logrotate_folder: /etc/logrotate.d
```

### subspace_node_binary_name

#### Default value

```YAML
subspace_node_binary_name: subspace_node
```

### subspace_node_binary_path

#### Default value

```YAML
subspace_node_binary_path: /usr/bin/{{ subspace_node_binary_name}}
```

### subspace_node_binary_url

#### Default value

```YAML
subspace_node_binary_url: '{{ subspace_github_url }}/{{ subspace_snapshot }}/subspace-node-{{
  subspace_binary }}-{{ subspace_snapshot}}'
```

### subspace_node_directories

#### Default value

```YAML
subspace_node_directories:
  - path: '{{ subspace_node_install_path }}'
  - path: '{{ subspace_node_log_folder }}'
```

### subspace_node_dsn_port

#### Default value

```YAML
subspace_node_dsn_port: 30433
```

### subspace_node_filesystem_enabled

#### Default value

```YAML
subspace_node_filesystem_enabled: true
```

### subspace_node_filesystem_list

#### Default value

```YAML
subspace_node_filesystem_list:
  - lv: lv_chimera
    vg: '{{ custom_vg_name }}'
    size: 10g
    path: '{{ subspace_install_path }}'
    owner: '{{ subspace_owner }}'
    group: '{{ subspace_group }}'
    mode: '0750'
    fstype: xfs
    force: false
    shrink: false
  - lv: lv_subspace_node_log
    vg: '{{ custom_vg_name }}'
    size: 2g
    path: '{{ subspace_node_log_folder }}'
    owner: '{{ subspace_owner }}'
    group: '{{ subspace_group }}'
    mode: '0750'
    fstype: xfs
    force: false
    shrink: false
```

### subspace_node_install_enabled

#### Default value

```YAML
subspace_node_install_enabled: true
```

### subspace_node_install_path

#### Default value

```YAML
subspace_node_install_path: '{{ subspace_install_path }}/node'
```

### subspace_node_log_file

#### Default value

```YAML
subspace_node_log_file: node.log
```

### subspace_node_log_folder

#### Default value

```YAML
subspace_node_log_folder: /var/log/chimera/subspace_node
```

### subspace_node_logrotate_file

#### Default value

```YAML
subspace_node_logrotate_file: subspace_node
```

### subspace_node_p2p_port

#### Default value

```YAML
subspace_node_p2p_port: 30333
```

### subspace_node_prometheus_port

#### Default value

```YAML
subspace_node_prometheus_port: 9615
```

### subspace_node_templates

#### Default value

```YAML
subspace_node_templates:
  - src: subspace_node.service.j2
    dest: /etc/systemd/system/subspace_node.service
    mode: '0640'
  - src: subspace_node.j2
    dest: '{{ subspace_logrotate_folder }}/{{ subspace_node_logrotate_file }}'
```

### subspace_operator_binary_name

#### Default value

```YAML
subspace_operator_binary_name: subspace_operator
```

### subspace_operator_binary_path

#### Default value

```YAML
subspace_operator_binary_path: /usr/bin/{{ subspace_operator_binary_name}}
```

### subspace_operator_binary_url

#### Default value

```YAML
subspace_operator_binary_url: '{{ subspace_github_url }}/{{ subspace_snapshot }}/subspace-node-{{
  subspace_binary }}-{{ subspace_snapshot}}'
```

### subspace_operator_directories

#### Default value

```YAML
subspace_operator_directories:
  - path: '{{ subspace_operator_install_path }}'
  - path: '{{ subspace_operator_log_folder }}'
```

### subspace_operator_dsn_port

#### Default value

```YAML
subspace_operator_dsn_port: 30433
```

### subspace_operator_filesystem_enabled

#### Default value

```YAML
subspace_operator_filesystem_enabled: true
```

### subspace_operator_filesystem_list

#### Default value

```YAML
subspace_operator_filesystem_list:
  - lv: lv_chimera
    vg: '{{ custom_vg_name }}'
    size: 10g
    path: '{{ subspace_install_path }}'
    owner: '{{ subspace_owner }}'
    group: '{{ subspace_group }}'
    mode: '0750'
    fstype: xfs
    force: false
    shrink: false
  - lv: lv_subspace_operator_log
    vg: '{{ custom_vg_name }}'
    size: 2g
    path: '{{ subspace_operator_log_folder }}'
    owner: '{{ subspace_owner }}'
    group: '{{ subspace_group }}'
    mode: '0750'
    fstype: xfs
    force: false
    shrink: false
```

### subspace_operator_install_enabled

#### Default value

```YAML
subspace_operator_install_enabled: true
```

### subspace_operator_install_path

#### Default value

```YAML
subspace_operator_install_path: '{{ subspace_install_path }}/node'
```

### subspace_operator_log_file

#### Default value

```YAML
subspace_operator_log_file: operator.log
```

### subspace_operator_log_folder

#### Default value

```YAML
subspace_operator_log_folder: /var/log/chimera/subspace_operator
```

### subspace_operator_logrotate_file

#### Default value

```YAML
subspace_operator_logrotate_file: subspace_operator
```

### subspace_operator_p2p_port

#### Default value

```YAML
subspace_operator_p2p_port: 30333
```

### subspace_operator_prometheus_port

#### Default value

```YAML
subspace_operator_prometheus_port: 9615
```

### subspace_operator_templates

#### Default value

```YAML
subspace_operator_templates:
  - src: subspace_operator.service.j2
    dest: /etc/systemd/system/subspace_operator.service
    mode: '0640'
  - src: subspace_operator.j2
    dest: '{{ subspace_logrotate_folder }}/{{ subspace_operator_logrotate_file }}'
```

### subspace_owner

#### Default value

```YAML
subspace_owner: chimera
```

### subspace_snapshot

#### Default value

```YAML
subspace_snapshot: '{{ subspace_chain_id }}-2024-may-01'
```



## Dependencies


## License

BSD-3-Clause

## Author

Douceur
