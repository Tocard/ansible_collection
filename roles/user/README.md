# user

this role simply install user & group to linux os

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [user_changed](#user_changed)
  - [user_expires](#user_expires)
  - [user_group](#user_group)
  - [user_groups](#user_groups)
  - [user_name](#user_name)
  - [user_password](#user_password)
  - [user_shell](#user_shell)
  - [user_system](#user_system)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### user_changed

#### Default value

```YAML
user_changed: false
```

### user_expires

#### Default value

```YAML
user_expires: -1
```

### user_group

#### Default value

```YAML
user_group:
```

### user_groups

#### Default value

```YAML
user_groups:
```

### user_name

#### Default value

```YAML
user_name:
```

### user_password

#### Default value

```YAML
user_password: "{{ lookup('community.general.random_string', min_lower=12, min_upper=12,
  min_special=12, min_numeric=12, length=64) }}"
```

### user_shell

#### Default value

```YAML
user_shell: /bin/bash
```

### user_system

#### Default value

```YAML
user_system: false
```



## Dependencies

None.

## License

BSD-3-Clause

## Author

Douceur
