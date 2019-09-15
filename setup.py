from distutils.core import setup
setup(
  name = 'Blinder',
  packages = ['Blinder'],
  version = 'v0.1',
  license='GPL V3.0',
  description = 'Blidner is a small python library to automate time-based blind SQL injection by using a pre defined queries as a functions to automate a rapid PoC development.',
  author = 'Askar',
  author_email = 'm.askar@isecur1ty.org',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/mhaskar/Blinder/archive/v0.1.tar.gz',
  keywords = ['SQL injection', 'Pentesting', "AppSec"],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Pentesters',
    'Topic :: Software Development :: Build Tools',
    'License :: GPL V3.0',
    'Programming Language :: Python :: 2.7'
  ],
)
