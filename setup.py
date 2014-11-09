#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="osi-licenses-full",
    version=version,
    description=("A python utility for downloading all OSI approved licenses "
        "in markdown format"),
    classifiers=[],
    keywords="osi foss markdown license",
    author="Liam Middlebrook",
    author_email="liammiddlebrook@gmail.com",
    url="https://github.com/liam-middlebrook/osi-licenses-full",
    license="MIT",
    packages=find_packages(
    ),
    scripts=[
        "distribute_setup.py",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "",
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)