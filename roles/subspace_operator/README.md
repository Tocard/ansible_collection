# subspace_operator

this role simply install & configure subspace node & make an operator

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [subspace_operator_binary](#subspace_operator_binary)
  - [subspace_operator_binary_name](#subspace_operator_binary_name)
  - [subspace_operator_binary_path](#subspace_operator_binary_path)
  - [subspace_operator_binary_url](#subspace_operator_binary_url)
  - [subspace_operator_chain_id](#subspace_operator_chain_id)
  - [subspace_operator_directories](#subspace_operator_directories)
  - [subspace_operator_donwload_binary_enabled](#subspace_operator_donwload_binary_enabled)
  - [subspace_operator_dsn_port](#subspace_operator_dsn_port)
  - [subspace_operator_extra_package](#subspace_operator_extra_package)
  - [subspace_operator_filesystem_disk_mounts](#subspace_operator_filesystem_disk_mounts)
  - [subspace_operator_filesystem_enabled](#subspace_operator_filesystem_enabled)
  - [subspace_operator_filesystem_lvs_mounts](#subspace_operator_filesystem_lvs_mounts)
  - [subspace_operator_github_url](#subspace_operator_github_url)
  - [subspace_operator_group](#subspace_operator_group)
  - [subspace_operator_log_file](#subspace_operator_log_file)
  - [subspace_operator_log_folder](#subspace_operator_log_folder)
  - [subspace_operator_logrotate_file](#subspace_operator_logrotate_file)
  - [subspace_operator_logrotate_folder](#subspace_operator_logrotate_folder)
  - [subspace_operator_node_path](#subspace_operator_node_path)
  - [subspace_operator_p2p_port](#subspace_operator_p2p_port)
  - [subspace_operator_prometheus_port](#subspace_operator_prometheus_port)
  - [subspace_operator_root_path](#subspace_operator_root_path)
  - [subspace_operator_snapshot](#subspace_operator_snapshot)
  - [subspace_operator_templates](#subspace_operator_templates)
  - [subspace_operator_user](#subspace_operator_user)
  - [suspace_operator_custom_vg_name](#suspace_operator_custom_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### subspace_operator_binary

#### Default value

```YAML
subspace_operator_binary: ubuntu-x86_64-skylake
```

### subspace_operator_binary_name

#### Default value

```YAML
subspace_operator_binary_name: subspace
```

### subspace_operator_binary_path

#### Default value

```YAML
subspace_operator_binary_path: /usr/bin/{{ subspace_operator_binary_name }}
```

### subspace_operator_binary_url

#### Default value

```YAML
subspace_operator_binary_url: '{{ subspace_operator_github_url }}/{{ subspace_operator_snapshot
  }}/subspace-node-{{ subspace_operator_binary }}-{{ subspace_operator_snapshot }}'
```

### subspace_operator_chain_id

#### Default value

```YAML
subspace_operator_chain_id: mainnet
```

### subspace_operator_directories

#### Default value

```YAML
subspace_operator_directories:
  - path: '{{ subspace_operator_root_path }}'
  - path: '{{ subspace_operator_node_path }}'
  - path: '{{ subspace_operator_log_folder }}'
```

### subspace_operator_donwload_binary_enabled

#### Default value

```YAML
subspace_operator_donwload_binary_enabled: true
```

### subspace_operator_dsn_port

#### Default value

```YAML
subspace_operator_dsn_port: 30433
```

### subspace_operator_extra_package

#### Default value

```YAML
subspace_operator_extra_package:
  - logrotate
```

### subspace_operator_filesystem_disk_mounts

#### Default value

```YAML
subspace_operator_filesystem_disk_mounts:
  - disk: sdb
    path: '{{ subspace_operator_root_path }}'
    owner: '{{ subspace_operator_user }}'
    group: '{{ subspace_operator_group }}'
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
    vg: '{{ suspace_operator_custom_vg_name }}'
    size: 2g
    path: '{{ subspace_operator_log_folder }}'
    owner: '{{ subspace_operator_user }}'
    group: '{{ subspace_operator_group }}'
```

### subspace_operator_github_url

#### Default value

```YAML
subspace_operator_github_url: https://github.com/subspace/subspace/releases/download
```

### subspace_operator_group

#### Default value

```YAML
subspace_operator_group: subspace
```

### subspace_operator_log_file

#### Default value

```YAML
subspace_operator_log_file: operator.log
```

### subspace_operator_log_folder

#### Default value

```YAML
subspace_operator_log_folder: /var/log/subspace/subspace_operator
```

### subspace_operator_logrotate_file

#### Default value

```YAML
subspace_operator_logrotate_file: subspace
```

### subspace_operator_logrotate_folder

#### Default value

```YAML
subspace_operator_logrotate_folder: /etc/logrotate.d
```

### subspace_operator_node_path

#### Default value

```YAML
subspace_operator_node_path: '{{ subspace_operator_root_path }}/node'
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

### subspace_operator_root_path

#### Default value

```YAML
subspace_operator_root_path: /opt/subspace
```

### subspace_operator_snapshot

#### Default value

```YAML
subspace_operator_snapshot: '{{ subspace_operator_chain_id }}-2024-nov-13'
```

### subspace_operator_templates

#### Default value

```YAML
subspace_operator_templates:
  - src: subspace_operator.service.j2
    dest: /etc/systemd/system/subspace_operator.service
    mode: '0640'
  - src: subspace_operator.j2
    dest: '{{ subspace_operator_logrotate_folder }}/{{ subspace_operator_logrotate_file
      }}'
```

### subspace_operator_user

#### Default value

```YAML
subspace_operator_user: subspace
```

### suspace_operator_custom_vg_name

#### Default value

```YAML
suspace_operator_custom_vg_name: olympus
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
