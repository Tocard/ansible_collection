# ternoa

this role simply install & configure ternoa node

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [ternoa_custom_become_method](#ternoa_custom_become_method)
  - [ternoa_donwload_binary](#ternoa_donwload_binary)
  - [ternoa_extra_package](#ternoa_extra_package)
  - [ternoa_github_url](#ternoa_github_url)
  - [ternoa_group](#ternoa_group)
  - [ternoa_logrotate_folder](#ternoa_logrotate_folder)
  - [ternoa_lv_log_name](#ternoa_lv_log_name)
  - [ternoa_lv_log_size](#ternoa_lv_log_size)
  - [ternoa_lv_node_name](#ternoa_lv_node_name)
  - [ternoa_lv_node_size](#ternoa_lv_node_size)
  - [ternoa_node_binary_name](#ternoa_node_binary_name)
  - [ternoa_node_binary_path](#ternoa_node_binary_path)
  - [ternoa_node_binary_url](#ternoa_node_binary_url)
  - [ternoa_node_chain](#ternoa_node_chain)
  - [ternoa_node_directories](#ternoa_node_directories)
  - [ternoa_node_filesystem_enabled](#ternoa_node_filesystem_enabled)
  - [ternoa_node_filesystem_lvs_mounts](#ternoa_node_filesystem_lvs_mounts)
  - [ternoa_node_install_enabled](#ternoa_node_install_enabled)
  - [ternoa_node_install_path](#ternoa_node_install_path)
  - [ternoa_node_log_file](#ternoa_node_log_file)
  - [ternoa_node_log_folder](#ternoa_node_log_folder)
  - [ternoa_node_logrotate_file](#ternoa_node_logrotate_file)
  - [ternoa_node_name](#ternoa_node_name)
  - [ternoa_node_templates](#ternoa_node_templates)
  - [ternoa_prometheus_enabled](#ternoa_prometheus_enabled)
  - [ternoa_prometheus_port](#ternoa_prometheus_port)
  - [ternoa_user](#ternoa_user)
  - [ternoa_version](#ternoa_version)
  - [ternoa_vg_name](#ternoa_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### ternoa_custom_become_method

#### Default value

```YAML
ternoa_custom_become_method: sudo
```

### ternoa_donwload_binary

#### Default value

```YAML
ternoa_donwload_binary: true
```

### ternoa_extra_package

#### Default value

```YAML
ternoa_extra_package:
  - logrotate
```

### ternoa_github_url

#### Default value

```YAML
ternoa_github_url: https://github.com/capsule-corp-ternoa/ternoa-node/releases/download
```

### ternoa_group

#### Default value

```YAML
ternoa_group: chimera
```

### ternoa_logrotate_folder

#### Default value

```YAML
ternoa_logrotate_folder: /etc/logrotate.d
```

### ternoa_lv_log_name

#### Default value

```YAML
ternoa_lv_log_name: lv_ternoa_node_log
```

### ternoa_lv_log_size

#### Default value

```YAML
ternoa_lv_log_size: 1g
```

### ternoa_lv_node_name

#### Default value

```YAML
ternoa_lv_node_name: lv_ternoa_node
```

### ternoa_lv_node_size

#### Default value

```YAML
ternoa_lv_node_size: 10g
```

### ternoa_node_binary_name

#### Default value

```YAML
ternoa_node_binary_name: ternoa_node
```

### ternoa_node_binary_path

#### Default value

```YAML
ternoa_node_binary_path: /usr/bin/{{ ternoa_node_binary_name }}
```

### ternoa_node_binary_url

#### Default value

```YAML
ternoa_node_binary_url: '{{ ternoa_github_url }}/v{{ ternoa_version }}/ternoa'
```

### ternoa_node_chain

#### Default value

```YAML
ternoa_node_chain: mainnet
```

### ternoa_node_directories

#### Default value

```YAML
ternoa_node_directories:
  - path: '{{ ternoa_node_install_path }}'
  - path: '{{ ternoa_node_log_folder }}'
```

### ternoa_node_filesystem_enabled

#### Default value

```YAML
ternoa_node_filesystem_enabled: true
```

### ternoa_node_filesystem_lvs_mounts

#### Default value

```YAML
ternoa_node_filesystem_lvs_mounts:
  - lv: '{{ ternoa_lv_node_name }}'
    vg: '{{ ternoa_vg_name }}'
    size: '{{ ternoa_lv_node_size }}'
    path: '{{ ternoa_node_install_path }}'
    owner: '{{ ternoa_user }}'
    group: '{{ ternoa_group }}'
  - lv: '{{ ternoa_lv_log_name }}'
    vg: '{{ ternoa_vg_name }}'
    size: '{{ ternoa_lv_log_size }}'
    path: '{{ ternoa_node_log_folder }}'
    owner: '{{ ternoa_user }}'
    group: '{{ ternoa_group }}'
```

### ternoa_node_install_enabled

#### Default value

```YAML
ternoa_node_install_enabled: true
```

### ternoa_node_install_path

#### Default value

```YAML
ternoa_node_install_path: /opt/chimera/ternoa
```

### ternoa_node_log_file

#### Default value

```YAML
ternoa_node_log_file: node.log
```

### ternoa_node_log_folder

#### Default value

```YAML
ternoa_node_log_folder: /var/log/chimera/ternoa_node
```

### ternoa_node_logrotate_file

#### Default value

```YAML
ternoa_node_logrotate_file: ternoa_node
```

### ternoa_node_name

#### Default value

```YAML
ternoa_node_name: '{{ ansible_hostname }}'
```

### ternoa_node_templates

#### Default value

```YAML
ternoa_node_templates:
  - src: ternoa_node.service.j2
    dest: /etc/systemd/system/ternoa_node.service
    mode: '0640'
  - src: ternoa_node.j2
    dest: '{{ ternoa_logrotate_folder }}/{{ ternoa_node_logrotate_file }}'
```

### ternoa_prometheus_enabled

#### Default value

```YAML
ternoa_prometheus_enabled: true
```

### ternoa_prometheus_port

#### Default value

```YAML
ternoa_prometheus_port: 9615
```

### ternoa_user

#### Default value

```YAML
ternoa_user: chimera
```

### ternoa_version

#### Default value

```YAML
ternoa_version: 1.3.2
```

### ternoa_vg_name

#### Default value

```YAML
ternoa_vg_name: olympus
```



## Dependencies


## License

BSD-3-Clause

## Author

Douceur
