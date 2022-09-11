from setuptools import setup, find_packages
import codecs
import os

cwd = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(cwd, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.2"
DESCRIPTION = "For using python to automate tasks in the MaroPost Neto environment"

setup(
    name="netotools",
    version=VERSION,
    author="Dan Hobday",
    author_email="<danhobday@proton.me>",
    url="https://github.com/DPHobday/netotools",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=["tests"]),
    install_requires=["requests"],
    keywords=["python", "neto"],
    classifiers=[
        "Development Status :: Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
