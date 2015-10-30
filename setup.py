"""Package Setup"""
import os
from setuptools import setup, find_packages


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


def find_files(directory):
    """Returns a list of files in a directory tree.

    The names are relative to the directory given as an argument.
    """
    result = []
    idx = len(directory) + 1
    for here, subdirs, files in os.walk(directory):
        for filename in files:
            if not filename.startswith('__init__.py'):
                result.append(os.path.join(here, filename)[idx:])
    return result


setup(
    name="playground",
    version='0.0.1',
    author="ACME, Inc.",
    author_email="agroszer@gmail.com",
    description="Playground",
    long_description="Playground",
    keywords="",
    url="http://github.com",
    license='ZPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=[],
    zip_safe=False,
    extras_require=dict(
        test=[
            'zope.testing',
            'pylint',
        ],
    ),
    entry_points={
    },
    install_requires=[
        'setuptools',
        'z3c.form',
        'z3c.formui',
        'zope.app.publication',
    ],
)
