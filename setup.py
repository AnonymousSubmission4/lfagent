from setuptools import setup, find_packages
from os.path import join, dirname
import sys, os

sys.path.insert(0, os.path.abspath(__file__ + "/.."))
with open(os.path.abspath(__file__ + "/../srccode/__init__.py"), "r") as f:
    for line in f.readlines():
        if "__version__" in line:
            exec(line)
            break

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="srccode",
    version=__version__,
    author="Anon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=required,
    python_requires=">=3.9.16, <3.12",
)
