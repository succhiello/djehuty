#!/usr/bin/env python
from setuptools import setup, find_packages


install_requires = [
    'pyramid==1.5.1',
    'cornice==0.16.2',
    'cliff==1.6.1',
]

setup(
    name='thoth',
    version='0.0.2',
    description='chat bot manager',
    author='xica development team',
    author_email='info@xica.net',
    url='https://github.com/xica/thoth',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
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
