User
=========

install user on linux

Requirements
------------

'community.general.random_string' only if user_password is not set.

Role Variables
--------------

all variable is kinda simply to understand.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - role: user
      user_name: "{{ vault_user }}"
      user_group: "{{ vault_group }}"

License
-------

BSD

