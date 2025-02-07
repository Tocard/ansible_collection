# nfs_server

this role simply install & configure nfs-server

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [nfs_server_custom_dirs](#nfs_server_custom_dirs)
  - [nfs_server_exports](#nfs_server_exports)
  - [nfs_server_group](#nfs_server_group)
  - [nfs_server_groups](#nfs_server_groups)
  - [nfs_server_packages](#nfs_server_packages)
  - [nfs_server_templates](#nfs_server_templates)
  - [nfs_server_user](#nfs_server_user)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### nfs_server_custom_dirs

#### Default value

```YAML
nfs_server_custom_dirs:
  - path: /run/nfs_server
    mode: '0750'
  - path: /etc/nfs_server/ssl
    mode: '0750'
```

### nfs_server_exports

#### Default value

```YAML
nfs_server_exports:
  - path: /mnt/sdb
    disk: sdb
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sdc
    disk: sdc
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sdd
    disk: sdd
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sde
    disk: sde
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sdf
    disk: sdf
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sdg
    disk: sdg
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sdh
    disk: sdh
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sdi
    disk: sdi
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sdj
    disk: sdj
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
  - path: /mnt/sdk
    disk: sdk
    clients: 192.168.1.0/24(rw,sync,no_root_squash)
    options: async,no_subtree_check
```

### nfs_server_group

#### Default value

```YAML
nfs_server_group: nfs_server
```

### nfs_server_groups

#### Default value

```YAML
nfs_server_groups: []
```

### nfs_server_packages

#### Default value

```YAML
nfs_server_packages:
  - nfs-kernel-server
```

### nfs_server_templates

#### Default value

```YAML
nfs_server_templates:
  - src: exports.j2
    dest: /etc/exports
    mode: '0644'
```

### nfs_server_user

#### Default value

```YAML
nfs_server_user: nfs_server
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
