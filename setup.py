#!/usr/bin/env python

from distutils.core import setup

setup(name='tftpy',
      version='0.4.3',
      description='Python TFTP library',
      author='Michael P. Soulier',
      author_email='msoulier@digitaltorque.ca',
      url='http://digitaltorque.ca',
      packages=['tftpy'],
      scripts=['bin/tftpy_client.py','bin/tftpy_server.py'],
      classifiers=[
        'Development Status :: Alpha',
        'License :: OSI Approved :: CNRI Python License',
        'Topic :: Networking :: TFTP',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Environment :: Console',
        ]
      )
