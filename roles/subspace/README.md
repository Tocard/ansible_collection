# subspace

this role simply install & configure subspace node & farmer

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [subspace_binary](#subspace_binary)
  - [subspace_chain_id](#subspace_chain_id)
  - [subspace_custom_become_method](#subspace_custom_become_method)
  - [subspace_donwload_binary_enabled](#subspace_donwload_binary_enabled)
  - [subspace_extra_package](#subspace_extra_package)
  - [subspace_github_url](#subspace_github_url)
  - [subspace_group](#subspace_group)
  - [subspace_install_path](#subspace_install_path)
  - [subspace_logrotate_folder](#subspace_logrotate_folder)
  - [subspace_node_binary_name](#subspace_node_binary_name)
  - [subspace_node_binary_path](#subspace_node_binary_path)
  - [subspace_node_binary_url](#subspace_node_binary_url)
  - [subspace_node_directories](#subspace_node_directories)
  - [subspace_node_dsn_port](#subspace_node_dsn_port)
  - [subspace_node_filesystem_disk_mounts](#subspace_node_filesystem_disk_mounts)
  - [subspace_node_filesystem_enabled](#subspace_node_filesystem_enabled)
  - [subspace_node_filesystem_lvs_mounts](#subspace_node_filesystem_lvs_mounts)
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
  - [subspace_operator_filesystem_lvs_mounts](#subspace_operator_filesystem_lvs_mounts)
  - [subspace_operator_install_enabled](#subspace_operator_install_enabled)
  - [subspace_operator_install_path](#subspace_operator_install_path)
  - [subspace_operator_log_file](#subspace_operator_log_file)
  - [subspace_operator_log_folder](#subspace_operator_log_folder)
  - [subspace_operator_logrotate_file](#subspace_operator_logrotate_file)
  - [subspace_operator_p2p_port](#subspace_operator_p2p_port)
  - [subspace_operator_prometheus_port](#subspace_operator_prometheus_port)
  - [subspace_operator_templates](#subspace_operator_templates)
  - [subspace_snapshot](#subspace_snapshot)
  - [subspace_user](#subspace_user)
  - [suspace_custom_vg_name](#suspace_custom_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### subspace_binary

#### Default value

```YAML
subspace_binary: ubuntu-x86_64-skylake
```

### subspace_chain_id

#### Default value

```YAML
subspace_chain_id: mainnet
```

### subspace_custom_become_method

#### Default value

```YAML
subspace_custom_become_method: sudo
```

### subspace_donwload_binary_enabled

#### Default value

```YAML
subspace_donwload_binary_enabled: true
```

### subspace_extra_package

#### Default value

```YAML
subspace_extra_package:
  - libgomp1
  - logrotate
```

### subspace_github_url

#### Default value

```YAML
subspace_github_url: https://github.com/subspace/subspace/releases/download
```

### subspace_group

#### Default value

```YAML
subspace_group: subspace
```

### subspace_install_path

#### Default value

```YAML
subspace_install_path: /opt/subspace
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
subspace_node_binary_path: /usr/bin/{{ subspace_node_binary_name }}
```

### subspace_node_binary_url

#### Default value

```YAML
subspace_node_binary_url: '{{ subspace_github_url }}/{{ subspace_snapshot }}/subspace-node-{{
  subspace_binary }}-{{ subspace_snapshot }}'
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

### subspace_node_filesystem_disk_mounts

#### Default value

```YAML
subspace_node_filesystem_disk_mounts:
  - disk: sdb
    path: '{{ subspace_node_install_path }}'
    owner: '{{ subspace_user }}'
    group: '{{ subspace_group }}'
```

### subspace_node_filesystem_enabled

#### Default value

```YAML
subspace_node_filesystem_enabled: true
```

### subspace_node_filesystem_lvs_mounts

#### Default value

```YAML
subspace_node_filesystem_lvs_mounts:
  - lv: lv_subspace_node_log
    vg: '{{ suspace_custom_vg_name }}'
    size: 2g
    path: '{{ subspace_node_log_folder }}'
    owner: '{{ subspace_user }}'
    group: '{{ subspace_group }}'
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
subspace_operator_binary_path: /usr/bin/{{ subspace_operator_binary_name }}
```

### subspace_operator_binary_url

#### Default value

```YAML
subspace_operator_binary_url: '{{ subspace_github_url }}/{{ subspace_snapshot }}/subspace-node-{{
  subspace_binary }}-{{ subspace_snapshot }}'
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

### subspace_operator_filesystem_lvs_mounts

#### Default value

```YAML
subspace_operator_filesystem_lvs_mounts:
  - lv: lv_subspace_operator_log
    vg: '{{ suspace_custom_vg_name }}'
    size: 2g
    path: '{{ subspace_operator_log_folder }}'
    owner: '{{ subspace_user }}'
    group: '{{ subspace_group }}'
```

### subspace_operator_install_enabled

#### Default value

```YAML
subspace_operator_install_enabled: false
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

### subspace_snapshot

#### Default value

```YAML
subspace_snapshot: '{{ subspace_chain_id }}-2024-nov-13'
```

### subspace_user

#### Default value

```YAML
subspace_user: subspace
```

### suspace_custom_vg_name

#### Default value

```YAML
suspace_custom_vg_name: olympus
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
