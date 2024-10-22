# nats

this role configure nexus

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [nats_bin_path](#nats_bin_path)
  - [nats_config_directory](#nats_config_directory)
  - [nats_data_directory](#nats_data_directory)
  - [nats_directories](#nats_directories)
  - [nats_download_url](#nats_download_url)
  - [nats_group](#nats_group)
  - [nats_groups](#nats_groups)
  - [nats_http_port](#nats_http_port)
  - [nats_log_directory](#nats_log_directory)
  - [nats_log_file](#nats_log_file)
  - [nats_password](#nats_password)
  - [nats_payload_mb_size](#nats_payload_mb_size)
  - [nats_port](#nats_port)
  - [nats_service_name](#nats_service_name)
  - [nats_temp_folder](#nats_temp_folder)
  - [nats_templates](#nats_templates)
  - [nats_user](#nats_user)
  - [nats_version](#nats_version)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### nats_bin_path

#### Default value

```YAML
nats_bin_path: /usr/local/bin/nats-server
```

### nats_config_directory

#### Default value

```YAML
nats_config_directory: /etc/nats
```

### nats_data_directory

#### Default value

```YAML
nats_data_directory: /var/lib/nats
```

### nats_directories

#### Default value

```YAML
nats_directories:
  - '{{ nats_config_directory  }}'
  - '{{ nats_data_directory }}'
  - '{{ nats_log_directory }}'
  - '{{ nats_temp_folder }}'
```

### nats_download_url

#### Default value

```YAML
nats_download_url: https://github.com/nats-io/nats-server/releases/download/{{ nats_version
  }}/nats-server-{{ nats_version }}-linux-amd64.tar.gz
```

### nats_group

#### Default value

```YAML
nats_group: nats
```

### nats_groups

#### Default value

```YAML
nats_groups: []
```

### nats_http_port

#### Default value

```YAML
nats_http_port: 8222
```

### nats_log_directory

#### Default value

```YAML
nats_log_directory: /var/log/nats
```

### nats_log_file

#### Default value

```YAML
nats_log_file: nats.log
```

### nats_password

#### Default value

```YAML
nats_password:
```

### nats_payload_mb_size

#### Default value

```YAML
nats_payload_mb_size: 2MB
```

### nats_port

#### Default value

```YAML
nats_port: 4222
```

### nats_service_name

#### Default value

```YAML
nats_service_name: nats
```

### nats_temp_folder

#### Default value

```YAML
nats_temp_folder: /opt/nats
```

### nats_templates

#### Default value

```YAML
nats_templates:
  - src: nats.conf.j2
    dest: '{{ nats_config_directory }}/nats.conf'
  - src: nats.service.j2
    dest: /etc/systemd/system/{{ nats_service_name }}.service
    mode: '0644'
```

### nats_user

#### Default value

```YAML
nats_user: nats
```

### nats_version

#### Default value

```YAML
nats_version: v2.10.17
```



## Dependencies

- tocard.utils.user

## License

BSD-3-Clause

## Author

Douceur
