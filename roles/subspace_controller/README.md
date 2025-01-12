# subspace_controller

this role simply install & configure subspace controller

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [subspace_controller_binary](#subspace_controller_binary)
  - [subspace_controller_binary_name](#subspace_controller_binary_name)
  - [subspace_controller_binary_path](#subspace_controller_binary_path)
  - [subspace_controller_binary_url](#subspace_controller_binary_url)
  - [subspace_controller_chain_id](#subspace_controller_chain_id)
  - [subspace_controller_directories](#subspace_controller_directories)
  - [subspace_controller_extra_package](#subspace_controller_extra_package)
  - [subspace_controller_filesystem_enabled](#subspace_controller_filesystem_enabled)
  - [subspace_controller_filesystem_lvs_mounts](#subspace_controller_filesystem_lvs_mounts)
  - [subspace_controller_github_url](#subspace_controller_github_url)
  - [subspace_controller_group](#subspace_controller_group)
  - [subspace_controller_install_path](#subspace_controller_install_path)
  - [subspace_controller_log_file](#subspace_controller_log_file)
  - [subspace_controller_log_folder](#subspace_controller_log_folder)
  - [subspace_controller_logrotate_file](#subspace_controller_logrotate_file)
  - [subspace_controller_logrotate_folder](#subspace_controller_logrotate_folder)
  - [subspace_controller_nats_ip](#subspace_controller_nats_ip)
  - [subspace_controller_node_rpc_url](#subspace_controller_node_rpc_url)
  - [subspace_controller_release_date](#subspace_controller_release_date)
  - [subspace_controller_snapshot](#subspace_controller_snapshot)
  - [subspace_controller_templates](#subspace_controller_templates)
  - [subspace_controller_user](#subspace_controller_user)
  - [suspace_custom_vg_name](#suspace_custom_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### subspace_controller_binary

#### Default value

```YAML
subspace_controller_binary: ubuntu-x86_64-skylake
```

### subspace_controller_binary_name

#### Default value

```YAML
subspace_controller_binary_name: subspace_controller
```

### subspace_controller_binary_path

#### Default value

```YAML
subspace_controller_binary_path: /usr/bin/{{ subspace_controller_binary_name }}
```

### subspace_controller_binary_url

#### Default value

```YAML
subspace_controller_binary_url: '{{ subspace_controller_github_url }}/{{ subspace_controller_snapshot
  }}/subspace-farmer-{{ subspace_controller_binary }}-{{ subspace_controller_snapshot
  }}'
```

### subspace_controller_chain_id

#### Default value

```YAML
subspace_controller_chain_id: mainnet
```

### subspace_controller_directories

#### Default value

```YAML
subspace_controller_directories:
  - path: '{{ subspace_controller_install_path }}'
  - path: '{{ subspace_controller_log_folder }}'
```

### subspace_controller_extra_package

#### Default value

```YAML
subspace_controller_extra_package:
  - logrotate
```

### subspace_controller_filesystem_enabled

#### Default value

```YAML
subspace_controller_filesystem_enabled: true
```

### subspace_controller_filesystem_lvs_mounts

#### Default value

```YAML
subspace_controller_filesystem_lvs_mounts:
  - lv: lv_subspace_controller_log
    vg: '{{ suspace_custom_vg_name }}'
    size: 2g
    path: '{{ subspace_controller_log_folder }}'
    owner: '{{ subspace_controller_user }}'
    group: '{{ subspace_controller_group }}'
```

### subspace_controller_github_url

#### Default value

```YAML
subspace_controller_github_url: https://github.com/subspace/subspace/releases/download
```

### subspace_controller_group

#### Default value

```YAML
subspace_controller_group: subspace_controller
```

### subspace_controller_install_path

#### Default value

```YAML
subspace_controller_install_path: /opt/subspace_controller
```

### subspace_controller_log_file

#### Default value

```YAML
subspace_controller_log_file: controller.log
```

### subspace_controller_log_folder

#### Default value

```YAML
subspace_controller_log_folder: /var/log/subspace_controller
```

### subspace_controller_logrotate_file

#### Default value

```YAML
subspace_controller_logrotate_file: subspace_controller
```

### subspace_controller_logrotate_folder

#### Default value

```YAML
subspace_controller_logrotate_folder: /etc/logrotate.d
```

### subspace_controller_nats_ip

#### Default value

```YAML
subspace_controller_nats_ip: nats://127.0.0.1:4222
```

### subspace_controller_node_rpc_url

#### Default value

```YAML
subspace_controller_node_rpc_url: ws://127.0.0.1:9944
```

### subspace_controller_release_date

#### Default value

```YAML
subspace_controller_release_date: 2025-jan-03
```

### subspace_controller_snapshot

#### Default value

```YAML
subspace_controller_snapshot: '{{ subspace_controller_chain_id }}-{{ subspace_controller_release_date
  }}'
```

### subspace_controller_templates

#### Default value

```YAML
subspace_controller_templates:
  - src: subspace_controller.service.j2
    dest: /etc/systemd/system/subspace_controller.service
    mode: '0640'
  - src: subspace_controller.j2
    dest: '{{ subspace_controller_logrotate_folder }}/{{ subspace_controller_logrotate_file
      }}'
  - src: filebeat/subspace_controller.yml.j2
    dest: /etc/filebeat/inputs.d/subspace_controller.yml
    owner: root
    group: root
```

### subspace_controller_user

#### Default value

```YAML
subspace_controller_user: subspace_controller
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
