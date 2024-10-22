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
  - [metricbeat_elasticsearch_password](#metricbeat_elasticsearch_password)
  - [metricbeat_elasticsearch_url](#metricbeat_elasticsearch_url)
  - [metricbeat_elasticsearch_user](#metricbeat_elasticsearch_user)
  - [metricbeat_filesystem_enabled](#metricbeat_filesystem_enabled)
  - [metricbeat_filesystem_lvs_mounts](#metricbeat_filesystem_lvs_mounts)
  - [metricbeat_filesystem_vg_name](#metricbeat_filesystem_vg_name)
  - [metricbeat_gpg_key](#metricbeat_gpg_key)
  - [metricbeat_group](#metricbeat_group)
  - [metricbeat_install_mode](#metricbeat_install_mode)
  - [metricbeat_log_dir](#metricbeat_log_dir)
  - [metricbeat_module_path](#metricbeat_module_path)
  - [metricbeat_ssl_files](#metricbeat_ssl_files)
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
```

### metricbeat_custom_templates

#### Default value

```YAML
metricbeat_custom_templates:
  - src: metricbeat.yml.j2
    dest: /etc/metricbeat/metricbeat.yml
  - src: system.yml.j2
    dest: '{{ metricbeat_module_path }}/system.yml'
```

### metricbeat_deb

#### Default value

```YAML
metricbeat_deb:
  - https://artifacts.elastic.co/packages/8.x/apt stable main
```

### metricbeat_elasticsearch_password

#### Default value

```YAML
metricbeat_elasticsearch_password: free_metricbeat4ever
```

### metricbeat_elasticsearch_url

#### Default value

```YAML
metricbeat_elasticsearch_url: https://mythologic.fr:9200
```

### metricbeat_elasticsearch_user

#### Default value

```YAML
metricbeat_elasticsearch_user: free_metricbeat
```

### metricbeat_filesystem_enabled

#### Default value

```YAML
metricbeat_filesystem_enabled: true
```

### metricbeat_filesystem_lvs_mounts

#### Default value

```YAML
metricbeat_filesystem_lvs_mounts:
  - lv: lv_metricbeat_log
    vg: '{{ metricbeat_filesystem_vg_name }}'
    size: 1g
    path: '{{ metricbeat_log_dir }}'
    owner: '{{ metricbeat_user }}'
    group: '{{ metricbeat_group }}'
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

### metricbeat_ssl_files

#### Default value

```YAML
metricbeat_ssl_files:
  - /etc/metricbeat/chain.pem
```

### metricbeat_use_generic_ac

#### Default value

```YAML
metricbeat_use_generic_ac: false
```

### metricbeat_user

#### Default value

```YAML
metricbeat_user: root
```

### metricbeat_version

#### Default value

```YAML
metricbeat_version: 8.14.2
```

### metricbeat_xpack_templates

#### Default value

```YAML
metricbeat_xpack_templates:
  - src: elasticsearch-xpack.yml.j2
    dest: '{{ metricbeat_module_path }}/elasticsearch-xpack.yml'
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
