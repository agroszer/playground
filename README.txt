Playground
===========

To get going:

$ virtualenv -p python2.7 ve
$ ve/bin/pip install --upgrade setuptools==18.1

$ ve/bin/python bootstrap.py --version=2.4.0
$ bin/buildout

When all done, you can

Run pylint:
$ bin/pylint playground

Run the tests:
$ bin/test
