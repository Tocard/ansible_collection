# nexus

this role configure nexus

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [nexus_binary_path](#nexus_binary_path)
  - [nexus_blob_path](#nexus_blob_path)
  - [nexus_custom_become_method](#nexus_custom_become_method)
  - [nexus_directories](#nexus_directories)
  - [nexus_download_url](#nexus_download_url)
  - [nexus_filesystem_disk_mounts](#nexus_filesystem_disk_mounts)
  - [nexus_filesystem_lvs_mounts](#nexus_filesystem_lvs_mounts)
  - [nexus_filesystem_vgs_to_create](#nexus_filesystem_vgs_to_create)
  - [nexus_group](#nexus_group)
  - [nexus_groups](#nexus_groups)
  - [nexus_home](#nexus_home)
  - [nexus_java_version](#nexus_java_version)
  - [nexus_log_lv_name](#nexus_log_lv_name)
  - [nexus_log_path](#nexus_log_path)
  - [nexus_log_size](#nexus_log_size)
  - [nexus_lv_name](#nexus_lv_name)
  - [nexus_lv_size](#nexus_lv_size)
  - [nexus_package](#nexus_package)
  - [nexus_run_home](#nexus_run_home)
  - [nexus_ssl_enabled](#nexus_ssl_enabled)
  - [nexus_ssl_file](#nexus_ssl_file)
  - [nexus_ssl_path](#nexus_ssl_path)
  - [nexus_templates](#nexus_templates)
  - [nexus_user](#nexus_user)
  - [nexus_version](#nexus_version)
  - [nexus_vg_name](#nexus_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### nexus_binary_path

#### Default value

```YAML
nexus_binary_path: '{{ nexus_run_home }}/bin/nexus'
```

### nexus_blob_path

#### Default value

```YAML
nexus_blob_path: '{{ nexus_home }}/sonatype-work/nexus3/blobs'
```

### nexus_custom_become_method

#### Default value

```YAML
nexus_custom_become_method: sudo
```

### nexus_directories

#### Default value

```YAML
nexus_directories:
  - path: '{{ nexus_home }}'
  - path: '{{ nexus_ssl_path }}'
  - path: '{{ nexus_log_path }}'
```

### nexus_download_url

#### Default value

```YAML
nexus_download_url: https://download.sonatype.com/nexus/3/nexus-{{ nexus_version }}-java{{
  nexus_java_version }}-unix.tar.gz
```

### nexus_filesystem_disk_mounts

#### Default value

```YAML
nexus_filesystem_disk_mounts:
  - disk: sdc
    path: '{{ nexus_blob_path }}/olympus'
    owner: '{{ nexus_user }}'
    group: '{{ nexus_group }}'
  - disk: sdd
    path: '{{ nexus_blob_path }}/public'
    owner: '{{ nexus_user }}'
    group: '{{ nexus_group }}'
```

### nexus_filesystem_lvs_mounts

#### Default value

```YAML
nexus_filesystem_lvs_mounts:
  - lv: '{{ nexus_lv_name }}'
    vg: '{{ nexus_vg_name }}'
    size: '{{ nexus_lv_size }}'
    path: '{{ nexus_home }}'
    owner: '{{ nexus_user }}'
    group: '{{ nexus_group }}'
  - lv: '{{ nexus_log_lv_name }}'
    vg: '{{ nexus_vg_name }}'
    size: '{{ nexus_log_size }}'
    path: '{{ nexus_log_path }}'
    owner: '{{ nexus_user }}'
    group: '{{ nexus_group }}'
```

### nexus_filesystem_vgs_to_create

#### Default value

```YAML
nexus_filesystem_vgs_to_create:
  - vg: '{{ nexus_vg_name }}'
```

### nexus_group

#### Default value

```YAML
nexus_group: nexus
```

### nexus_groups

#### Default value

```YAML
nexus_groups: [certbot]
```

### nexus_home

#### Default value

```YAML
nexus_home: /opt/nexus
```

### nexus_java_version

#### Default value

```YAML
nexus_java_version: 11
```

### nexus_log_lv_name

#### Default value

```YAML
nexus_log_lv_name: lv_nexus_log
```

### nexus_log_path

#### Default value

```YAML
nexus_log_path: /var/log/nexus
```

### nexus_log_size

#### Default value

```YAML
nexus_log_size: 1g
```

### nexus_lv_name

#### Default value

```YAML
nexus_lv_name: lv_nexus
```

### nexus_lv_size

#### Default value

```YAML
nexus_lv_size: 8g
```

### nexus_package

#### Default value

```YAML
nexus_package:
  - openjdk-{{ nexus_java_version }}-jdk
```

### nexus_run_home

#### Default value

```YAML
nexus_run_home: '{{ nexus_home }}/nexus-{{ nexus_version }}'
```

### nexus_ssl_enabled

#### Default value

```YAML
nexus_ssl_enabled: true
```

### nexus_ssl_file

#### Default value

```YAML
nexus_ssl_file:
  - src: /opt/certbot/eden/cert.pem
    dest: '{{ nexus_ssl_path }}/cert.pem'
  - src: /opt/certbot/eden/chain.pem
    dest: '{{ nexus_ssl_path }}/chain.pem'
  - src: /opt/certbot/eden/fullchain.pem
    dest: '{{ nexus_ssl_path }}/fullchain.pem'
  - src: /opt/certbot/eden/fullchain.pem.key
    dest: '{{ nexus_ssl_path }}/fullchain.pem.key'
```

### nexus_ssl_path

#### Default value

```YAML
nexus_ssl_path: '{{ nexus_home }}/ssl'
```

### nexus_templates

#### Default value

```YAML
nexus_templates:
  - src: nexus.service.j2
    dest: /etc/systemd/system/nexus.service
```

### nexus_user

#### Default value

```YAML
nexus_user: nexus
```

### nexus_version

#### Default value

```YAML
nexus_version: 3.68.0-04
```

### nexus_vg_name

#### Default value

```YAML
nexus_vg_name: tartarus
```



## Dependencies

- tocard.utils.certbot

## License

BSD-3-Clause

## Author

Douceur
