from setuptools import find_packages
from setuptools import setup

setup(
    name='user_interface',
    version='0.0.0',
    packages=find_packages(
        include=('user_interface', 'user_interface.*')),
)
