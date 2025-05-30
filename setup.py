# coding: utf-8

"""
    icds

     Industrial Corridors Discovery Finder & Discovery Service. This service provides APIs to discover and manage industrial corridors and drone ports. It includes features for authentication, data management, and health checks. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "drone_distcat"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
    "requests>= 2.32.2",
]

setup(
    name=NAME,
    version=VERSION,
    description="icds",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "icds"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
     Industrial Corridors Discovery Finder &amp; Discovery Service. This service provides APIs to discover and manage industrial corridors and drone ports. It includes features for authentication, data management, and health checks. 
    """,  # noqa: E501
    package_data={"drone_distcat": ["py.typed"]},
)
