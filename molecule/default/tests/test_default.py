import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize('id,fingerprint', [
    ('Google Inc. (Linux Packages Signing Authority) '
     '<linux-packages-keymaster@google.com>', 'D38B4796'),
    ('Google, Inc. Linux Package Signing Key '
     '<linux-packages-keymaster@google.com>', '7FAC5991'),
    ('Yarn Packaging <yarn@dan.cx>', '86E50310')
])
def test_apt_key(host, id, fingerprint):
    k = host.run('apt-key adv --fingerprint --list-keys %s', id)

    assert fingerprint in k.stdout


@pytest.mark.parametrize('file,repository', [
    ('dl_google_com_linux_chrome_deb.list',
     'http://dl.google.com/linux/chrome/deb/'),
    ('dl_yarnpkg_com_debian.list',
     'https://dl.yarnpkg.com/debian/')
])
def test_apt_repository(host, file, repository):
    f = host.file('/etc/apt/sources.list.d/{}'.format(file))

    assert f.exists
    assert f.is_file
    assert repository in f.content_string


@pytest.mark.parametrize('package', [
    'google-chrome-stable',
    'tree',
    'vim',
    'yarn',
    'zoom',
])
def test_apt_package(host, package):
    d = host.run('dpkg -l {}'.format(package))
    c = host.run('command -v {}'.format(package))

    assert 'no packages found matching' not in d.stdout
    assert '/usr/bin/{}'.format(package) in c.stdout
