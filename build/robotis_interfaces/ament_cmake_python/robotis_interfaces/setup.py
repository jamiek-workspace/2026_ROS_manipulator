from setuptools import find_packages
from setuptools import setup

setup(
    name='robotis_interfaces',
    version='1.1.0',
    packages=find_packages(
        include=('robotis_interfaces', 'robotis_interfaces.*')),
)
