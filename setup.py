#!/usr/bin/env python
from distutils.core import setup
from html_blocks import VERSION
path='xpaginate'

setup(name=path,
      version=VERSION,
      description='django paginate',
      long_description = open('README.txt').read(),
      author='NORD',
      author_email='nordmenss@gmail.com',
      url='https://github.com/nordmenss/django-xpaginate',
      packages=[ path,],

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