# kibana

this role simply install & configure kibana

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [kibana_custom_become_method](#kibana_custom_become_method)
  - [kibana_custom_dirs](#kibana_custom_dirs)
  - [kibana_custom_templates](#kibana_custom_templates)
  - [kibana_data_dir](#kibana_data_dir)
  - [kibana_deb](#kibana_deb)
  - [kibana_elasticsearch_url](#kibana_elasticsearch_url)
  - [kibana_elasticsearch_username](#kibana_elasticsearch_username)
  - [kibana_filesystem_lvs_mounts](#kibana_filesystem_lvs_mounts)
  - [kibana_filesystem_vg_name](#kibana_filesystem_vg_name)
  - [kibana_gpg_key](#kibana_gpg_key)
  - [kibana_group](#kibana_group)
  - [kibana_groups](#kibana_groups)
  - [kibana_log_dir](#kibana_log_dir)
  - [kibana_package](#kibana_package)
  - [kibana_share_dir](#kibana_share_dir)
  - [kibana_ssl_file](#kibana_ssl_file)
  - [kibana_ssl_path](#kibana_ssl_path)
  - [kibana_user](#kibana_user)
  - [kibana_version](#kibana_version)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### kibana_custom_become_method

#### Default value

```YAML
kibana_custom_become_method: sudo
```

### kibana_custom_dirs

#### Default value

```YAML
kibana_custom_dirs:
  - path: '{{ kibana_log_dir }}'
  - path: '{{ kibana_ssl_path }}'
```

### kibana_custom_templates

#### Default value

```YAML
kibana_custom_templates:
  - src: kibana.yml.j2
    dest: /etc/kibana/kibana.yml
```

### kibana_data_dir

#### Default value

```YAML
kibana_data_dir: /var/lib/kibana
```

### kibana_deb

#### Default value

```YAML
kibana_deb:
  - https://artifacts.elastic.co/packages/8.x/apt stable main
```

### kibana_elasticsearch_url

#### Default value

```YAML
kibana_elasticsearch_url:
```

### kibana_elasticsearch_username

#### Default value

```YAML
kibana_elasticsearch_username: kibana_system
```

### kibana_filesystem_lvs_mounts

#### Default value

```YAML
kibana_filesystem_lvs_mounts:
  - lv: lv_kibana_data
    vg: '{{ kibana_filesystem_vg_name }}'
    size: 1g
    path: '{{ kibana_data_dir }}'
    owner: '{{ kibana_user }}'
    group: '{{ kibana_group }}'
  - lv: lv_kibana_share
    vg: '{{ kibana_filesystem_vg_name }}'
    size: 1536m
    path: '{{ kibana_share_dir }}'
    owner: '{{ kibana_user }}'
    group: '{{ kibana_group }}'
  - lv: lv_kibana_log
    vg: '{{ kibana_filesystem_vg_name }}'
    size: 1g
    path: '{{ kibana_log_dir }}'
    owner: '{{ kibana_user }}'
    group: '{{ kibana_group }}'
```

### kibana_filesystem_vg_name

#### Default value

```YAML
kibana_filesystem_vg_name: olympus
```

### kibana_gpg_key

#### Default value

```YAML
kibana_gpg_key:
  - https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

### kibana_group

#### Default value

```YAML
kibana_group: kibana
```

### kibana_groups

#### Default value

```YAML
kibana_groups: [certbot]
```

### kibana_log_dir

#### Default value

```YAML
kibana_log_dir: /var/log/kibana
```

### kibana_package

#### Default value

```YAML
kibana_package:
  - kibana={{ kibana_version }}
```

### kibana_share_dir

#### Default value

```YAML
kibana_share_dir: /usr/share/kibana
```

### kibana_ssl_file

#### Default value

```YAML
kibana_ssl_file:
  - src: /opt/certbot/eden/cert.pem
    dest: '{{ kibana_ssl_path }}/cert.pem'
  - src: /opt/certbot/eden/chain.pem
    dest: '{{ kibana_ssl_path }}/chain.pem'
  - src: /opt/certbot/eden/fullchain.pem
    dest: '{{ kibana_ssl_path }}/fullchain.pem'
  - src: /opt/certbot/eden/fullchain.pem.key
    dest: '{{ kibana_ssl_path }}/fullchain.pem.key'
```

### kibana_ssl_path

#### Default value

```YAML
kibana_ssl_path: /etc/kibana/ssl
```

### kibana_user

#### Default value

```YAML
kibana_user: kibana
```

### kibana_version

#### Default value

```YAML
kibana_version: 8.13.4
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
