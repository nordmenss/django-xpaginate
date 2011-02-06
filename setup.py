#!/usr/bin/env python
from setuptools import setup, find_packages
from html_blocks import VERSION
path='xpaginate'

setup(name=path,
      version=VERSION,
      description='django paginate',
      long_description = open('README.txt').read(),
      author='NORD',
      author_email='nordmenss@gmail.com',
      url='https://github.com/nordmenss/django-xpaginate',
      packages=find_packages(),
      include_package_data=True,

      classifiers=(
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
        ),
      license="GPL"
     )