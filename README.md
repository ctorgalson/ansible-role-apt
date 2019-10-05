# Ansible Role Apt

[![Build Status](https://travis-ci.com/ctorgalson/ansible-role-apt.svg?branch=master)](https://travis-ci.com/ctorgalson/ansible-role-apt)

Desktop-oriented Apt management role for Debian-based systems.

This role is effectively a simple wrapper for Ansible's three main Apt-related
modules, `apt`, `apt_key`, and `apt_repository`. This enables these modules to
be used in playbooks simply by providing variables to the playbook. If your
apt-related requirements involve more than simple key, repository, and package
management (and especially if you need to manage servers or many machines),
you may find one of the other Galaxy roles more suitable.

## Role Variables

| Variable name      | Default value | Description |
|--------------------|---------------|-------------|
| `apt_keys`         | `[]` | A list of apt keys to add, remove, or update. |
| `apt_packages`     | `[]` | A list of apt packages to add, remove, or update. |
| `apt_repositories` | `[]` | A list of apt repositories to add, remove, or update. |

### Available `apt_keys` properties per-item

All properties of Ansible's `apt_key` module are supported for items in the
`apt_keys` list.

### Available `apt_packages` properties per-item

At this time, the following [Apt module](https://docs.ansible.com/ansible/latest/modules/apt_module.html) properties are supported--note that as with using the Apt module directly, some
properties are mutually incompatible when used on the same item (e.g. `name`
and `deb`):

  - `deb`
  - `dpkg_options`
  - `force_apt_get`
  - `install_recommends`
  - `name`
  - `state`

### Available `apt_repositories` properties per-item

All properties of Ansible's `apt_repository` module are supported for items
in the `apt_repositories` list.

## Example Playbook

    ---
    - name: Test playbook to install Vim and Google Chrome.
      hosts: all
      vars:
        apt_packages:
          - name: "google-chrome-stable"
          - name: "vim"
        apt_keys:
          - url: "https://dl-ssl.google.com/linux/linux_signing_key.pub"
            state: "present"
        apt_repositories:
          - repo: "deb http://dl.google.com/linux/chrome/deb/ stable main"
            update_cache: true
            state: "present"
      roles:
        - role: ansible-role-apt

## License

GPLv3

## Author Information

Christopher Torgalson
