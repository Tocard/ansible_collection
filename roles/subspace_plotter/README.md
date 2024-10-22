# subspace_plotter

this role simply install & configure subspace plotter

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [subspace_plotter_binary](#subspace_plotter_binary)
  - [subspace_plotter_binary_name](#subspace_plotter_binary_name)
  - [subspace_plotter_binary_path](#subspace_plotter_binary_path)
  - [subspace_plotter_binary_url](#subspace_plotter_binary_url)
  - [subspace_plotter_chain_id](#subspace_plotter_chain_id)
  - [subspace_plotter_directories](#subspace_plotter_directories)
  - [subspace_plotter_directory](#subspace_plotter_directory)
  - [subspace_plotter_extra_package](#subspace_plotter_extra_package)
  - [subspace_plotter_filesystem_enabled](#subspace_plotter_filesystem_enabled)
  - [subspace_plotter_filesystem_lvs_mounts](#subspace_plotter_filesystem_lvs_mounts)
  - [subspace_plotter_github_url](#subspace_plotter_github_url)
  - [subspace_plotter_group](#subspace_plotter_group)
  - [subspace_plotter_log_file](#subspace_plotter_log_file)
  - [subspace_plotter_log_folder](#subspace_plotter_log_folder)
  - [subspace_plotter_logrotate_file](#subspace_plotter_logrotate_file)
  - [subspace_plotter_logrotate_folder](#subspace_plotter_logrotate_folder)
  - [subspace_plotter_nats_ip](#subspace_plotter_nats_ip)
  - [subspace_plotter_node_rpc_url](#subspace_plotter_node_rpc_url)
  - [subspace_plotter_release_date](#subspace_plotter_release_date)
  - [subspace_plotter_snapshot](#subspace_plotter_snapshot)
  - [subspace_plotter_templates](#subspace_plotter_templates)
  - [subspace_plotter_user](#subspace_plotter_user)
  - [suspace_custom_vg_name](#suspace_custom_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### subspace_plotter_binary

#### Default value

```YAML
subspace_plotter_binary: ubuntu-x86_64-skylake
```

### subspace_plotter_binary_name

#### Default value

```YAML
subspace_plotter_binary_name: subspace_plotter
```

### subspace_plotter_binary_path

#### Default value

```YAML
subspace_plotter_binary_path: /usr/bin/{{ subspace_plotter_binary_name }}
```

### subspace_plotter_binary_url

#### Default value

```YAML
subspace_plotter_binary_url: '{{ subspace_plotter_github_url }}/{{ subspace_plotter_snapshot
  }}/subspace-farmer-{{ subspace_plotter_binary }}-{{ subspace_plotter_snapshot }}'
```

### subspace_plotter_chain_id

#### Default value

```YAML
subspace_plotter_chain_id: gemini-3h
```

### subspace_plotter_directories

#### Default value

```YAML
subspace_plotter_directories:
  - path: '{{ subspace_plotter_directory }}'
  - path: '{{ subspace_plotter_log_folder }}'
```

### subspace_plotter_directory

#### Default value

```YAML
subspace_plotter_directory: /opt/subspace_plotter
```

### subspace_plotter_extra_package

#### Default value

```YAML
subspace_plotter_extra_package:
  - logrotate
```

### subspace_plotter_filesystem_enabled

#### Default value

```YAML
subspace_plotter_filesystem_enabled: true
```

### subspace_plotter_filesystem_lvs_mounts

#### Default value

```YAML
subspace_plotter_filesystem_lvs_mounts:
  - lv: lv_subspace_plotter_log
    vg: '{{ suspace_custom_vg_name }}'
    size: 2g
    path: '{{ subspace_plotter_log_folder }}'
    owner: '{{ subspace_plotter_user }}'
    group: '{{ subspace_plotter_group }}'
```

### subspace_plotter_github_url

#### Default value

```YAML
subspace_plotter_github_url: https://github.com/subspace/subspace/releases/download
```

### subspace_plotter_group

#### Default value

```YAML
subspace_plotter_group: subspace_plotter
```

### subspace_plotter_log_file

#### Default value

```YAML
subspace_plotter_log_file: plotter.log
```

### subspace_plotter_log_folder

#### Default value

```YAML
subspace_plotter_log_folder: /var/log/subspace_plotter
```

### subspace_plotter_logrotate_file

#### Default value

```YAML
subspace_plotter_logrotate_file: subspace_plotter
```

### subspace_plotter_logrotate_folder

#### Default value

```YAML
subspace_plotter_logrotate_folder: /etc/logrotate.d
```

### subspace_plotter_nats_ip

#### Default value

```YAML
subspace_plotter_nats_ip: nats://127.0.0.1:4222
```

### subspace_plotter_node_rpc_url

#### Default value

```YAML
subspace_plotter_node_rpc_url: ws://127.0.0.1:9944
```

### subspace_plotter_release_date

#### Default value

```YAML
subspace_plotter_release_date: 2024-oct-10
```

### subspace_plotter_snapshot

#### Default value

```YAML
subspace_plotter_snapshot: '{{ subspace_plotter_chain_id }}-{{ subspace_plotter_release_date
  }}'
```

### subspace_plotter_templates

#### Default value

```YAML
subspace_plotter_templates:
  - src: subspace_plotter.service.j2
    dest: /etc/systemd/system/subspace_plotter.service
    mode: '0640'
  - src: subspace_plotter.j2
    dest: '{{ subspace_plotter_logrotate_folder }}/{{ subspace_plotter_logrotate_file
      }}'
  - src: filebeat/subspace_plotter.yml.j2
    dest: /etc/filebeat/inputs.d/subspace_plotter.yml
    owner: root
    group: root
```

### subspace_plotter_user

#### Default value

```YAML
subspace_plotter_user: subspace_plotter
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
