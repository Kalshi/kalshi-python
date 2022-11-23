# coding: utf-8

"""
    Kalshi Trade API

    This documentation describes Kalshi's trading API (known as Trade API v2). By using this API, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@kalshi.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "kalshi_python"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Kalshi Trade API",
    author_email="support@kalshi.com",
    url="",
    keywords=["Swagger", "Kalshi Trade API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    #kalshi-python
    
    This library is the official python SDK for algorithmic trading on [Kalshi](https://kalshi.com). 
    
    This SDK is powered by Kalshi's trading rest api v2. The documentation for the underlying api [can be found here](https://trading-api.readme.io). 
    
    By using this SDK, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).
    """
)