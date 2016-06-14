#!/usr/bin/env python

PROJECT = 'pdkutil'

# Change docs/sphinx/conf.py too!
VERSION = '1.0'

from setuptools import setup, find_packages

# try:
#     long_description = open('README.rst', 'rt').read()
# except IOError:
long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Stores files in barbican containers',
    long_description=long_description,

    author='Simona Iuliana Toader',

    # url='https://github.com/dreamhost/cliff',
    # download_url='https://github.com/dreamhost/cliff/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff','python-barbicanclient'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'pdkutil = pdkutil.pdkutil:main'
        ],
        'pdkutil': [
            'store = pdkutil.commands:Store',
            'get = pdkutil.commands:Get',
        ],
    },

    zip_safe=False,
)
