
from setuptools import setup, find_packages
import sys, os

setup(name='rodeo',
    version='0.9.1',
    description="Rodeo Templates",
    long_description="Rodeo Templates",
    classifiers=[], 
    keywords='',
    author='BJ Dierkes',
    author_email='derks@bjdierkes.com',
    url='http://github.com/derks/rodeo',
    license='BSD-3-Clause',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        'pystache',
        'blessings',
        ],
    setup_requires=[],
    entry_points="""
    """,
    namespace_packages=[],
    )
