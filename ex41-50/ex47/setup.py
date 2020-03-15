try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'PythonJungle',
    'description': 'This is exercise 47 from Learn Python 3 The Hard Way - Shaw',
    'version': '0.1',
    'packages': ['ex47'],
    'author': 'Hoang Nguyen',
    'author_email': 'hoang.m.nguyen719@gmail.com',
    'install_requires': [
        'nose'
        ],
    'scripts': []
}

setup(**config)