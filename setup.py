import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(fname):
    for line in open(os.path.join(os.path.dirname(__file__), fname)):
        yield line.strip()


setup(
    name="jsonable",
    version=read('VERSION').strip(),
    author="Aaron Halfaker",
    author_email="ahalfaker@wikimedia.org",
    description=("An abstract class that supports json serialization/deserialization."),
    license="MIT",
    url="https://github.com/halfak/JSONable-data-types",
    py_modules=['jsonable'],
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
