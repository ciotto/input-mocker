#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
import os

__version__ = '0.1.4'

github_url = 'https://github.com/ciotto'
package_name = 'input-mocker'
package_path = os.path.abspath(os.path.dirname(__file__))
long_description_file_path = os.path.join(package_path, 'README.md')
long_description = ''
try:
    with open(long_description_file_path) as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name=package_name,
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    version=__version__,
    description='input-mocker is simple and easy-to-use tool for mocking of prompt functions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ciotto',
    author_email='info@ci8.it',
    url='%s/%s' % (github_url, package_name, ),
    download_url='%s/%s/archive/v%s.tar.gz' % (github_url, package_name, __version__, ),
    keywords=['tests', 'prompt', 'input', 'raw_input', 'mock'],
    install_requires=[
        'timeout-decorator >= 0.4, < 1.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
    ],
    license='MIT',
    test_suite='tests'
)
