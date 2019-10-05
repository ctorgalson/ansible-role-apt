import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize('package', [
    'tree',
    'vagrant',
    'vim',
])
def test_package(host, package):
    d = host.run('dpkg -i {}'.format(package))
    c = host.run('command -v {}'.format(package))

    assert 'no packages found matching' not in d.stdout
    assert '/usr/bin/{}'.format(package) in c.stdout
