#!/usr/bin/env python

from setuptools import find_packages, setup

exec(open('admin_interface/version.py').read())

setup(
    name='django-admin-interface',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    version=__version__,
    description='django-admin-interface is a modern responsive flat admin interface customizable by the admin itself.',
    author='Fabio Caccamo',
    author_email='fabio.caccamo@gmail.com',
    url='https://github.com/fabiocaccamo/django-admin-interface',
    download_url='https://github.com/fabiocaccamo/django-admin-interface/archive/%s.tar.gz' % __version__,
    keywords=['django', 'admin', 'interface', 'responsive', 'flat', 'theme', 'custom', 'ui'],
    requires=['django(>=1.7)'],
    install_requires=[
        'django-colorfield>=0.1,<1.0',
        'django-flat-theme>=1.0,<2.0',
        'django-flat-responsive>=1.0,<2.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Build Tools',
    ],
    license='MIT',
    test_suite='runtests.runtests'
)

