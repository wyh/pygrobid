#!/usr/bin/env python
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pygrobid",
    version="0.1.6",
    author="Samuel.Wu",
    author_email="samuel.yh.wu@gmail.com",
    description="A python client for Grobid service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wyh/pygrobid",
    packages=['grobid'],
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license='LICENSE',
    python_requires='>=3.6',
)
