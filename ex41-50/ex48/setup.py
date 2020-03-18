try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'NAME',
    'description': 'Description',
    'version': '0.1',
    'packages': ['NAME'],
    'author': 'Hoang Nguyen',
    'author_email': 'hoang.m.nguyen719@gmail.com',
    'install_requires': [
        'nose'
        ],
    'scripts': []
}

setup(**config)