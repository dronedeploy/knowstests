#!/usr/bin/env python

from distutils.core import setup

setup(name='knowstests',
      version='1.0',
      description='Test running framework that has facilities for pydevd debugging',
      author='Mike Hughes',
      author_email='mhughes@dronedeploy.com',
      py_modules=['knowstests'],
      requires=['nose', 'pydevd'],
      scripts=['knowstests']
      )
