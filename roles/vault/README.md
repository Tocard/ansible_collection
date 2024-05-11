# vault

this role simply install & configure vault server

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [vault_base_path](#vault_base_path)
  - [vault_bind_adress](#vault_bind_adress)
  - [vault_bind_port](#vault_bind_port)
  - [vault_custom_become_method](#vault_custom_become_method)
  - [vault_custom_templates](#vault_custom_templates)
  - [vault_filesystem_list](#vault_filesystem_list)
  - [vault_filesystem_vg_name](#vault_filesystem_vg_name)
  - [vault_gpg_key](#vault_gpg_key)
  - [vault_group](#vault_group)
  - [vault_groups](#vault_groups)
  - [vault_log_file](#vault_log_file)
  - [vault_log_path](#vault_log_path)
  - [vault_package_list](#vault_package_list)
  - [vault_path_data](#vault_path_data)
  - [vault_ssl_enabled](#vault_ssl_enabled)
  - [vault_ssl_file](#vault_ssl_file)
  - [vault_user](#vault_user)
  - [vault_version](#vault_version)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### vault_base_path

#### Default value

```YAML
vault_base_path: /opt/vault
```

### vault_bind_adress

#### Default value

```YAML
vault_bind_adress: 0.0.0.0
```

### vault_bind_port

#### Default value

```YAML
vault_bind_port: 8200
```

### vault_custom_become_method

#### Default value

```YAML
vault_custom_become_method: sudo
```

### vault_custom_templates

#### Default value

```YAML
vault_custom_templates:
  - src: vault.hcl.j2
    dest: /etc/vault.d/vault.hcl
    mode: '0640'
  - src: vault.service.j2
    dest: /etc/systemd/system/vault.service
    mode: '0640'
```

### vault_filesystem_list

#### Default value

```YAML
vault_filesystem_list:
  - lv: lv_vault_data
    vg: '{{ vault_filesystem_vg_name }}'
    size: 5g
    path: '{{ vault_path_data }}'
    owner: '{{ vault_user }}'
    group: '{{ vault_group }}'
    mode: '0750'
  - lv: lv_vault_log
    vg: '{{ vault_filesystem_vg_name }}'
    size: 1g
    path: '{{ vault_log_path }}'
    owner: '{{ vault_user }}'
    group: '{{ vault_group }}'
    mode: '0750'
```

### vault_filesystem_vg_name

#### Default value

```YAML
vault_filesystem_vg_name: olympus
```

### vault_gpg_key

#### Default value

```YAML
vault_gpg_key: https://apt.releases.hashicorp.com/gpg
```

### vault_group

#### Default value

```YAML
vault_group: vault
```

### vault_groups

#### Default value

```YAML
vault_groups: [certbot]
```

### vault_log_file

#### Default value

```YAML
vault_log_file: vault.log
```

### vault_log_path

#### Default value

```YAML
vault_log_path: /var/log/vault
```

### vault_package_list

#### Default value

```YAML
vault_package_list:
  - vault={{ vault_version  }}
```

### vault_path_data

#### Default value

```YAML
vault_path_data: '{{ vault_base_path}}/data'
```

### vault_ssl_enabled

#### Default value

```YAML
vault_ssl_enabled: true
```

### vault_ssl_file

#### Default value

```YAML
vault_ssl_file:
  - src: /opt/certbot/eden/fullchain.pem
    dest: '{{ vault_base_path }}/tls.crt'
  - src: /opt/certbot/eden/fullchain.pem.key
    dest: '{{ vault_base_path }}/tls.key'
```

### vault_user

#### Default value

```YAML
vault_user: vault
```

### vault_version

#### Default value

```YAML
vault_version: 1.16.2-1
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem
- tocard.utils.certbot

## License

BSD-3-Clause

## Author

Douceur
