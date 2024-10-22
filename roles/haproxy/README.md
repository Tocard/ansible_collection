# haproxy

this role simply install & configure haproxy

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [haproxy_certs_path](#haproxy_certs_path)
  - [haproxy_config_folder](#haproxy_config_folder)
  - [haproxy_custom_dirs](#haproxy_custom_dirs)
  - [haproxy_filesystem_lvs_mounts](#haproxy_filesystem_lvs_mounts)
  - [haproxy_filesystem_vg_name](#haproxy_filesystem_vg_name)
  - [haproxy_group](#haproxy_group)
  - [haproxy_groups](#haproxy_groups)
  - [haproxy_packages](#haproxy_packages)
  - [haproxy_ssl_file](#haproxy_ssl_file)
  - [haproxy_stats_password](#haproxy_stats_password)
  - [haproxy_stats_user](#haproxy_stats_user)
  - [haproxy_sudo_become_method](#haproxy_sudo_become_method)
  - [haproxy_templates](#haproxy_templates)
  - [haproxy_user](#haproxy_user)
  - [haproxy_version](#haproxy_version)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### haproxy_certs_path

#### Default value

```YAML
haproxy_certs_path: /etc/haproxy/ssl
```

### haproxy_config_folder

#### Default value

```YAML
haproxy_config_folder: /etc/haproxy
```

### haproxy_custom_dirs

#### Default value

```YAML
haproxy_custom_dirs:
  - path: /run/haproxy
    mode: '0750'
  - path: /etc/haproxy/ssl
    mode: '0750'
```

### haproxy_filesystem_lvs_mounts

#### Default value

```YAML
haproxy_filesystem_lvs_mounts:
  - lv: lv_haproxy_log
    vg: '{{ haproxy_filesystem_vg_name }}'
    size: 1g
    path: /var/log/haproxy
    owner: '{{ haproxy_user }}'
    group: '{{ haproxy_group }}'
```

### haproxy_filesystem_vg_name

#### Default value

```YAML
haproxy_filesystem_vg_name: olympus
```

### haproxy_group

#### Default value

```YAML
haproxy_group: haproxy
```

### haproxy_groups

#### Default value

```YAML
haproxy_groups: [certbot]
```

### haproxy_packages

#### Default value

```YAML
haproxy_packages:
  - apt-utils
  - haproxy={{ haproxy_version }}
```

### haproxy_ssl_file

#### Default value

```YAML
haproxy_ssl_file:
  - src: /opt/certbot/eden/cert.pem
    dest: '{{ haproxy_certs_path }}/cert.pem'
  - src: /opt/certbot/eden/chain.pem
    dest: '{{ haproxy_certs_path }}/chain.pem'
  - src: /opt/certbot/eden/fullchain.pem
    dest: '{{ haproxy_certs_path }}/fullchain.pem'
  - src: /opt/certbot/eden/fullchain.pem.key
    dest: '{{ haproxy_certs_path }}/fullchain.pem.key'
```

### haproxy_stats_password

#### Default value

```YAML
haproxy_stats_password: "{{ lookup('hashi_vault', hashi_haproxy_path ~ '/stats_user:moz
  ' ~ hashi_connect) }}"
```

### haproxy_stats_user

#### Default value

```YAML
haproxy_stats_user: admin
```

### haproxy_sudo_become_method

#### Default value

```YAML
haproxy_sudo_become_method: sudo
```

### haproxy_templates

#### Default value

```YAML
haproxy_templates:
  - src: haproxy.cfg.j2
    dest: /etc/haproxy/00_haproxy.cfg
    mode: '0640'
  - src: stats.cfg.j2
    dest: /etc/haproxy/stats.cfg
    mode: '0640'
  - src: https.cfg.j2
    dest: /etc/haproxy/https.cfg
    mode: '0640'
  - src: elasticsearch.cfg.j2
    dest: /etc/haproxy/elasticsearch.cfg
    mode: '0640'
  - src: nats.cfg.j2
    dest: /etc/haproxy/nats.cfg
    mode: '0640'
  - src: subspace.cfg.j2
    dest: /etc/haproxy/subspace.cfg
    mode: '0640'
  - src: haproxy.service.j2
    dest: /lib/systemd/system/haproxy.service
    mode: '0644'
```

### haproxy_user

#### Default value

```YAML
haproxy_user: haproxy
```

### haproxy_version

#### Default value

```YAML
haproxy_version: 2.8.9-1ppa1~jammy
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
