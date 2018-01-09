from setuptools import setup

import sys

setup(
    name='cameraupload-server',
    version='0.2.3',

    description='receives images from cameraupload_full',
    long_description=open("README.md").read(),
    license='WTFPL',
    url='http://localhost/',
    download_url='http://localhost/',

    author='makefu',
    author_email='github.com@syntax-fehler.de',

    packages=['cuserver'],
    entry_points={ },
    install_requires= [ "Flask" ],
    classifiers=[
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
