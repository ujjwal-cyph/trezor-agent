#!/usr/bin/env python
from setuptools import setup

setup(
    name='x1wallet_agent',
    version='0.1.0',
    description='Using X1 Wallet as hardware SSH/GPG agent',
    author='X1 Wallet team',
    author_email='support@cypherock.com',
    url='http://github.com/romanz/trezor-agent',
    scripts=['x1wallet_agent.py'],
    install_requires=[
        'libagent>=0.10.0'
    ],
    platforms=['POSIX'],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Communications',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    entry_points={'console_scripts': [
        'x1wallet-agent = x1wallet_agent:ssh_agent',
        'x1wallet-gpg = x1wallet_agent:gpg_tool',
        'x1wallet-gpg-agent = x1wallet_agent:gpg_agent',
    ]},
)
