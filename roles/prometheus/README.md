# prometheus

this role simply install & configure prometheus

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [prometheus_binary_path](#prometheus_binary_path)
  - [prometheus_config_directory](#prometheus_config_directory)
  - [prometheus_config_path](#prometheus_config_path)
  - [prometheus_custom_become_method](#prometheus_custom_become_method)
  - [prometheus_deb](#prometheus_deb)
  - [prometheus_directories](#prometheus_directories)
  - [prometheus_filesystem_enabled](#prometheus_filesystem_enabled)
  - [prometheus_filesystem_list](#prometheus_filesystem_list)
  - [prometheus_filesystem_log_size](#prometheus_filesystem_log_size)
  - [prometheus_filesystem_storage_size](#prometheus_filesystem_storage_size)
  - [prometheus_github_url](#prometheus_github_url)
  - [prometheus_gpg_key](#prometheus_gpg_key)
  - [prometheus_group](#prometheus_group)
  - [prometheus_listen_address](#prometheus_listen_address)
  - [prometheus_log_directory](#prometheus_log_directory)
  - [prometheus_log_filename](#prometheus_log_filename)
  - [prometheus_log_service_filename](#prometheus_log_service_filename)
  - [prometheus_owner](#prometheus_owner)
  - [prometheus_storage_directory](#prometheus_storage_directory)
  - [prometheus_templates](#prometheus_templates)
  - [prometheus_version](#prometheus_version)
  - [prometheus_virtual_group_name](#prometheus_virtual_group_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### prometheus_binary_path

#### Default value

```YAML
prometheus_binary_path: /usr/bin/prometheus
```

### prometheus_config_directory

#### Default value

```YAML
prometheus_config_directory: /etc/prometheus
```

### prometheus_config_path

#### Default value

```YAML
prometheus_config_path: '{{ prometheus_config_directory }}/prometheus.yml'
```

### prometheus_custom_become_method

#### Default value

```YAML
prometheus_custom_become_method: sudo
```

### prometheus_deb

#### Default value

```YAML
prometheus_deb:
  - https://packages.prometheus.com/oss/deb stable main
  - https://packages.prometheus.com/enterprise/deb stable main
```

### prometheus_directories

#### Default value

```YAML
prometheus_directories:
  - path: '{{ prometheus_config_directory }}'
  - path: '{{ prometheus_storage_directory }}'
  - path: '{{ prometheus_log_directory }}'
```

### prometheus_filesystem_enabled

#### Default value

```YAML
prometheus_filesystem_enabled: false
```

### prometheus_filesystem_list

#### Default value

```YAML
prometheus_filesystem_list:
  - lv: lv_prometheus_storage
    vg: '{{ prometheus_virtual_group_name }}'
    size: '{{ prometheus_filesystem_storage_size }}'
    path: '{{ prometheus_storage_directory }}'
    owner: '{{ prometheus_owner }}'
    group: '{{ prometheus_group }}'
  - lv: lv_prometheus_log
    vg: '{{ prometheus_virtual_group_name }}'
    size: '{{ prometheus_filesystem_log_size}}'
    path: '{{ prometheus_log_directory }}'
    owner: '{{ prometheus_owner }}'
    group: '{{ prometheus_group }}'
```

### prometheus_filesystem_log_size

#### Default value

```YAML
prometheus_filesystem_log_size: 2G
```

### prometheus_filesystem_storage_size

#### Default value

```YAML
prometheus_filesystem_storage_size: 10g
```

### prometheus_github_url

#### Default value

```YAML
prometheus_github_url: https://github.com/prometheus/prometheus/releases/download/v{{
  prometheus_version}}/prometheus-{{ prometheus_version }}.linux-amd64.tar.gz
```

### prometheus_gpg_key

#### Default value

```YAML
prometheus_gpg_key:
  - https://packages.prometheus.com/gpg.key
```

### prometheus_group

#### Default value

```YAML
prometheus_group: prometheus
```

### prometheus_listen_address

#### Default value

```YAML
prometheus_listen_address: :8090
```

### prometheus_log_directory

#### Default value

```YAML
prometheus_log_directory: /var/log/prometheus
```

### prometheus_log_filename

#### Default value

```YAML
prometheus_log_filename: prometheus.log
```

### prometheus_log_service_filename

#### Default value

```YAML
prometheus_log_service_filename: prometheus_service.log
```

### prometheus_owner

#### Default value

```YAML
prometheus_owner: prometheus
```

### prometheus_storage_directory

#### Default value

```YAML
prometheus_storage_directory: /var/lib/prometheus
```

### prometheus_templates

#### Default value

```YAML
prometheus_templates:
  - src: prometheus.yml.j2
    dest: '{{ prometheus_config_path }}'
  - src: prometheus.services.j2
    dest: '{{ prometheus_config_directory }}/prometheus.service'
```

### prometheus_version

#### Default value

```YAML
prometheus_version: 2.49.1
```

### prometheus_virtual_group_name

#### Default value

```YAML
prometheus_virtual_group_name:
```



## Dependencies


## License

BSD-3-Clause

## Author

Douceur
