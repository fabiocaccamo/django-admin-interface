|Build Status| |codecov| |Code Health| |PyPI version| |PyPI downloads| |Py versions| |License|

django-admin-interface
======================

django-admin-interface is a modern **responsive flat admin interface
customizable by the admin itself**.

|django-admin-interface_preview|
---------------------------------

Features
--------

- Beautiful default **django-theme**
- Themes management and customization *(you can customize admin title, logo and colors)*
- Responsive
- List filter dropdown *(optional)*
- ``NEW`` **Related modal** (instead of the old popup window, optional)
- ``NEW`` **Enviroment label** (development, testing, staging, production)
- Style optimizations for:
  - `django-ckeditor`
  - `django-modeltranslation`
  - `django-tabbed-admin`
  - `sorl-thumbnail`

Requirements
------------

- Python 2.7, 3.4, 3.5, 3.6, 3.7
- Django 1.7, 1.8, 1.9, 1.10, 1.11, 2.0, 2.1

Installation
------------

- Run ``pip install django-admin-interface``
- Add ``admin_interface``, ``flat_responsive`` *(only if django version < 2.0)*, ``flat`` *(only if django version < 1.9)* and ``colorfield`` to ``settings.INSTALLED_APPS`` **before** ``django.contrib.admin``
- Run ``python manage.py migrate``
- Run ``python manage.py collectstatic``
- Restart your application server

Upgrade
^^^^^^^

- Run ``pip install django-admin-interface --upgrade``
- Run ``python manage.py migrate`` *(add* ``--fake-initial`` *if you are upgrading from 0.1.0 version)*
- Run ``python manage.py collectstatic --clear``
- Restart your application server

Optional themes
^^^^^^^^^^^^^^^

This package ships with optional themes as fixtures, they can be
installed using the ``loaddata`` admin command.
Optional themes are activated on installation.

**Django theme** (default):

Run ``python manage.py loaddata admin_interface_theme_django.json``

**Bootstrap theme**:

Run ``python manage.py loaddata admin_interface_theme_bootstrap.json``

**Foundation theme**:

Run ``python manage.py loaddata admin_interface_theme_foundation.json``

**U.S. Web Design Standards theme**:

Run ``python manage.py loaddata admin_interface_theme_uswds.json``

Add more themes
^^^^^^^^^^^^^^^

You can add a theme you've created through the admin to this repository
by **sending us a PR**. Here are the steps to follow to add:

1. Export your exact theme as fixture using the ``dumpdata`` admin command:
``python manage.py dumpdata admin_interface.Theme --indent 4 -o admin_interface_theme_{{name}}.json --pks=N``

2. Copy the generated json file into the fixtures folder *(making sure
its name starts with ``admin_interface_theme_`` to avoid clashes with
fixtures that might be provided by other third party apps)*.

3. Remove the ``pk`` from the fixture and make sure the ``active``
field is set to ``true`` *(in this way a theme is automatically
activated when installed)*.

4. Edit the section above to document your theme.

Screenshots
-----------

Admin login


|django-admin-interface_login|
-------------------------------

Admin dashboard


|django-admin-interface_dashboard|
-----------------------------------

Admin themes management


|django-admin-interface_themes_management|
--------------------------------------------

Admin theme customization


|django-admin-interface_theme_customization|
---------------------------------------------

FAQ
---

**I already have a custom** ``base_site.html`` **, how can I make it work?**

You can use ``django-apptemplates`, then add ``{% extends "admin_interface:admin/base_site.html" %}`` to your ``base_site.html``

License
-------

Released under **MIT License**.


.. |Build Status| image:: https://travis-ci.org/fabiocaccamo/django-admin-interface.svg?branch=master

.. |codecov| image:: https://codecov.io/gh/fabiocaccamo/django-admin-interface/branch/master/graph/badge.svg

.. |Code Health| image:: https://landscape.io/github/fabiocaccamo/django-admin-interface/master/landscape.svg?style=flat

.. |PyPI version| image:: https://badge.fury.io/py/django-admin-interface.svg

.. |PyPI downloads| image:: https://img.shields.io/pypi/dm/django-admin-interface.svg

.. |Py versions| image:: https://img.shields.io/pypi/pyversions/django-admin-interface.svg

.. |License| image:: https://img.shields.io/pypi/l/django-admin-interface.svg

.. |django-admin-interface_preview| image:: https://user-images.githubusercontent.com/1035294/35631521-64b0cab8-06a4-11e8-8f57-c04fdfbb7e8b.gif

.. |django-admin-interface_login| image:: https://cloud.githubusercontent.com/assets/1035294/11240233/55c8d4ba-8df1-11e5-9568-00fdc987ede8.gif

.. |django-admin-interface_dashboard| image:: https://cloud.githubusercontent.com/assets/1035294/11240239/627c0362-8df1-11e5-81fa-216366a5d8da.gif

.. |django-admin-interface_themes_management| image:: https://cloud.githubusercontent.com/assets/1035294/11240245/6cd1c342-8df1-11e5-928b-f22217474d3d.gif

.. |django-admin-interface_theme_customization| image:: https://cloud.githubusercontent.com/assets/1035294/11240250/7350d942-8df1-11e5-9b28-f2f54c333cdc.gif