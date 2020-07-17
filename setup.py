#!/usr/bin/env python

from setuptools import setup

setup(
    name='Tinyquery',
    version='1.2',
    description='In-memory test stub for bigquery',
    author='Khan Academy',
    author_email='opensource+pypi@khanacademy.org',
    url='https://github.com/Khan/tinyquery',
    keywords=['bigquery'],
    packages=['tinyquery'],
    install_requires=['arrow', 'ply', 'six'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
