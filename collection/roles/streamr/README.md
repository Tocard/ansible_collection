StreamR Node
=========

Install StreamR on linux

Requirements
------------

None

Role Variables
--------------

```yaml
```

Dependencies
------------
```yml
dependencies:
  - name: community.general
    src: https://github.com/ansible-collections/community.general.git
    version: "main"
    scm: git
  - name: tocard.utils.user
  - name: tocard.utils.filesystem
  - name: morgangraphics.nvm
    src: https://github.com/morgangraphics/ansible-role-nvm.git
    version: "v1.5.2"
    scm: git
```

Example Playbook
----------------

```yaml
---

#==================================================================
# Streamr
#==================================================================

- hosts: streamr
  roles:
    - role: tocard.utils.user.streamr
      tags:
        - streamr

```

License
-------

BSD

