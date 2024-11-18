# subspace_farmer

this role simply install & configure subspace farmer

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [subspace_farmer_binary](#subspace_farmer_binary)
  - [subspace_farmer_binary_name](#subspace_farmer_binary_name)
  - [subspace_farmer_binary_path](#subspace_farmer_binary_path)
  - [subspace_farmer_binary_url](#subspace_farmer_binary_url)
  - [subspace_farmer_chain_id](#subspace_farmer_chain_id)
  - [subspace_farmer_directories](#subspace_farmer_directories)
  - [subspace_farmer_disks](#subspace_farmer_disks)
  - [subspace_farmer_extra_package](#subspace_farmer_extra_package)
  - [subspace_farmer_filesystem_disk](#subspace_farmer_filesystem_disk)
  - [subspace_farmer_filesystem_enabled](#subspace_farmer_filesystem_enabled)
  - [subspace_farmer_filesystem_lvs_mounts](#subspace_farmer_filesystem_lvs_mounts)
  - [subspace_farmer_github_url](#subspace_farmer_github_url)
  - [subspace_farmer_group](#subspace_farmer_group)
  - [subspace_farmer_install_path](#subspace_farmer_install_path)
  - [subspace_farmer_log_file](#subspace_farmer_log_file)
  - [subspace_farmer_log_folder](#subspace_farmer_log_folder)
  - [subspace_farmer_logrotate_file](#subspace_farmer_logrotate_file)
  - [subspace_farmer_logrotate_folder](#subspace_farmer_logrotate_folder)
  - [subspace_farmer_nats_ip](#subspace_farmer_nats_ip)
  - [subspace_farmer_node_rpc_url](#subspace_farmer_node_rpc_url)
  - [subspace_farmer_release_date](#subspace_farmer_release_date)
  - [subspace_farmer_reward_adress](#subspace_farmer_reward_adress)
  - [subspace_farmer_snapshot](#subspace_farmer_snapshot)
  - [subspace_farmer_templates](#subspace_farmer_templates)
  - [subspace_farmer_user](#subspace_farmer_user)
  - [suspace_custom_vg_name](#suspace_custom_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### subspace_farmer_binary

#### Default value

```YAML
subspace_farmer_binary: ubuntu-x86_64-skylake
```

### subspace_farmer_binary_name

#### Default value

```YAML
subspace_farmer_binary_name: subspace_farmer
```

### subspace_farmer_binary_path

#### Default value

```YAML
subspace_farmer_binary_path: /usr/bin/{{ subspace_farmer_binary_name }}
```

### subspace_farmer_binary_url

#### Default value

```YAML
subspace_farmer_binary_url: '{{ subspace_farmer_github_url }}/{{ subspace_farmer_snapshot
  }}/subspace-farmer-{{ subspace_farmer_binary }}-{{ subspace_farmer_snapshot }}'
```

### subspace_farmer_chain_id

#### Default value

```YAML
subspace_farmer_chain_id: mainnet
```

### subspace_farmer_directories

#### Default value

```YAML
subspace_farmer_directories:
  - path: '{{ subspace_farmer_install_path }}'
  - path: '{{ subspace_farmer_log_folder }}'
```

### subspace_farmer_disks

#### Default value

```YAML
subspace_farmer_disks:
  - path: /random/path
    size: 1G
```

### subspace_farmer_extra_package

#### Default value

```YAML
subspace_farmer_extra_package:
  - logrotate
```

### subspace_farmer_filesystem_disk

#### Default value

```YAML
subspace_farmer_filesystem_disk: []
```

### subspace_farmer_filesystem_enabled

#### Default value

```YAML
subspace_farmer_filesystem_enabled: true
```

### subspace_farmer_filesystem_lvs_mounts

#### Default value

```YAML
subspace_farmer_filesystem_lvs_mounts:
  - lv: lv_subspace_farmer_log
    vg: '{{ suspace_custom_vg_name }}'
    size: 2g
    path: '{{ subspace_farmer_log_folder }}'
    owner: '{{ subspace_farmer_user }}'
    group: '{{ subspace_farmer_group }}'
```

### subspace_farmer_github_url

#### Default value

```YAML
subspace_farmer_github_url: https://github.com/subspace/subspace/releases/download
```

### subspace_farmer_group

#### Default value

```YAML
subspace_farmer_group: subspace_farmer
```

### subspace_farmer_install_path

#### Default value

```YAML
subspace_farmer_install_path: /opt/subspace_farmer
```

### subspace_farmer_log_file

#### Default value

```YAML
subspace_farmer_log_file: farmer.log
```

### subspace_farmer_log_folder

#### Default value

```YAML
subspace_farmer_log_folder: /var/log/subspace_farmer
```

### subspace_farmer_logrotate_file

#### Default value

```YAML
subspace_farmer_logrotate_file: subspace_farmer
```

### subspace_farmer_logrotate_folder

#### Default value

```YAML
subspace_farmer_logrotate_folder: /etc/logrotate.d
```

### subspace_farmer_nats_ip

#### Default value

```YAML
subspace_farmer_nats_ip: nats://127.0.0.1:4222
```

### subspace_farmer_node_rpc_url

#### Default value

```YAML
subspace_farmer_node_rpc_url: ws://127.0.0.1:9944
```

### subspace_farmer_release_date

#### Default value

```YAML
subspace_farmer_release_date: 2024-nov-18
```

### subspace_farmer_reward_adress

#### Default value

```YAML
subspace_farmer_reward_adress:
```

### subspace_farmer_snapshot

#### Default value

```YAML
subspace_farmer_snapshot: '{{ subspace_farmer_chain_id }}-{{ subspace_farmer_release_date
  }}'
```

### subspace_farmer_templates

#### Default value

```YAML
subspace_farmer_templates:
  - src: subspace_farmer.service.j2
    dest: /etc/systemd/system/subspace_farmer.service
    mode: '0640'
  - src: subspace_farmer.j2
    dest: '{{ subspace_farmer_logrotate_folder }}/{{ subspace_farmer_logrotate_file
      }}'
  - src: filebeat/subspace_farmer.yml.j2
    dest: /etc/filebeat/inputs.d/subspace_farmer.yml
    owner: root
    group: root
```

### subspace_farmer_user

#### Default value

```YAML
subspace_farmer_user: subspace_farmer
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
