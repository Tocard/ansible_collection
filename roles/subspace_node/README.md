# subspace_node

this role simply install & configure subspace node & farmer

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [subspace_node_binary](#subspace_node_binary)
  - [subspace_node_binary_name](#subspace_node_binary_name)
  - [subspace_node_binary_path](#subspace_node_binary_path)
  - [subspace_node_binary_url](#subspace_node_binary_url)
  - [subspace_node_chain_id](#subspace_node_chain_id)
  - [subspace_node_directories](#subspace_node_directories)
  - [subspace_node_donwload_binary](#subspace_node_donwload_binary)
  - [subspace_node_dsn_port](#subspace_node_dsn_port)
  - [subspace_node_extra_package](#subspace_node_extra_package)
  - [subspace_node_filesystem_disk_mounts](#subspace_node_filesystem_disk_mounts)
  - [subspace_node_filesystem_enabled](#subspace_node_filesystem_enabled)
  - [subspace_node_filesystem_lvs_mounts](#subspace_node_filesystem_lvs_mounts)
  - [subspace_node_github_url](#subspace_node_github_url)
  - [subspace_node_group](#subspace_node_group)
  - [subspace_node_install_path](#subspace_node_install_path)
  - [subspace_node_log_file](#subspace_node_log_file)
  - [subspace_node_log_folder](#subspace_node_log_folder)
  - [subspace_node_logrotate_file](#subspace_node_logrotate_file)
  - [subspace_node_logrotate_folder](#subspace_node_logrotate_folder)
  - [subspace_node_p2p_port](#subspace_node_p2p_port)
  - [subspace_node_prometheus_port](#subspace_node_prometheus_port)
  - [subspace_node_snapshot](#subspace_node_snapshot)
  - [subspace_node_templates](#subspace_node_templates)
  - [subspace_node_user](#subspace_node_user)
  - [suspace_custom_vg_name](#suspace_custom_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### subspace_node_binary

#### Default value

```YAML
subspace_node_binary: ubuntu-x86_64-skylake
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
subspace_node_binary_url: '{{ subspace_node_github_url }}/{{ subspace_node_snapshot
  }}/subspace-node-{{ subspace_node_binary }}-{{ subspace_node_snapshot }}'
```

### subspace_node_chain_id

#### Default value

```YAML
subspace_node_chain_id: mainnet
```

### subspace_node_directories

#### Default value

```YAML
subspace_node_directories:
  - path: '{{ subspace_node_install_path }}'
  - path: '{{ subspace_node_log_folder }}'
```

### subspace_node_donwload_binary

#### Default value

```YAML
subspace_node_donwload_binary: true
```

### subspace_node_dsn_port

#### Default value

```YAML
subspace_node_dsn_port: 30433
```

### subspace_node_extra_package

#### Default value

```YAML
subspace_node_extra_package:
  - logrotate
```

### subspace_node_filesystem_disk_mounts

#### Default value

```YAML
subspace_node_filesystem_disk_mounts:
  - disk: sdb
    path: '{{ subspace_node_install_path }}'
    owner: '{{ subspace_node_user }}'
    group: '{{ subspace_node_group }}'
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
    owner: '{{ subspace_node_user }}'
    group: '{{ subspace_node_group }}'
```

### subspace_node_github_url

#### Default value

```YAML
subspace_node_github_url: https://github.com/subspace/subspace/releases/download
```

### subspace_node_group

#### Default value

```YAML
subspace_node_group: subspace_node
```

### subspace_node_install_path

#### Default value

```YAML
subspace_node_install_path: /opt/subspace_node
```

### subspace_node_log_file

#### Default value

```YAML
subspace_node_log_file: node.log
```

### subspace_node_log_folder

#### Default value

```YAML
subspace_node_log_folder: /var/log/subspace_node
```

### subspace_node_logrotate_file

#### Default value

```YAML
subspace_node_logrotate_file: subspace_node
```

### subspace_node_logrotate_folder

#### Default value

```YAML
subspace_node_logrotate_folder: /etc/logrotate.d
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

### subspace_node_snapshot

#### Default value

```YAML
subspace_node_snapshot: '{{ subspace_node_chain_id }}-2024-nov-06'
```

### subspace_node_templates

#### Default value

```YAML
subspace_node_templates:
  - src: subspace_node.service.j2
    dest: /etc/systemd/system/subspace_node.service
    mode: '0640'
  - src: subspace_node.j2
    dest: '{{ subspace_node_logrotate_folder }}/{{ subspace_node_logrotate_file }}'
  - src: filebeat/subspace_node.yml.j2
    dest: /etc/filebeat/inputs.d/subspace_node.yml
    owner: root
    group: root
```

### subspace_node_user

#### Default value

```YAML
subspace_node_user: subspace_node
```

### suspace_custom_vg_name

#### Default value

```YAML
suspace_custom_vg_name: olympus
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
