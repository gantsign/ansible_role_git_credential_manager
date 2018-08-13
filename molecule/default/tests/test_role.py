import pytest

import os

import testinfra.utils.ansible_runner

import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('dir_name', [
    'bin',
    'libexec',
    'jre',
])
def test_directories(Command, File, dir_name):
    install_dir_pattern = '/opt/git-credential-manager/[0-9\\.]+$'
    install_dir = Command.check_output('find %s | grep --color=never -E %s',
                                       '/opt/git-credential-manager',
                                       install_dir_pattern)
    dir = File(install_dir)
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'
    assert dir.group == 'root'

    dir = File(install_dir + '/' + dir_name)
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'
    assert dir.group == 'root'


@pytest.mark.parametrize('file_path', [
    'bin/git-credential-manager',
    'jre/bin/java',
])
def test_files(Command, File, file_path):
    install_dir_pattern = '/opt/git-credential-manager/[0-9\\.]+$'
    install_dir = Command.check_output('find %s | grep --color=never -E %s',
                                       '/opt/git-credential-manager',
                                       install_dir_pattern)
    dir = File(install_dir)
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'
    assert dir.group == 'root'

    installed_file = File(install_dir + '/' + file_path)
    assert installed_file.exists
    assert installed_file.is_file
    assert installed_file.user == 'root'
    assert installed_file.group == 'root'


def test_libexec(Command, File):
    file_pattern = ('/opt/git-credential-manager/[0-9\\.]+/libexec/'
                    'git-credential-manager-[0-9\\.]+\\.jar$')
    file_path = Command.check_output('find %s | grep --color=never -E %s',
                                     '/opt/git-credential-manager',
                                     file_pattern)
    installed_file = File(file_path)
    assert installed_file.exists
    assert installed_file.is_file
    assert installed_file.user == 'root'
    assert installed_file.group == 'root'


def test_link(Command, File):
    installed_file = File('/usr/local/bin/git-credential-manager')
    assert installed_file.exists
    assert installed_file.is_symlink
    assert installed_file.user == 'root'
    assert installed_file.group == 'root'


def test_version(Command, File):
    version = Command.check_output('git-credential-manager version')
    pattern = 'Git Credential Manager for Mac and Linux version [0-9\\.]'
    assert re.match(pattern, version)


def test_git_config(Command, File):
    config = Command.check_output('git config --system credential.helper')
    pattern = ("!'?/opt/git-credential-manager/[0-9\\.]+/jre/bin/java'?"
               " -Ddebug=false -Djava.net.useSystemProxies=true"
               " -Xshareclasses:name=git-credential-manager -Xquickstart"
               " -jar '?/opt/git-credential-manager/[0-9\\.]+/libexec/"
               "git-credential-manager-[0-9\\.]+.jar'?")
    assert re.match(pattern, config)
