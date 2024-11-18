# subspace_cache

this role simply install & configure subspace cache

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [subspace_cache_binary](#subspace_cache_binary)
  - [subspace_cache_binary_name](#subspace_cache_binary_name)
  - [subspace_cache_binary_path](#subspace_cache_binary_path)
  - [subspace_cache_binary_url](#subspace_cache_binary_url)
  - [subspace_cache_chain_id](#subspace_cache_chain_id)
  - [subspace_cache_directories](#subspace_cache_directories)
  - [subspace_cache_directory](#subspace_cache_directory)
  - [subspace_cache_disk_to_use](#subspace_cache_disk_to_use)
  - [subspace_cache_extra_package](#subspace_cache_extra_package)
  - [subspace_cache_filesystem_disk_mounts](#subspace_cache_filesystem_disk_mounts)
  - [subspace_cache_filesystem_enabled](#subspace_cache_filesystem_enabled)
  - [subspace_cache_filesystem_lvs_mounts](#subspace_cache_filesystem_lvs_mounts)
  - [subspace_cache_github_url](#subspace_cache_github_url)
  - [subspace_cache_group](#subspace_cache_group)
  - [subspace_cache_log_file](#subspace_cache_log_file)
  - [subspace_cache_log_folder](#subspace_cache_log_folder)
  - [subspace_cache_logrotate_file](#subspace_cache_logrotate_file)
  - [subspace_cache_logrotate_folder](#subspace_cache_logrotate_folder)
  - [subspace_cache_nats_ip](#subspace_cache_nats_ip)
  - [subspace_cache_node_rpc_url](#subspace_cache_node_rpc_url)
  - [subspace_cache_release_date](#subspace_cache_release_date)
  - [subspace_cache_size](#subspace_cache_size)
  - [subspace_cache_snapshot](#subspace_cache_snapshot)
  - [subspace_cache_templates](#subspace_cache_templates)
  - [subspace_cache_user](#subspace_cache_user)
  - [suspace_custom_vg_name](#suspace_custom_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### subspace_cache_binary

#### Default value

```YAML
subspace_cache_binary: ubuntu-x86_64-skylake
```

### subspace_cache_binary_name

#### Default value

```YAML
subspace_cache_binary_name: subspace_cache
```

### subspace_cache_binary_path

#### Default value

```YAML
subspace_cache_binary_path: /usr/bin/{{ subspace_cache_binary_name }}
```

### subspace_cache_binary_url

#### Default value

```YAML
subspace_cache_binary_url: '{{ subspace_cache_github_url }}/{{ subspace_cache_snapshot
  }}/subspace-farmer-{{ subspace_cache_binary }}-{{ subspace_cache_snapshot }}'
```

### subspace_cache_chain_id

#### Default value

```YAML
subspace_cache_chain_id: mainnet
```

### subspace_cache_directories

#### Default value

```YAML
subspace_cache_directories:
  - path: '{{ subspace_cache_directory }}'
  - path: '{{ subspace_cache_log_folder }}'
```

### subspace_cache_directory

#### Default value

```YAML
subspace_cache_directory: /opt/subspace_cache
```

### subspace_cache_disk_to_use

#### Default value

```YAML
subspace_cache_disk_to_use: sdc
```

### subspace_cache_extra_package

#### Default value

```YAML
subspace_cache_extra_package:
  - logrotate
```

### subspace_cache_filesystem_disk_mounts

#### Default value

```YAML
subspace_cache_filesystem_disk_mounts:
  - disk: '{{ subspace_cache_disk_to_use }}'
    path: '{{ subspace_cache_directory }}'
    owner: '{{ subspace_cache_user }}'
    group: '{{ subspace_cache_group }}'
```

### subspace_cache_filesystem_enabled

#### Default value

```YAML
subspace_cache_filesystem_enabled: true
```

### subspace_cache_filesystem_lvs_mounts

#### Default value

```YAML
subspace_cache_filesystem_lvs_mounts:
  - lv: lv_subspace_cache_log
    vg: '{{ suspace_custom_vg_name }}'
    size: 2g
    path: '{{ subspace_cache_log_folder }}'
    owner: '{{ subspace_cache_user }}'
    group: '{{ subspace_cache_group }}'
```

### subspace_cache_github_url

#### Default value

```YAML
subspace_cache_github_url: https://github.com/subspace/subspace/releases/download
```

### subspace_cache_group

#### Default value

```YAML
subspace_cache_group: subspace_cache
```

### subspace_cache_log_file

#### Default value

```YAML
subspace_cache_log_file: cache.log
```

### subspace_cache_log_folder

#### Default value

```YAML
subspace_cache_log_folder: /var/log/subspace_cache
```

### subspace_cache_logrotate_file

#### Default value

```YAML
subspace_cache_logrotate_file: subspace_cache
```

### subspace_cache_logrotate_folder

#### Default value

```YAML
subspace_cache_logrotate_folder: /etc/logrotate.d
```

### subspace_cache_nats_ip

#### Default value

```YAML
subspace_cache_nats_ip: nats://127.0.0.1:4222
```

### subspace_cache_node_rpc_url

#### Default value

```YAML
subspace_cache_node_rpc_url: ws://127.0.0.1:9944
```

### subspace_cache_release_date

#### Default value

```YAML
subspace_cache_release_date: 2024-nov-18
```

### subspace_cache_size

#### Default value

```YAML
subspace_cache_size: 200G
```

### subspace_cache_snapshot

#### Default value

```YAML
subspace_cache_snapshot: '{{ subspace_cache_chain_id }}-{{ subspace_cache_release_date
  }}'
```

### subspace_cache_templates

#### Default value

```YAML
subspace_cache_templates:
  - src: subspace_cache.service.j2
    dest: /etc/systemd/system/subspace_cache.service
    mode: '0640'
  - src: subspace_cache.j2
    dest: '{{ subspace_cache_logrotate_folder }}/{{ subspace_cache_logrotate_file
      }}'
  - src: filebeat/subspace_cache.yml.j2
    dest: /etc/filebeat/inputs.d/subspace_cache.yml
    owner: root
    group: root
```

### subspace_cache_user

#### Default value

```YAML
subspace_cache_user: subspace_cache
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
