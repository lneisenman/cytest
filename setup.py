#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from distutils.extension import Extension
from Cython.Build import cythonize

import numpy

fubar_files = ['cytest/fubar/fubar.pyx', 'cytest/fubar/hello.c']
snafu_files = ['cytest/snafu/snafu.pyx']
include_dirs = [numpy.get_include()]
ext_modules = [Extension('cytest.fubar.fubar', sources=fubar_files,
                         include_dirs=include_dirs),
               Extension('cytest.snafu.snafu', sources=snafu_files,
                         include_dirs=include_dirs)]

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = ['cython', 'numpy']

setup(
    name='cytest',
    version='0.2.0',
    description="Cython demo package",
    long_description=readme + '\n\n' + history,
    author="Larry Eisenman",
    author_email='leisenman@wustl.edu',
    url='https://github.com/lneisenman/cytest',
    packages=find_packages(exclude=['contrib', 'docs', 'tests','tests.*']),
    package_dir={'cytest':'cytest'},
    package_data={'': ['*.pyx', '*.pxd', '*.h', '*.txt', '*.dat', '*.csv']},
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='cytest',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Cython',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    ext_modules=cythonize(ext_modules),
)