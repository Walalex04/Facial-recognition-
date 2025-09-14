

from setuptools import setup, find_packages

setup(
    name="facial_recognition",
    version="0.1",
    package=find_packages(include=['recognition*']),
    exclude_packages=['notebooks*']
)