# filesystem

this role simply create filesystem on linux

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [filesystem_disk_mounts](#filesystem_disk_mounts)
  - [filesystem_lvs_mounts](#filesystem_lvs_mounts)
  - [filesystem_mountpoint_group](#filesystem_mountpoint_group)
  - [filesystem_mountpoint_mode](#filesystem_mountpoint_mode)
  - [filesystem_mountpoint_user](#filesystem_mountpoint_user)
  - [filesystem_mounts](#filesystem_mounts)
  - [filesystem_nfs_mounts](#filesystem_nfs_mounts)
  - [filesystem_vgs_to_create](#filesystem_vgs_to_create)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### filesystem_disk_mounts

#### Default value

```YAML
filesystem_disk_mounts: []
```

### filesystem_lvs_mounts

#### Default value

```YAML
filesystem_lvs_mounts: []
```

### filesystem_mountpoint_group

#### Default value

```YAML
filesystem_mountpoint_group: root
```

### filesystem_mountpoint_mode

#### Default value

```YAML
filesystem_mountpoint_mode: '0750'
```

### filesystem_mountpoint_user

#### Default value

```YAML
filesystem_mountpoint_user: root
```

### filesystem_mounts

#### Default value

```YAML
filesystem_mounts: '{{ filesystem_lvs_mounts | union(filesystem_nfs_mounts) | union(filesystem_disk_mounts)
  }}'
```

### filesystem_nfs_mounts

#### Default value

```YAML
filesystem_nfs_mounts: []
```

### filesystem_vgs_to_create

#### Default value

```YAML
filesystem_vgs_to_create: []
```



## Dependencies

None.

## License

BSD-3-Clause

## Author

Douceur
