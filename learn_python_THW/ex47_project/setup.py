try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'LPTHW ex47',
    'author' : 'Joe Cavarretta',
    'url' : 'www.github/flatironsendurance.com',
    'download_url' : 'www.flatironsendurance.com',
    'author_email' : 'joe@flatironsendurance.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['ex47'],
    'scripts' : [],
    'name' : 'ex47'
}

setup(**config)
