# grafana

this role simply install & configure grafana

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [grafana_admin_user](#grafana_admin_user)
  - [grafana_custom_become_method](#grafana_custom_become_method)
  - [grafana_custom_configs](#grafana_custom_configs)
  - [grafana_custom_packages](#grafana_custom_packages)
  - [grafana_data_dir](#grafana_data_dir)
  - [grafana_deb](#grafana_deb)
  - [grafana_directories](#grafana_directories)
  - [grafana_directories_patch](#grafana_directories_patch)
  - [grafana_enforce_domain](#grafana_enforce_domain)
  - [grafana_filesystem_lvs_mounts](#grafana_filesystem_lvs_mounts)
  - [grafana_filesystem_vg_name](#grafana_filesystem_vg_name)
  - [grafana_gpg_key](#grafana_gpg_key)
  - [grafana_group](#grafana_group)
  - [grafana_groups](#grafana_groups)
  - [grafana_http_port](#grafana_http_port)
  - [grafana_log_dir](#grafana_log_dir)
  - [grafana_packages](#grafana_packages)
  - [grafana_public_domain](#grafana_public_domain)
  - [grafana_root_url](#grafana_root_url)
  - [grafana_secret](#grafana_secret)
  - [grafana_ssl_file](#grafana_ssl_file)
  - [grafana_ssl_location](#grafana_ssl_location)
  - [grafana_sub_path_enabled](#grafana_sub_path_enabled)
  - [grafana_user](#grafana_user)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### grafana_admin_user

#### Default value

```YAML
grafana_admin_user: admin
```

### grafana_custom_become_method

#### Default value

```YAML
grafana_custom_become_method: sudo
```

### grafana_custom_configs

#### Default value

```YAML
grafana_custom_configs:
  - src: grafana.ini.j2
    dest: /etc/grafana/grafana.ini
```

### grafana_custom_packages

#### Default value

```YAML
grafana_custom_packages:
  - nss
  - gtk3
```

### grafana_data_dir

#### Default value

```YAML
grafana_data_dir: /var/lib/grafana
```

### grafana_deb

#### Default value

```YAML
grafana_deb:
  - https://packages.grafana.com/oss/deb stable main
  - https://packages.grafana.com/enterprise/deb stable main
```

### grafana_directories

#### Default value

```YAML
grafana_directories:
  - path: '{{ grafana_ssl_location }}'
  - path: '{{ grafana_log_dir }}'
```

### grafana_directories_patch

#### Default value

```YAML
grafana_directories_patch:
  - path: /usr/share/grafana
  - path: '{{ grafana_data_dir }}'
  - path: /var/run/grafana
  - path: /etc/grafana
```

### grafana_enforce_domain

#### Default value

```YAML
grafana_enforce_domain: false
```

### grafana_filesystem_lvs_mounts

#### Default value

```YAML
grafana_filesystem_lvs_mounts:
  - lv: lv_grafana_data
    vg: '{{ grafana_filesystem_vg_name }}'
    size: 1g
    path: '{{ grafana_data_dir }}'
    owner: '{{ grafana_user }}'
    group: '{{ grafana_user }}'
  - lv: lv_grafana_log
    vg: '{{ grafana_filesystem_vg_name }}'
    size: 500m
    path: '{{ grafana_log_dir }}'
    owner: '{{ grafana_user }}'
    group: '{{ grafana_user }}'
```

### grafana_filesystem_vg_name

#### Default value

```YAML
grafana_filesystem_vg_name: olympus
```

### grafana_gpg_key

#### Default value

```YAML
grafana_gpg_key:
  - https://packages.grafana.com/gpg.key
```

### grafana_group

#### Default value

```YAML
grafana_group: grafana
```

### grafana_groups

#### Default value

```YAML
grafana_groups: [certbot]
```

### grafana_http_port

#### Default value

```YAML
grafana_http_port: 3000
```

### grafana_log_dir

#### Default value

```YAML
grafana_log_dir: /var/log/grafana
```

### grafana_packages

#### Default value

```YAML
grafana_packages:
  - grafana-enterprise=10.4.2
```

### grafana_public_domain

#### Default value

```YAML
grafana_public_domain: '{{ ansible_hostname }}'
```

### grafana_root_url

#### Default value

```YAML
grafana_root_url: '%(protocol)s://%(domain)s:%(http_port)s/grafana/'
```

### grafana_secret

#### Default value

```YAML
grafana_secret: change_me
```

### grafana_ssl_file

#### Default value

```YAML
grafana_ssl_file:
  - src: /opt/certbot/eden/cert.pem
    dest: '{{ grafana_ssl_location }}/cert.pem'
  - src: /opt/certbot/eden/chain.pem
    dest: '{{ grafana_ssl_location }}/chain.pem'
  - src: /opt/certbot/eden/fullchain.pem
    dest: '{{ grafana_ssl_location }}/fullchain.pem'
  - src: /opt/certbot/eden/fullchain.pem.key
    dest: '{{ grafana_ssl_location }}/fullchain.pem.key'
```

### grafana_ssl_location

#### Default value

```YAML
grafana_ssl_location: /etc/grafana/ssl
```

### grafana_sub_path_enabled

#### Default value

```YAML
grafana_sub_path_enabled: true
```

### grafana_user

#### Default value

```YAML
grafana_user: grafana
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
