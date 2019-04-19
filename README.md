Ansible Role: Git Credential Manager
====================================

[![Build Status](https://travis-ci.com/gantsign/ansible_role_git_credential_manager.svg?branch=master)](https://travis-ci.com/gantsign/ansible_role_git_credential_manager)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.git__credential__manager-blue.svg)](https://galaxy.ansible.com/gantsign/git_credential_manager)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_git_credential_manager/master/LICENSE)

Role to install Microsoft's [Git Credential Manager for Mac and Linux](https://github.com/Microsoft/Git-Credential-Manager-for-Mac-and-Linux).

**Important:** while Microsoft's Git Credential Manager works on macOS this
Ansible role is presently for Linux only.

Requirements
------------

* Ansible >= 2.5

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 7

        * Fedora

            * 28

    * SUSE Family

        * openSUSE

            * 15.0

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# Git Credential Manager version number
git_credential_manager_version: '2.0.4'

# The SHA256 of the Git Credential Manager JAR
git_credential_manager_jar_sha256sum: 'fb8536aac9b00cdf6bdeb0dd152bb1306d88cd3fdb7a958ac9a144bf4017cad7'

# The major version of the JRE
git_credential_manager_jre_major_version: '8'

# The full version of the JRE (from AdoptOpenJDK)
git_credential_manager_jre_version: 'jdk8u212-b03_openj9-0.14.0'

# The SHA256 of the JRE
git_credential_manager_jre_sha256sum: '4aa8fdb3916816788c516423236bef68a05a694cbd44fa14c4f8f5b76891aa4c'

# Base installation directory the Git Credential Manager
git_credential_manager_install_dir: '/opt/git-credential-manager/{{ git_credential_manager_version }}'

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
