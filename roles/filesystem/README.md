# filesystem

this role simply create filesystem on linux

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [filesystem_custom_become_method](#filesystem_custom_become_method)
  - [filesystem_list](#filesystem_list)
  - [filesystem_physical_volumes_list](#filesystem_physical_volumes_list)
  - [filesystem_volume_create_enabled](#filesystem_volume_create_enabled)
  - [filesystem_volume_group_name](#filesystem_volume_group_name)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### filesystem_custom_become_method

#### Default value

```YAML
filesystem_custom_become_method: sudo
```

### filesystem_list

#### Default value

```YAML
filesystem_list: []
```

### filesystem_physical_volumes_list

#### Default value

```YAML
filesystem_physical_volumes_list:
  - /dev/sdb
```

### filesystem_volume_create_enabled

#### Default value

```YAML
filesystem_volume_create_enabled: false
```

### filesystem_volume_group_name

#### Default value

```YAML
filesystem_volume_group_name: appli_vg
```



## Dependencies

None.

## License

BSD-3-Clause

## Author

Douceur
