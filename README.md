[![Build Status](https://travis-ci.org/fabiocaccamo/django-admin-interface.svg?branch=master)](https://travis-ci.org/fabiocaccamo/django-admin-interface)
[![codecov](https://codecov.io/gh/fabiocaccamo/django-admin-interface/branch/master/graph/badge.svg)](https://codecov.io/gh/fabiocaccamo/django-admin-interface)
[![PyPI version](https://badge.fury.io/py/django-admin-interface.svg)](https://badge.fury.io/py/django-admin-interface)
[![Py versions](https://img.shields.io/pypi/pyversions/django-admin-interface.svg)](https://img.shields.io/pypi/pyversions/django-admin-interface.svg)
[![License](https://img.shields.io/pypi/l/django-admin-interface.svg)](https://img.shields.io/pypi/l/django-admin-interface.svg)

# django-admin-interface
django-admin-interface is a modern **responsive flat admin interface customizable by the admin itself**.

## Features
- Beautiful default **django-theme**
- Themes management and customization *(you can **customize admin title, logo and colors**)*
- Responsive
- List filter dropdown *(optional)*
- **`NEW`** **Related modal** *(instead of the old popup window, optional)*
- Style optimizations for: `django-ckeditor`, `django-modeltranslation`, `sorl-thumbnail`

## Requirements
- Python 2.7, 3.4, 3.5, 3.6
- Django 1.7, 1.8, 1.9, 1.10, 1.11

## Installation
- Run `pip install django-admin-interface`
- Add `admin_interface`, `flat_responsive`, `flat` and `colorfield` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    'admin_interface',
    'flat_responsive',
    'flat', #if django version < 1.9
    'colorfield',
    #...
    'django.contrib.admin',
    #...
)
```
- Run ``python manage.py migrate``
- Run ``python manage.py collectstatic``
- Restart your application server

#### Upgrade
- Run `pip install django-admin-interface --upgrade`
- Run ``python manage.py migrate`` *(add ``--fake-initial`` if you are upgrading from 0.1.0 version)*
- Run ``python manage.py collectstatic --clear``
- Restart your application server


## Screenshots
###### Admin login
![django-admin-interface_login](https://cloud.githubusercontent.com/assets/1035294/11240233/55c8d4ba-8df1-11e5-9568-00fdc987ede8.gif)
---
###### Admin dashboard
![django-admin-interface_dashboard](https://cloud.githubusercontent.com/assets/1035294/11240239/627c0362-8df1-11e5-81fa-216366a5d8da.gif)
---
###### Admin themes management
![django-admin-interface_themes_management](https://cloud.githubusercontent.com/assets/1035294/11240245/6cd1c342-8df1-11e5-928b-f22217474d3d.gif)
---
###### Admin theme customization
![django-admin-interface_theme_customization](https://cloud.githubusercontent.com/assets/1035294/11240250/7350d942-8df1-11e5-9b28-f2f54c333cdc.gif)

#### Thanks
- [django-flat-theme](https://github.com/elky/django-flat-theme/)
- [django-flat-responsive](https://github.com/elky/django-flat-responsive)
- [django-colorfield](https://github.com/jaredly/django-colorfield/)

## License
Released under [MIT License](LICENSE).
