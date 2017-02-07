#!/usr/bin/env python
from setuptools import find_packages, setup

exec(open('admin_interface/version.py').read())


setup(
    name='django-admin-interface',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    version=__version__,
    description='django-admin-interface is a modern responsive flat admin interface customizable by the admin itself.',
    author='Fabio Caccamo',
    author_email='fabio.caccamo@gmail.com',
    url='https://github.com/fabiocaccamo/django-admin-interface',
    download_url='https://github.com/fabiocaccamo/django-admin-interface/archive/%s.tar.gz' % __version__,
    keywords=['django', 'admin', 'interface', 'responsive', 'flat', 'theme', 'custom', 'ui'],
    install_requires=[
        'django-colorfield==0.1.12',
        'django-flat-theme==1.1.4',
        'django-flat-responsive==1.2.0'
    ],
    classifiers=[]
)

