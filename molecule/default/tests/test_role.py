import re


def test_version(host):
    version = host.check_output('git-credential-manager-core --version')
    pattern = r'[0-9\.]+(\.[0-9\.]+){2}'
    assert re.search(pattern, version)


def test_git_config(host):
    config = host.check_output('git config --system credential.helper')
    assert config == '/usr/local/share/gcm-core/git-credential-manager-core'
    config = host.check_output(
        'git config --system credential.credentialStore')
    assert config == 'secretservice'
