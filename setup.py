#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-html-reporter',
    version='0.0.1',
    author='Prashanth Sams',
    author_email='sams.prashanth@gmail.com',
    maintainer='Prashanth Sams',
    maintainer_email='sams.prashanth@gmail.com',
    license='MIT',
    url='https://github.com/prashanth-sams/pytest-html-reporter',
    description='Generate a static pytest html report',
    long_description=read('README.md'),
    keywords=[
        'pytest', 'py.test', 'html', 'reporter', 'report'
    ],
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'pytest',
    ],
    classifiers=[
        'Framework :: Pytest',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'reporter = pytest_html_reporter.plugin',
        ],
    },
)