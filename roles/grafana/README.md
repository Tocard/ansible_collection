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
  - [grafana_filesystem_list](#grafana_filesystem_list)
  - [grafana_filesystem_vg_name](#grafana_filesystem_vg_name)
  - [grafana_gpg_key](#grafana_gpg_key)
  - [grafana_group](#grafana_group)
  - [grafana_http_port](#grafana_http_port)
  - [grafana_log_dir](#grafana_log_dir)
  - [grafana_owner](#grafana_owner)
  - [grafana_packages](#grafana_packages)
  - [grafana_public_domain](#grafana_public_domain)
  - [grafana_ssl_file](#grafana_ssl_file)
  - [grafana_ssl_location](#grafana_ssl_location)
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
  - path: /usr/share/grafana
  - path: '{{ grafana_data_dir }}'
  - path: /var/run/grafana
  - path: '{{ grafana_log_dir }}'
```

### grafana_filesystem_list

#### Default value

```YAML
grafana_filesystem_list:
  - lv: lv_grafana_data
    vg: '{{ grafana_filesystem_vg_name }}'
    size: 1G
    path: '{{ grafana_data_dir }}'
    owner: '{{ grafana_owner }}'
    group: '{{ grafana_owner }}'
    mode: '0750'
  - lv: lv_grafana_log
    vg: '{{ grafana_filesystem_vg_name }}'
    size: 500M
    path: '{{ grafana_log_dir }}'
    owner: '{{ grafana_owner }}'
    group: '{{ grafana_owner }}'
    mode: '0750'
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

### grafana_owner

#### Default value

```YAML
grafana_owner: grafana
```

### grafana_packages

#### Default value

```YAML
grafana_packages:
  - grafana=10.4.2
```

### grafana_public_domain

#### Default value

```YAML
grafana_public_domain: mythologic.fr
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



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
