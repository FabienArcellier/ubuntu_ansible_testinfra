#!/usr/bin/env python

import os
import subprocess
import sys

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
ROOT_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..'))

def main(arguments):
    os.chdir(SCRIPT_DIR + '/..')
    tests_environment = [
        ('Dockerfile.ubuntu1804', 'ubuntu1804_ansible_testinfra'),
        ('Dockerfile.ubuntu1604', 'ubuntu1604_ansible_testinfra'),
        # ('Dockerfile.ubuntu1404', 'ubuntu1404_ansible_testinfra'),
    ]

    for (dockerfile, image) in tests_environment:
        print(subprocess.check_output('docker build -t {0} -f {1} .'.format(image, dockerfile), shell=True))
        print(subprocess.check_output('docker run -v "{0}":/mnt {1} py.test /mnt/tests/test_dockerfile.py'.format(ROOT_DIR, image), shell=True))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))