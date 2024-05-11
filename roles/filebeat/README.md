# filebeat

this role simply install & configure filebeat

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [filebeat_custom_become_method](#filebeat_custom_become_method)
  - [filebeat_custom_dirs](#filebeat_custom_dirs)
  - [filebeat_custom_templates](#filebeat_custom_templates)
  - [filebeat_deb](#filebeat_deb)
  - [filebeat_filesyste_vg_name](#filebeat_filesyste_vg_name)
  - [filebeat_filesystem_list](#filebeat_filesystem_list)
  - [filebeat_gpg_key](#filebeat_gpg_key)
  - [filebeat_group](#filebeat_group)
  - [filebeat_input_dir](#filebeat_input_dir)
  - [filebeat_input_templates](#filebeat_input_templates)
  - [filebeat_install_mode](#filebeat_install_mode)
  - [filebeat_log_dir](#filebeat_log_dir)
  - [filebeat_log_path_to_watch](#filebeat_log_path_to_watch)
  - [filebeat_module_path](#filebeat_module_path)
  - [filebeat_owner](#filebeat_owner)
  - [filebeat_password](#filebeat_password)
  - [filebeat_use_generic_ac](#filebeat_use_generic_ac)
  - [filebeat_user](#filebeat_user)
  - [filebeat_version](#filebeat_version)
  - [subspace_filebeat_enabled](#subspace_filebeat_enabled)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### filebeat_custom_become_method

#### Default value

```YAML
filebeat_custom_become_method: sudo
```

### filebeat_custom_dirs

#### Default value

```YAML
filebeat_custom_dirs:
  - path: '{{ filebeat_log_dir }}'
    state: directory
    owner: '{{ filebeat_owner }}'
    group: '{{ filebeat_group }}'
    mode: '0750'
  - path: '{{ filebeat_input_dir }}'
    state: directory
    owner: '{{ filebeat_owner }}'
    group: '{{ filebeat_group }}'
    mode: '0750'
```

### filebeat_custom_templates

#### Default value

```YAML
filebeat_custom_templates:
  - src: filebeat.yml.j2
    dest: /etc/filebeat/filebeat.yml
    owner: '{{ filebeat_owner }}'
    group: '{{ filebeat_group }}'
    mode: '0640'
```

### filebeat_deb

#### Default value

```YAML
filebeat_deb:
  - https://artifacts.elastic.co/packages/8.x/apt stable main
```

### filebeat_filesyste_vg_name

#### Default value

```YAML
filebeat_filesyste_vg_name: olympus
```

### filebeat_filesystem_list

#### Default value

```YAML
filebeat_filesystem_list:
  - lv: lv_filebeat_log
    vg: '{{ filebeat_filesyste_vg_name }}'
    size: 1g
    path: '{{ filebeat_log_dir }}'
    owner: '{{ filebeat_owner }}'
    group: '{{ filebeat_group }}'
    mode: '0750'
```

### filebeat_gpg_key

#### Default value

```YAML
filebeat_gpg_key:
  - https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

### filebeat_group

#### Default value

```YAML
filebeat_group: root
```

### filebeat_input_dir

#### Default value

```YAML
filebeat_input_dir: /etc/filebeat/inputs.d
```

### filebeat_input_templates

#### Default value

```YAML
filebeat_input_templates: []
```

### filebeat_install_mode

#### Default value

```YAML
filebeat_install_mode: latest
```

### filebeat_log_dir

#### Default value

```YAML
filebeat_log_dir: /var/log/filebeat
```

### filebeat_log_path_to_watch

#### Default value

```YAML
filebeat_log_path_to_watch: []
```

### filebeat_module_path

#### Default value

```YAML
filebeat_module_path: /etc/filebeat/modules.d
```

### filebeat_owner

#### Default value

```YAML
filebeat_owner: root
```

### filebeat_password

#### Default value

```YAML
filebeat_password: changeme
```

### filebeat_use_generic_ac

#### Default value

```YAML
filebeat_use_generic_ac: false
```

### filebeat_user

#### Default value

```YAML
filebeat_user: filebeat
```

### filebeat_version

#### Default value

```YAML
filebeat_version: ''
```

### subspace_filebeat_enabled

#### Default value

```YAML
subspace_filebeat_enabled: false
```



## Dependencies


## License

BSD-3-Clause

## Author

Douceur
