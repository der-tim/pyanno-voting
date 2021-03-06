import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyAnno",
    version = "0.1a",
    author = "ASPP",
    author_email = "ASPP@kungfu.py",
    description = ("PyAnno"),
    license = "BSD",
    keywords = "pyanno python aspp2015 kungfupython labels voting",
    url = "https://github.com/der-tim/pyanno-voting",
    packages = find_packages(),
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approv3d :: BSD License",
    ],
)
