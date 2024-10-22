# cosmos_node

this role install & configure generic cosmos full node

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [cosmos_node](#cosmos_node)
  - [cosmos_node_addrbook_donwload_url](#cosmos_node_addrbook_donwload_url)
  - [cosmos_node_app_toml_path](#cosmos_node_app_toml_path)
  - [cosmos_node_arch](#cosmos_node_arch)
  - [cosmos_node_base_url](#cosmos_node_base_url)
  - [cosmos_node_binaries](#cosmos_node_binaries)
  - [cosmos_node_binaries_download_url](#cosmos_node_binaries_download_url)
  - [cosmos_node_binaries_path](#cosmos_node_binaries_path)
  - [cosmos_node_chain_id](#cosmos_node_chain_id)
  - [cosmos_node_config_path](#cosmos_node_config_path)
  - [cosmos_node_config_toml_path](#cosmos_node_config_toml_path)
  - [cosmos_node_data_disk_name](#cosmos_node_data_disk_name)
  - [cosmos_node_database_backend](#cosmos_node_database_backend)
  - [cosmos_node_denom](#cosmos_node_denom)
  - [cosmos_node_directories](#cosmos_node_directories)
  - [cosmos_node_extra_remote_config_file](#cosmos_node_extra_remote_config_file)
  - [cosmos_node_filesystem_disk_mounts](#cosmos_node_filesystem_disk_mounts)
  - [cosmos_node_filesystem_lvs_mounts](#cosmos_node_filesystem_lvs_mounts)
  - [cosmos_node_genesis_donwload_url](#cosmos_node_genesis_donwload_url)
  - [cosmos_node_genesis_location](#cosmos_node_genesis_location)
  - [cosmos_node_group](#cosmos_node_group)
  - [cosmos_node_key_name](#cosmos_node_key_name)
  - [cosmos_node_key_password](#cosmos_node_key_password)
  - [cosmos_node_keys_management_enabled](#cosmos_node_keys_management_enabled)
  - [cosmos_node_linimum_gas_price](#cosmos_node_linimum_gas_price)
  - [cosmos_node_log_file](#cosmos_node_log_file)
  - [cosmos_node_log_format](#cosmos_node_log_format)
  - [cosmos_node_log_level](#cosmos_node_log_level)
  - [cosmos_node_log_lv_name](#cosmos_node_log_lv_name)
  - [cosmos_node_log_path](#cosmos_node_log_path)
  - [cosmos_node_log_size](#cosmos_node_log_size)
  - [cosmos_node_moniker](#cosmos_node_moniker)
  - [cosmos_node_p2p_external_address](#cosmos_node_p2p_external_address)
  - [cosmos_node_p2p_external_address_enabled](#cosmos_node_p2p_external_address_enabled)
  - [cosmos_node_p2p_external_port](#cosmos_node_p2p_external_port)
  - [cosmos_node_p2p_port](#cosmos_node_p2p_port)
  - [cosmos_node_packages](#cosmos_node_packages)
  - [cosmos_node_path](#cosmos_node_path)
  - [cosmos_node_persistent_peers](#cosmos_node_persistent_peers)
  - [cosmos_node_privkey_validator](#cosmos_node_privkey_validator)
  - [cosmos_node_prometheus_enabled](#cosmos_node_prometheus_enabled)
  - [cosmos_node_prometheus_namespace](#cosmos_node_prometheus_namespace)
  - [cosmos_node_prometheus_port](#cosmos_node_prometheus_port)
  - [cosmos_node_seeds](#cosmos_node_seeds)
  - [cosmos_node_short_name](#cosmos_node_short_name)
  - [cosmos_node_sudo_method](#cosmos_node_sudo_method)
  - [cosmos_node_templates](#cosmos_node_templates)
  - [cosmos_node_upnp_enabled](#cosmos_node_upnp_enabled)
  - [cosmos_node_user](#cosmos_node_user)
  - [cosmos_node_validator_mode](#cosmos_node_validator_mode)
  - [cosmos_node_validator_templates](#cosmos_node_validator_templates)
  - [cosmos_node_validator_templates_enabled](#cosmos_node_validator_templates_enabled)
  - [cosmos_node_version](#cosmos_node_version)
  - [cosmos_node_vg_name](#cosmos_node_vg_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### cosmos_node

#### Default value

```YAML
cosmos_node: nibiru
```

### cosmos_node_addrbook_donwload_url

#### Default value

```YAML
cosmos_node_addrbook_donwload_url: https://snapshots.kjnodes.com/nibiru/addrbook.json
```

### cosmos_node_app_toml_path

#### Default value

```YAML
cosmos_node_app_toml_path: '{{ cosmos_node_config_path }}/app.toml'
```

### cosmos_node_arch

#### Default value

```YAML
cosmos_node_arch: linux_amd64
```

### cosmos_node_base_url

#### Default value

```YAML
cosmos_node_base_url: https://github.com/NibiruChain/nibiru/releases/download
```

### cosmos_node_binaries

#### Default value

```YAML
cosmos_node_binaries: '{{ cosmos_node_short_name }}'
```

### cosmos_node_binaries_download_url

#### Default value

```YAML
cosmos_node_binaries_download_url: '{{ cosmos_node_base_url }}/v{{ cosmos_node_version
  }}/nibid_{{ cosmos_node_version }}_{{ cosmos_node_arch }}.tar.gz'
```

### cosmos_node_binaries_path

#### Default value

```YAML
cosmos_node_binaries_path: /usr/bin
```

### cosmos_node_chain_id

#### Default value

```YAML
cosmos_node_chain_id: cataclysm-1
```

### cosmos_node_config_path

#### Default value

```YAML
cosmos_node_config_path: '{{ cosmos_node_path }}/config'
```

### cosmos_node_config_toml_path

#### Default value

```YAML
cosmos_node_config_toml_path: '{{ cosmos_node_config_path }}/config.toml'
```

### cosmos_node_data_disk_name

#### Default value

```YAML
cosmos_node_data_disk_name: sdb
```

### cosmos_node_database_backend

#### Default value

```YAML
cosmos_node_database_backend: goleveldb
```

### cosmos_node_denom

#### Default value

```YAML
cosmos_node_denom:
```

### cosmos_node_directories

#### Default value

```YAML
cosmos_node_directories:
  - path: '{{ cosmos_node_path }}'
  - path: '{{ cosmos_node_config_path }}'
  - path: '{{ cosmos_node_log_path }}'
```

### cosmos_node_extra_remote_config_file

#### Default value

```YAML
cosmos_node_extra_remote_config_file:
  - src: '{{ cosmos_node_genesis_donwload_url }}'
    dest: '{{ cosmos_node_config_path }}/genesis.json'
  - src: '{{ cosmos_node_addrbook_donwload_url }}'
    dest: '{{ cosmos_node_config_path }}/addrbook.json'
```

### cosmos_node_filesystem_disk_mounts

#### Default value

```YAML
cosmos_node_filesystem_disk_mounts:
  - disk: '{{ cosmos_node_data_disk_name }}'
    path: '{{ cosmos_node_path }}'
    owner: '{{ cosmos_node_user }}'
    group: '{{ cosmos_node_group }}'
```

### cosmos_node_filesystem_lvs_mounts

#### Default value

```YAML
cosmos_node_filesystem_lvs_mounts:
  - lv: '{{ cosmos_node_log_lv_name }}'
    vg: '{{ cosmos_node_vg_name }}'
    size: '{{ cosmos_node_log_size }}'
    path: '{{ cosmos_node_log_path }}'
    owner: '{{ cosmos_node_user }}'
    group: '{{ cosmos_node_group }}'
```

### cosmos_node_genesis_donwload_url

#### Default value

```YAML
cosmos_node_genesis_donwload_url: https://snapshots.kjnodes.com/nibiru/genesis.json
```

### cosmos_node_genesis_location

#### Default value

```YAML
cosmos_node_genesis_location: '{{ cosmos_node_config_path }}/genesis.json'
```

### cosmos_node_group

#### Default value

```YAML
cosmos_node_group: '{{ cosmos_node }}'
```

### cosmos_node_key_name

#### Default value

```YAML
cosmos_node_key_name: '{{ ansible_hostname }}'
```

### cosmos_node_key_password

#### Default value

```YAML
cosmos_node_key_password: "{{ lookup('hashi_vault', hashi_cosmos_node_path ~ '/' ~
  ansible_hostname  ~ hashi_connect) }}"
```

### cosmos_node_keys_management_enabled

#### Default value

```YAML
cosmos_node_keys_management_enabled: false
```

### cosmos_node_linimum_gas_price

#### Default value

```YAML
cosmos_node_linimum_gas_price: 0.5{{ cosmos_node_denom }}
```

### cosmos_node_log_file

#### Default value

```YAML
cosmos_node_log_file: '{{ cosmos_node }}.log'
```

### cosmos_node_log_format

#### Default value

```YAML
cosmos_node_log_format: json
```

### cosmos_node_log_level

#### Default value

```YAML
cosmos_node_log_level: info
```

### cosmos_node_log_lv_name

#### Default value

```YAML
cosmos_node_log_lv_name: lv_log_{{ cosmos_node }}
```

### cosmos_node_log_path

#### Default value

```YAML
cosmos_node_log_path: /var/log/{{ cosmos_node }}
```

### cosmos_node_log_size

#### Default value

```YAML
cosmos_node_log_size: 2g
```

### cosmos_node_moniker

#### Default value

```YAML
cosmos_node_moniker: '{{ ansible_hostname }}'
```

### cosmos_node_p2p_external_address

#### Default value

```YAML
cosmos_node_p2p_external_address: ''
```

### cosmos_node_p2p_external_address_enabled

#### Default value

```YAML
cosmos_node_p2p_external_address_enabled: false
```

### cosmos_node_p2p_external_port

#### Default value

```YAML
cosmos_node_p2p_external_port: '{{ cosmos_node_p2p_port }}'
```

### cosmos_node_p2p_port

#### Default value

```YAML
cosmos_node_p2p_port: 26656
```

### cosmos_node_packages

#### Default value

```YAML
cosmos_node_packages:
  - jq
  - curl
  - acl
```

### cosmos_node_path

#### Default value

```YAML
cosmos_node_path: /opt/{{ cosmos_node }}/{{ cosmos_node_chain_id }}
```

### cosmos_node_persistent_peers

#### Default value

```YAML
cosmos_node_persistent_peers:
```

### cosmos_node_privkey_validator

#### Default value

```YAML
cosmos_node_privkey_validator: "{{ lookup('hashi_vault', hashi_cosmos_node_path ~
  '/' ~ ansible_hostname ~ hashi_connect) }}"
```

### cosmos_node_prometheus_enabled

#### Default value

```YAML
cosmos_node_prometheus_enabled: true
```

### cosmos_node_prometheus_namespace

#### Default value

```YAML
cosmos_node_prometheus_namespace: cometbft
```

### cosmos_node_prometheus_port

#### Default value

```YAML
cosmos_node_prometheus_port: :26660
```

### cosmos_node_seeds

#### Default value

```YAML
cosmos_node_seeds:
```

### cosmos_node_short_name

#### Default value

```YAML
cosmos_node_short_name: nibid
```

### cosmos_node_sudo_method

#### Default value

```YAML
cosmos_node_sudo_method: sudo
```

### cosmos_node_templates

#### Default value

```YAML
cosmos_node_templates:
  - src: node.service.j2
    dest: /etc/systemd/system/{{ cosmos_node }}.service
```

### cosmos_node_upnp_enabled

#### Default value

```YAML
cosmos_node_upnp_enabled: false
```

### cosmos_node_user

#### Default value

```YAML
cosmos_node_user: '{{ cosmos_node }}'
```

### cosmos_node_validator_mode

#### Default value

```YAML
cosmos_node_validator_mode: false
```

### cosmos_node_validator_templates

#### Default value

```YAML
cosmos_node_validator_templates:
  - src: priv_validator_key.json.j2
    dest: '{{ cosmos_node_config_path }}/priv_validator_key.json'
```

### cosmos_node_validator_templates_enabled

#### Default value

```YAML
cosmos_node_validator_templates_enabled: true
```

### cosmos_node_version

#### Default value

```YAML
cosmos_node_version: 1.3.0
```

### cosmos_node_vg_name

#### Default value

```YAML
cosmos_node_vg_name: olympus
```



## Dependencies


## License

BSD-3-Clause

## Author

Douceur
