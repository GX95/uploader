#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='upload',
    version='1.0',
    py_modules=['upload'],
    install_requires=[
        'requests',
    ],
    entry_points='''
        [console_scripts]
        upload=upload:main
    '''
)
