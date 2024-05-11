# streamr

this role simply install streamr with npm

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [streamr_directories](#streamr_directories)
  - [streamr_exec_start_command](#streamr_exec_start_command)
  - [streamr_filesystem_enabled](#streamr_filesystem_enabled)
  - [streamr_filesystem_list](#streamr_filesystem_list)
  - [streamr_group](#streamr_group)
  - [streamr_install_dir](#streamr_install_dir)
  - [streamr_log_color_enabled](#streamr_log_color_enabled)
  - [streamr_log_dir](#streamr_log_dir)
  - [streamr_log_filename_name](#streamr_log_filename_name)
  - [streamr_logrotate_folder](#streamr_logrotate_folder)
  - [streamr_lv_data_size](#streamr_lv_data_size)
  - [streamr_lv_log_size](#streamr_lv_log_size)
  - [streamr_node_port_max](#streamr_node_port_max)
  - [streamr_node_port_min](#streamr_node_port_min)
  - [streamr_node_priv_key](#streamr_node_priv_key)
  - [streamr_node_version](#streamr_node_version)
  - [streamr_nodejs_version](#streamr_nodejs_version)
  - [streamr_operator_contract_adress](#streamr_operator_contract_adress)
  - [streamr_package_list](#streamr_package_list)
  - [streamr_pretty_log_disabled](#streamr_pretty_log_disabled)
  - [streamr_run_script_name](#streamr_run_script_name)
  - [streamr_serial_mode_enabled](#streamr_serial_mode_enabled)
  - [streamr_serial_sleep](#streamr_serial_sleep)
  - [streamr_sudo_method](#streamr_sudo_method)
  - [streamr_supervision_log_enabled](#streamr_supervision_log_enabled)
  - [streamr_supervision_metric_enabled](#streamr_supervision_metric_enabled)
  - [streamr_templates](#streamr_templates)
  - [streamr_user](#streamr_user)
  - [streamr_virtual_group_name](#streamr_virtual_group_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### streamr_directories

#### Default value

```YAML
streamr_directories:
  - path: '{{ streamr_install_dir }}'
  - path: '{{ streamr_log_dir }}'
```

### streamr_exec_start_command

#### Default value

```YAML
streamr_exec_start_command: sh {{ streamr_install_dir}}/{{ streamr_run_script_name
  }}
```

### streamr_filesystem_enabled

#### Default value

```YAML
streamr_filesystem_enabled: true
```

### streamr_filesystem_list

#### Default value

```YAML
streamr_filesystem_list:
  - lv: lv_streamr_data
    vg: '{{ streamr_virtual_group_name }}'
    size: '{{ streamr_lv_data_size }}'
    path: '{{ streamr_install_dir }}'
    owner: '{{ streamr_user }}'
    group: '{{ streamr_group }}'
    mode: '0750'
    fstype: xfs
    force: false
    shrink: false
  - lv: lv_streamr_log
    vg: '{{ streamr_virtual_group_name }}'
    size: '{{ streamr_lv_log_size }}'
    path: '{{ streamr_log_dir }}'
    owner: '{{ streamr_user }}'
    group: '{{ streamr_group }}'
    mode: '0750'
    fstype: xfs
    force: false
    shrink: false
```

### streamr_group

#### Default value

```YAML
streamr_group: chimera
```

### streamr_install_dir

#### Default value

```YAML
streamr_install_dir: /opt/chimera/streamr
```

### streamr_log_color_enabled

#### Default value

```YAML
streamr_log_color_enabled: false
```

### streamr_log_dir

#### Default value

```YAML
streamr_log_dir: /var/log/chimera
```

### streamr_log_filename_name

#### Default value

```YAML
streamr_log_filename_name: streamr.log
```

### streamr_logrotate_folder

#### Default value

```YAML
streamr_logrotate_folder: /etc/logrotate.d
```

### streamr_lv_data_size

#### Default value

```YAML
streamr_lv_data_size: 10G
```

### streamr_lv_log_size

#### Default value

```YAML
streamr_lv_log_size: 1G
```

### streamr_node_port_max

#### Default value

```YAML
streamr_node_port_max: 32200
```

### streamr_node_port_min

#### Default value

```YAML
streamr_node_port_min: 32200
```

### streamr_node_priv_key

#### Default value

```YAML
streamr_node_priv_key: "{{ lookup('hashi_vault', hashi_streamr_path ~ '/streamr_node_privkey
  ' ~ hashi_connect) }}"
```

### streamr_node_version

#### Default value

```YAML
streamr_node_version: 100.2.3
```

### streamr_nodejs_version

#### Default value

```YAML
streamr_nodejs_version: 20.10.0
```

### streamr_operator_contract_adress

#### Default value

```YAML
streamr_operator_contract_adress: '0x25f83066055bc49395ffa782325f1f19c59e1358'
```

### streamr_package_list

#### Default value

```YAML
streamr_package_list:
  - git
  - curl
  - acl
```

### streamr_pretty_log_disabled

#### Default value

```YAML
streamr_pretty_log_disabled: true
```

### streamr_run_script_name

#### Default value

```YAML
streamr_run_script_name: run_streamr.sh
```

### streamr_serial_mode_enabled

#### Default value

```YAML
streamr_serial_mode_enabled: false
```

### streamr_serial_sleep

#### Default value

```YAML
streamr_serial_sleep: 240
```

### streamr_sudo_method

#### Default value

```YAML
streamr_sudo_method: sudo
```

### streamr_supervision_log_enabled

#### Default value

```YAML
streamr_supervision_log_enabled: false
```

### streamr_supervision_metric_enabled

#### Default value

```YAML
streamr_supervision_metric_enabled: false
```

### streamr_templates

#### Default value

```YAML
streamr_templates:
  - src: default.json.j2
    dest: '{{ streamr_install_dir }}/default.json'
  - src: run_node.sh.j2
    dest: '{{ streamr_install_dir }}/{{ streamr_run_script_name}}'
  - src: streamr.service.j2
    dest: /etc/systemd/system/streamr.service
  - src: logrotate_streamr_node.j2
    dest: '{{ streamr_logrotate_folder }}/logrotate_streamr_node'
```

### streamr_user

#### Default value

```YAML
streamr_user: chimera
```

### streamr_virtual_group_name

#### Default value

```YAML
streamr_virtual_group_name: data_virtual
```



## Dependencies


## License

BSD-3-Clause

## Author

Douceur
