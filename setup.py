#!/usr/bin/env python
from setuptools import setup, find_packages


install_requires = [
    'pyramid',
    'cornice',
    'cliff',
]

setup(
    name='thoth',
    version='0.0.2',
    description='chat bot manager',
    author='xica development team',
    author_email='info@xica.net',
    url='http://xica-inc.com',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'thoth = thoth.app:main',
        ],
        'thoth.commands': [
            'commands = thoth.command.commands:Commands',
            'yo = thoth.command.yo:Yo',
        ],
    }
)
