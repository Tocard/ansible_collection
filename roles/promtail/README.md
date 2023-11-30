Promtail
=========

Install promtail on linux

Requirements
------------

None

Role Variables
--------------

```yaml
scrape_configs:
{% if promtail_chia_enabled | default(false) %}
{% include './subconfig/chia.j2' %}
{% endif %}
{% if promtail_streamr_enabled | default(false) %}
{% include './subconfig/streamr.j2' %}
{% endif %}
{% if promtail_subspace_enabled | default(false) %}
{% include './subconfig/subspace.j2' %}
{% endif %}
{% if promtail_babylon_enabled | default(false) %}
{% include './subconfig/babylon.j2' %}
{% endif %}
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
---
#==================================================================
# Promtail
#==================================================================
- hosts: promtail
  roles:
    - role: tocard.utils.user
      user_name: "{{ promtail_owner }}"
      user_group: "{{ promtail_group }}"
      tags:
        - promtail
    - role: promtail
      tags:
        - promtail

```

License
-------

BSD

