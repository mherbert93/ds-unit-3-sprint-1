
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-mherbert93", # the name that you will install via pip
    version="1.2",
    author="Martin Herbert",
    author_email="martinherbert93@gmail.com",
    description="Test package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/mherbert93/ds-unit-3-sprint-1",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)