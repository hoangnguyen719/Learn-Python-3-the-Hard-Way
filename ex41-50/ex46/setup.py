try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'PythonJungle',
    'description': 'This package is copied from ex43_owned and meant for ex46 - LP3THW',
    'version': '0.1',
    'packages': ['PythonJungle'],
    'author': 'Hoang Nguyen',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'hoang.m.nguyen719@gmail.com',
    'install_requires': [
        'nose'
        ],
    'scripts': []
}

setup(**config)