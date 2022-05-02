Ansible Role: Git Credential Manager
====================================

[![Tests](https://github.com/gantsign/ansible_role_git_credential_manager/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_git_credential_manager/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.git__credential__manager-blue.svg)](https://galaxy.ansible.com/gantsign/git_credential_manager)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_git_credential_manager/master/LICENSE)

Role to install the [Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager).

**Important:** while the Git Credential Manager works on macOS and Windows this
Ansible role only works on Debian and Ubuntu.

Requirements
------------

* Ansible >= 2.9

* Linux Distribution

    * Debian Family

        * Debian

            * Buster (10)
            * Bullseye (11)

        * Ubuntu

            * Focal (20.04)
            * Jammy (22.04)

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# Git Credential Manager version number
git_credential_manager_version: '2.0.696'

# The SHA256 of the Git Credential Manager JAR
git_credential_manager_redis_sha256sum: 'caba73101f80c1a789225730d0d1b82941c31707cef6a55fb3cb3caada68d234'

# The credential store to use
git_credential_manager_credential_store: 'secretservice'

# Directory to store files downloaded for the Git Credential Manager
git_credential_manager_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.git_credential_manager
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
