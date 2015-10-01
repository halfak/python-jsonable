import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(fname):
    for line in open(os.path.join(os.path.dirname(__file__), fname)):
        yield line.strip()


setup(
    name="jsonable",
    version="0.3.1",
    author="Aaron Halfaker",
    author_email="ahalfaker@wikimedia.org",
    description=("An abstract class that supports json" +\
                 "serialization/deserialization."),
    license="MIT",
    url="https://github.com/halfak/JSONable-data-types",
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
