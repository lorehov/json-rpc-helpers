#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ""


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['jsonrpc_helpers/tests/']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='json-rpc-validation',
    version='1.0.0',
    packages=find_packages(),

    tests_require=['pytest', 'jsonschema', 'six'],
    install_requires=['jsonschema'],
    test_suite='test_jsonrpcvalid',
    cmdclass={'test': PyTest},
    py_modules=['jsonrpcvalid'],

    # metadata for upload to PyPI
    author='Lev Orekhov',
    author_email='lev.orekhov@gmail.com',
    url='https://github.com/lorehov/json-rpc-validation',
    description='Helpers for validation of JSON-RPC using JSON-SCHEMA',
    long_desccription=read('README.md'),
    keywords='json-rpc json-schema validation',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='MIT',
)
