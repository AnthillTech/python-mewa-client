#! /usr/bin/env python
# Authors: Krzysztof Langner klangner@gmail.com
# LICENSE: BSD3

from distutils.core import setup

setup(
    name="mewa",
    version="0.2-dev",
    description="Client for Mewa server",
    maintainer="Krzysztof Langner",
    maintainer_email="klangner@gmail.com",
    license="BSD3",
    url='https://github.com/AnthillTech/python-mewa-client',
    packages=[
        'mewa',
    ],
    long_description=open('README.md').read(),
)