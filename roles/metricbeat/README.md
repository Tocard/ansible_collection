# metricbeat

this role simply install & configure metricbeat

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [metricbeat_cosmos_chain_name](#metricbeat_cosmos_chain_name)
  - [metricbeat_cosmos_node_enabled](#metricbeat_cosmos_node_enabled)
  - [metricbeat_cosmos_node_host](#metricbeat_cosmos_node_host)
  - [metricbeat_cosmos_node_port](#metricbeat_cosmos_node_port)
  - [metricbeat_cosmos_template](#metricbeat_cosmos_template)
  - [metricbeat_custom_become_method](#metricbeat_custom_become_method)
  - [metricbeat_custom_dirs](#metricbeat_custom_dirs)
  - [metricbeat_custom_templates](#metricbeat_custom_templates)
  - [metricbeat_deb](#metricbeat_deb)
  - [metricbeat_filesystem_list](#metricbeat_filesystem_list)
  - [metricbeat_filesystem_vg_name](#metricbeat_filesystem_vg_name)
  - [metricbeat_gpg_key](#metricbeat_gpg_key)
  - [metricbeat_group](#metricbeat_group)
  - [metricbeat_hddtemp_templates](#metricbeat_hddtemp_templates)
  - [metricbeat_install_mode](#metricbeat_install_mode)
  - [metricbeat_log_dir](#metricbeat_log_dir)
  - [metricbeat_module_path](#metricbeat_module_path)
  - [metricbeat_owner](#metricbeat_owner)
  - [metricbeat_password](#metricbeat_password)
  - [metricbeat_use_generic_ac](#metricbeat_use_generic_ac)
  - [metricbeat_user](#metricbeat_user)
  - [metricbeat_version](#metricbeat_version)
  - [metricbeat_xpack_templates](#metricbeat_xpack_templates)
  - [metricbeat_yum_repo](#metricbeat_yum_repo)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### metricbeat_cosmos_chain_name

#### Default value

```YAML
metricbeat_cosmos_chain_name:
```

### metricbeat_cosmos_node_enabled

#### Default value

```YAML
metricbeat_cosmos_node_enabled: false
```

### metricbeat_cosmos_node_host

#### Default value

```YAML
metricbeat_cosmos_node_host: localhost
```

### metricbeat_cosmos_node_port

#### Default value

```YAML
metricbeat_cosmos_node_port:
```

### metricbeat_cosmos_template

#### Default value

```YAML
metricbeat_cosmos_template:
  - src: cosmos.yml.j2
    dest: '{{ metricbeat_module_path }}/cosmos.yml'
    owner: '{{ metricbeat_owner }}'
    group: '{{ metricbeat_group }}'
    mode: '0640'
```

### metricbeat_custom_become_method

#### Default value

```YAML
metricbeat_custom_become_method: sudo
```

### metricbeat_custom_dirs

#### Default value

```YAML
metricbeat_custom_dirs:
  - path: '{{ metricbeat_log_dir }}'
    state: directory
    owner: '{{ metricbeat_owner }}'
    group: '{{ metricbeat_group }}'
    mode: '0750'
```

### metricbeat_custom_templates

#### Default value

```YAML
metricbeat_custom_templates:
  - src: metricbeat.yml.j2
    dest: /etc/metricbeat/metricbeat.yml
    owner: '{{ metricbeat_owner }}'
    group: '{{ metricbeat_group }}'
    mode: '0640'
  - src: system.yml.j2
    dest: '{{ metricbeat_module_path }}/system.yml'
    owner: '{{ metricbeat_owner }}'
    group: '{{ metricbeat_group }}'
    mode: '0640'
```

### metricbeat_deb

#### Default value

```YAML
metricbeat_deb:
  - https://artifacts.elastic.co/packages/8.x/apt stable main
```

### metricbeat_filesystem_list

#### Default value

```YAML
metricbeat_filesystem_list:
  - lv: lv_metricbeat_log
    vg: '{{ metricbeat_filesystem_vg_name }}'
    size: 1g
    path: '{{ metricbeat_log_dir }}'
    owner: '{{ metricbeat_owner }}'
    group: '{{ metricbeat_group }}'
    mode: '0750'
```

### metricbeat_filesystem_vg_name

#### Default value

```YAML
metricbeat_filesystem_vg_name: olympus
```

### metricbeat_gpg_key

#### Default value

```YAML
metricbeat_gpg_key:
  - https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

### metricbeat_group

#### Default value

```YAML
metricbeat_group: root
```

### metricbeat_hddtemp_templates

#### Default value

```YAML
metricbeat_hddtemp_templates:
  - src: hddtemp.yml.j2
    dest: '{{ metricbeat_module_path }}/hddtemp.yml'
    owner: '{{ metricbeat_owner }}'
    group: '{{ metricbeat_group }}'
    mode: '0640'
```

### metricbeat_install_mode

#### Default value

```YAML
metricbeat_install_mode: latest
```

### metricbeat_log_dir

#### Default value

```YAML
metricbeat_log_dir: /var/log/metricbeat
```

### metricbeat_module_path

#### Default value

```YAML
metricbeat_module_path: /etc/metricbeat/modules.d
```

### metricbeat_owner

#### Default value

```YAML
metricbeat_owner: root
```

### metricbeat_password

#### Default value

```YAML
metricbeat_password: changeme
```

### metricbeat_use_generic_ac

#### Default value

```YAML
metricbeat_use_generic_ac: false
```

### metricbeat_user

#### Default value

```YAML
metricbeat_user: metricbeat
```

### metricbeat_version

#### Default value

```YAML
metricbeat_version: ''
```

### metricbeat_xpack_templates

#### Default value

```YAML
metricbeat_xpack_templates:
  - src: elasticsearch-xpack.yml.j2
    dest: '{{ metricbeat_module_path }}/elasticsearch-xpack.yml'
    owner: '{{ metricbeat_owner }}'
    group: '{{ metricbeat_group }}'
    mode: '0640'
```

### metricbeat_yum_repo

#### Default value

```YAML
metricbeat_yum_repo:
  - src: elastic.repo
    dest: /etc/yum.repos.d/elastic.repo
```



## Dependencies


## License

BSD-3-Clause

## Author

Douceur
