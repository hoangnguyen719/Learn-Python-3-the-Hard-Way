try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'projectname',
    'description': 'This package is copied from ex43_owned and meant for ex46 - LP3THW',
    'version': '0.1',
    'packages': ['PythonJungle'],
    'author': 'Hoang Nguyen',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'install_requires': ['nose'],
    'scripts': []
}

setup(**config)