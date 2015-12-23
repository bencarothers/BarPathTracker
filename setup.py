#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='trackr',
      version='0.0.1',
      long_description=open('README.md').read(),
      authors=['Ben Carothers', 'Shane Caldwell'],
      author_email='benjamin.carothers13@ncf.edu',
      url='https://github.com/bencarothers/trackr',
      packages=['server', 'server.tests'],
      test_suite="server.tests",
      install_requires=[
            'coverage>=3.3',
            'nose>=1.0',
            'flask==0.10.1',
            'flask-restful==0.3.5',
            'Jinja2==2.7.3',
            'MarkupSafe==0.23',
            'Werkzeug==0.9.6',
            'itsdangerous==0.24',
            'requests==2.4.1',
            'wsgiref==0.1.2',
            'cv2==1.0',
            'mongoengine==0.10.5',
            'flask-mongoengine==0.7.4',
            'Flask-SuperAdmin==1.7.1',
            # 'matplotlib==1.5.0'
          ],
      )
