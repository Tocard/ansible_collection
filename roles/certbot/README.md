# certbot

this role configure certbot on server and create script to auto renew cert

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [certbot_clean_previous_install](#certbot_clean_previous_install)
  - [certbot_cred_path](#certbot_cred_path)
  - [certbot_credential_dns_ovh_application_key](#certbot_credential_dns_ovh_application_key)
  - [certbot_credential_dns_ovh_application_secret](#certbot_credential_dns_ovh_application_secret)
  - [certbot_credential_dns_ovh_consumer_key](#certbot_credential_dns_ovh_consumer_key)
  - [certbot_credential_dns_ovh_endpoint](#certbot_credential_dns_ovh_endpoint)
  - [certbot_custom_become_method](#certbot_custom_become_method)
  - [certbot_directories](#certbot_directories)
  - [certbot_domain_to_claim](#certbot_domain_to_claim)
  - [certbot_email_contact](#certbot_email_contact)
  - [certbot_final_name_pattern](#certbot_final_name_pattern)
  - [certbot_force_renew](#certbot_force_renew)
  - [certbot_group](#certbot_group)
  - [certbot_home](#certbot_home)
  - [certbot_main_domain](#certbot_main_domain)
  - [certbot_owner](#certbot_owner)
  - [certbot_package](#certbot_package)
  - [certbot_templates](#certbot_templates)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### certbot_clean_previous_install

#### Default value

```YAML
certbot_clean_previous_install: false
```

### certbot_cred_path

#### Default value

```YAML
certbot_cred_path: '{{ certbot_home }}/certbot.cred'
```

### certbot_credential_dns_ovh_application_key

#### Default value

```YAML
certbot_credential_dns_ovh_application_key: "{{ lookup('hashi_vault', hashi_certbot_path
  ~ '/ovh:dns_ovh_application_key ' ~ hashi_connect) }}"
```

### certbot_credential_dns_ovh_application_secret

#### Default value

```YAML
certbot_credential_dns_ovh_application_secret: "{{ lookup('hashi_vault', hashi_certbot_path
  ~ '/ovh:dns_ovh_application_secret ' ~ hashi_connect) }}"
```

### certbot_credential_dns_ovh_consumer_key

#### Default value

```YAML
certbot_credential_dns_ovh_consumer_key: "{{ lookup('hashi_vault', hashi_certbot_path
  ~ '/ovh:dns_ovh_consumer_key ' ~ hashi_connect) }}"
```

### certbot_credential_dns_ovh_endpoint

#### Default value

```YAML
certbot_credential_dns_ovh_endpoint: "{{ lookup('hashi_vault', hashi_certbot_path
  ~ '/ovh:dns_ovh_endpoint ' ~ hashi_connect) }}"
```

### certbot_custom_become_method

#### Default value

```YAML
certbot_custom_become_method: sudo
```

### certbot_directories

#### Default value

```YAML
certbot_directories:
  - path: '{{ certbot_home }}'
  - path: '{{ certbot_home }}/work'
  - path: '{{ certbot_home }}/config'
  - path: '{{ certbot_home }}/log'
  - path: '{{ certbot_home }}/eden'
  - path: /etc/letsencrypt
    recurse: true
```

### certbot_domain_to_claim

#### Default value

```YAML
certbot_domain_to_claim:
  - '{{ certbot_main_domain }}'
```

### certbot_email_contact

#### Default value

```YAML
certbot_email_contact: contact@ether-source.fr
```

### certbot_final_name_pattern

#### Default value

```YAML
certbot_final_name_pattern: '{{ ansible_hostname }}'
```

### certbot_force_renew

#### Default value

```YAML
certbot_force_renew: false
```

### certbot_group

#### Default value

```YAML
certbot_group: certbot
```

### certbot_home

#### Default value

```YAML
certbot_home: /opt/certbot
```

### certbot_main_domain

#### Default value

```YAML
certbot_main_domain: '{{ certbot_final_name_pattern }}.mythologic.fr'
```

### certbot_owner

#### Default value

```YAML
certbot_owner: certbot
```

### certbot_package

#### Default value

```YAML
certbot_package:
  - certbot
  - python3-certbot-nginx
  - python3-certbot-dns-ovh
  - cron
  - acl
```

### certbot_templates

#### Default value

```YAML
certbot_templates:
  - src: certbot.sh.j2
    dest: '{{ certbot_home }}/certbot.sh'
  - src: certbot.cred.j2
    dest: '{{ certbot_cred_path }}'
  - src: certbot_eden.sh.j2
    dest: /usr/bin/certbot_eden.sh
    mode: '0770'
```



## Dependencies


## License

BSD-3-Clause

## Author

Douceur
