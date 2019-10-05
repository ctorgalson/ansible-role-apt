# Role Name

Desktop-oriented Apt management role for Debian-based systems.

## Requirements

No special requirements.

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

At this time, the following properties are suppored--note that as with using
Ansible's Apt module directly, some properties cannot be used at the same time
for the same item (e.g. `name` and `deb`):

  - deb
  - dpkg_options
  - force_apt_get
  - install_recommends
  - name
  - state

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

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
