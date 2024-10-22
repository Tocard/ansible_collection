# elasticsearch

this role simply install & configure elasticsearch

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [elasticsearch_cluster_users](#elasticsearch_cluster_users)
  - [elasticsearch_custom_become_method](#elasticsearch_custom_become_method)
  - [elasticsearch_custom_roles](#elasticsearch_custom_roles)
  - [elasticsearch_custom_users](#elasticsearch_custom_users)
  - [elasticsearch_deb](#elasticsearch_deb)
  - [elasticsearch_directories](#elasticsearch_directories)
  - [elasticsearch_elastic_current_password](#elasticsearch_elastic_current_password)
  - [elasticsearch_elastic_password](#elasticsearch_elastic_password)
  - [elasticsearch_elastic_user](#elasticsearch_elastic_user)
  - [elasticsearch_exclude_node](#elasticsearch_exclude_node)
  - [elasticsearch_filebeat_password](#elasticsearch_filebeat_password)
  - [elasticsearch_filesystem_disk_mounts](#elasticsearch_filesystem_disk_mounts)
  - [elasticsearch_filesystem_lvs_mounts](#elasticsearch_filesystem_lvs_mounts)
  - [elasticsearch_filesystem_vg_name](#elasticsearch_filesystem_vg_name)
  - [elasticsearch_gpg_key](#elasticsearch_gpg_key)
  - [elasticsearch_grafana_password](#elasticsearch_grafana_password)
  - [elasticsearch_group](#elasticsearch_group)
  - [elasticsearch_groups](#elasticsearch_groups)
  - [elasticsearch_host](#elasticsearch_host)
  - [elasticsearch_http_base_url](#elasticsearch_http_base_url)
  - [elasticsearch_kibana_password](#elasticsearch_kibana_password)
  - [elasticsearch_metricbeat_advanced_password](#elasticsearch_metricbeat_advanced_password)
  - [elasticsearch_metricbeat_password](#elasticsearch_metricbeat_password)
  - [elasticsearch_minotor_password](#elasticsearch_minotor_password)
  - [elasticsearch_mozquito_password](#elasticsearch_mozquito_password)
  - [elasticsearch_other_nodes](#elasticsearch_other_nodes)
  - [elasticsearch_packages](#elasticsearch_packages)
  - [elasticsearch_packetbeat_password](#elasticsearch_packetbeat_password)
  - [elasticsearch_path_bin](#elasticsearch_path_bin)
  - [elasticsearch_path_config](#elasticsearch_path_config)
  - [elasticsearch_path_data](#elasticsearch_path_data)
  - [elasticsearch_path_logs](#elasticsearch_path_logs)
  - [elasticsearch_port](#elasticsearch_port)
  - [elasticsearch_ssl_file](#elasticsearch_ssl_file)
  - [elasticsearch_ssl_path](#elasticsearch_ssl_path)
  - [elasticsearch_templates](#elasticsearch_templates)
  - [elasticsearch_unicast_hosts](#elasticsearch_unicast_hosts)
  - [elasticsearch_url_license](#elasticsearch_url_license)
  - [elasticsearch_url_security](#elasticsearch_url_security)
  - [elasticsearch_user](#elasticsearch_user)
  - [elasticsearch_version](#elasticsearch_version)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.9`

## Default Variables

### elasticsearch_cluster_users

#### Default value

```YAML
elasticsearch_cluster_users:
  - name: kibana_system
    password: '{{ elasticsearch_kibana_password }}'
  - name: elastic
    password: '{{ elasticsearch_elastic_password }}'
```

### elasticsearch_custom_become_method

#### Default value

```YAML
elasticsearch_custom_become_method: sudo
```

### elasticsearch_custom_roles

#### Default value

```YAML
elasticsearch_custom_roles:
  - name: metricbeat_olympus
    cluster_settings: [manage_index_templates, monitor, manage_ilm]
    indices:
      - names: [metricbeat*, .monitoring*, .ds-.monitoring-*]
        privileges: [write, create_index, manage, view_index_metadata]
  - name: metricbeat
    cluster_settings: [manage_index_templates, monitor, manage_ilm]
    indices:
      - names: [metricbeat*]
        privileges: [write, create_index, manage, view_index_metadata]
  - name: grafana
    cluster_settings: []
    indices:
      - names: [flux-*, cosmos-*, defi-*, minotor-*, metricbeat*, .monitoring-*, osmosis-*]
        privileges: [read, monitor, view_index_metadata]
```

### elasticsearch_custom_users

#### Default value

```YAML
elasticsearch_custom_users:
  - name: grafana
    password: '{{ elasticsearch_grafana_password }}'
    roles: [grafana_role]
    full_name: grafana user from olympus
```

### elasticsearch_deb

#### Default value

```YAML
elasticsearch_deb:
  - https://artifacts.elastic.co/packages/8.x/apt stable main
```

### elasticsearch_directories

#### Default value

```YAML
elasticsearch_directories:
  - path: '{{ elasticsearch_ssl_path }}'
```

### elasticsearch_elastic_current_password

#### Default value

```YAML
elasticsearch_elastic_current_password:
```

### elasticsearch_elastic_password

#### Default value

```YAML
elasticsearch_elastic_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/elastic:moz ' ~ hashi_connect) }}"
```

### elasticsearch_elastic_user

#### Default value

```YAML
elasticsearch_elastic_user: elastic
```

### elasticsearch_exclude_node

#### Default value

```YAML
elasticsearch_exclude_node:
  - '{{ ansible_host }}'
```

### elasticsearch_filebeat_password

#### Default value

```YAML
elasticsearch_filebeat_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/filebeat:moz ' ~ hashi_connect) }}"
```

### elasticsearch_filesystem_disk_mounts

#### Default value

```YAML
elasticsearch_filesystem_disk_mounts:
  - disk: sdb
    path: '{{ elasticsearch_path_data }}'
    owner: '{{ elasticsearch_user }}'
    group: '{{ elasticsearch_user }}'
```

### elasticsearch_filesystem_lvs_mounts

#### Default value

```YAML
elasticsearch_filesystem_lvs_mounts:
  - lv: lv_es_log
    vg: '{{ elasticsearch_filesystem_vg_name }}'
    size: 1g
    path: '{{ elasticsearch_path_logs }}'
    owner: '{{ elasticsearch_user }}'
    group: '{{ elasticsearch_user }}'
```

### elasticsearch_filesystem_vg_name

#### Default value

```YAML
elasticsearch_filesystem_vg_name: olympus
```

### elasticsearch_gpg_key

#### Default value

```YAML
elasticsearch_gpg_key:
  - https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

### elasticsearch_grafana_password

#### Default value

```YAML
elasticsearch_grafana_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/grafana:moz ' ~ hashi_connect) }}"
```

### elasticsearch_group

#### Default value

```YAML
elasticsearch_group: elasticsearch
```

### elasticsearch_groups

#### Default value

```YAML
elasticsearch_groups: [certbot]
```

### elasticsearch_host

#### Default value

```YAML
elasticsearch_host: '{{ ansible_host }}'
```

### elasticsearch_http_base_url

#### Default value

```YAML
elasticsearch_http_base_url: https://{{ elasticsearch_host }}:{{ elasticsearch_port
  }}
```

### elasticsearch_kibana_password

#### Default value

```YAML
elasticsearch_kibana_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/kibana:moz ' ~ hashi_connect) }}"
```

### elasticsearch_metricbeat_advanced_password

#### Default value

```YAML
elasticsearch_metricbeat_advanced_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/metricbeat-advanced:moz ' ~ hashi_connect) }}"
```

### elasticsearch_metricbeat_password

#### Default value

```YAML
elasticsearch_metricbeat_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/metricbeat:moz ' ~ hashi_connect) }}"
```

### elasticsearch_minotor_password

#### Default value

```YAML
elasticsearch_minotor_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/minotor:moz ' ~ hashi_connect) }}"
```

### elasticsearch_mozquito_password

#### Default value

```YAML
elasticsearch_mozquito_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/mozquito:moz ' ~ hashi_connect) }}"
```

### elasticsearch_other_nodes

#### Default value

```YAML
elasticsearch_other_nodes: '{{ elasticsearch_unicast_hosts | difference(elasticsearch_exclude_node)
  }}'
```

### elasticsearch_packages

#### Default value

```YAML
elasticsearch_packages:
  - elasticsearch={{ elasticsearch_version }}
```

### elasticsearch_packetbeat_password

#### Default value

```YAML
elasticsearch_packetbeat_password: "{{ lookup('hashi_vault', hashi_elasticsearch_path
  ~ '/packetbeat:moz ' ~ hashi_connect) }}"
```

### elasticsearch_path_bin

#### Default value

```YAML
elasticsearch_path_bin: /usr/share/elasticsearch
```

### elasticsearch_path_config

#### Default value

```YAML
elasticsearch_path_config: /etc/elasticsearch
```

### elasticsearch_path_data

#### Default value

```YAML
elasticsearch_path_data: /var/lib/elasticsearch
```

### elasticsearch_path_logs

#### Default value

```YAML
elasticsearch_path_logs: /var/log/elasticsearch
```

### elasticsearch_port

#### Default value

```YAML
elasticsearch_port: 9200
```

### elasticsearch_ssl_file

#### Default value

```YAML
elasticsearch_ssl_file:
  - src: /opt/certbot/eden/cert.pem
    dest: '{{ elasticsearch_ssl_path }}/cert.pem'
    user: elasticsearch
  - src: /opt/certbot/eden/chain.pem
    dest: '{{ elasticsearch_ssl_path }}/chain.pem'
    user: elasticsearch
  - src: /opt/certbot/eden/fullchain.pem
    dest: '{{ elasticsearch_ssl_path }}/fullchain.pem'
    user: elasticsearch
  - src: /opt/certbot/eden/fullchain.pem.key
    dest: '{{ elasticsearch_ssl_path }}/fullchain.pem.key'
    user: elasticsearch
```

### elasticsearch_ssl_path

#### Default value

```YAML
elasticsearch_ssl_path: '{{ elasticsearch_path_config }}/ssl'
```

### elasticsearch_templates

#### Default value

```YAML
elasticsearch_templates:
  - src: elasticsearch.yml.j2
    dest: '{{ elasticsearch_path_config }}/elasticsearch.yml'
```

### elasticsearch_unicast_hosts

#### Default value

```YAML
elasticsearch_unicast_hosts: "{{ groups['elasticsearch'] | map('extract', hostvars,
  ['ansible_host']) | list }}"
```

### elasticsearch_url_license

#### Default value

```YAML
elasticsearch_url_license: '{{ elasticsearch_http_base_url }}/_license'
```

### elasticsearch_url_security

#### Default value

```YAML
elasticsearch_url_security: '{{ elasticsearch_http_base_url }}/_security'
```

### elasticsearch_user

#### Default value

```YAML
elasticsearch_user: elasticsearch
```

### elasticsearch_version

#### Default value

```YAML
elasticsearch_version: 8.13.4
```



## Dependencies

- tocard.utils.user
- tocard.utils.filesystem

## License

BSD-3-Clause

## Author

Douceur
