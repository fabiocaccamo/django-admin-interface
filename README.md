[![](https://img.shields.io/pypi/pyversions/django-admin-interface.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-admin-interface?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-admin-interface.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-admin-interface/)
[![](https://pepy.tech/badge/django-admin-interface)](https://pepy.tech/project/django-admin-interface)
[![](https://img.shields.io/github/stars/fabiocaccamo/django-admin-interface?logo=github)](https://github.com/fabiocaccamo/django-admin-interface/)
[![](https://badges.pufler.dev/visits/fabiocaccamo/django-admin-interface?label=visitors&color=blue)](https://badges.pufler.dev)
[![](https://img.shields.io/pypi/l/django-admin-interface.svg?color=blue)](https://github.com/fabiocaccamo/django-admin-interface/blob/master/LICENSE.txt)

[![](https://img.shields.io/travis/fabiocaccamo/django-admin-interface?logo=travis&label=build)](https://travis-ci.org/fabiocaccamo/django-admin-interface)
[![](https://img.shields.io/codecov/c/gh/fabiocaccamo/django-admin-interface?logo=codecov)](https://codecov.io/gh/fabiocaccamo/django-admin-interface)
[![](https://img.shields.io/codacy/grade/21cb657283c04e70b56fb935277a1ad1?logo=codacy)](https://www.codacy.com/app/fabiocaccamo/django-admin-interface)
[![](https://img.shields.io/codeclimate/maintainability/fabiocaccamo/django-admin-interface?logo=code-climate)](https://codeclimate.com/github/fabiocaccamo/django-admin-interface/)
[![](https://requires.io/github/fabiocaccamo/django-admin-interface/requirements.svg?branch=master)](https://requires.io/github/fabiocaccamo/django-admin-interface/requirements/?branch=master)

# django-admin-interface
django-admin-interface is a modern **responsive flat admin interface customizable by the admin itself**.

![django-admin-interface-preview](https://user-images.githubusercontent.com/1035294/35631521-64b0cab8-06a4-11e8-8f57-c04fdfbb7e8b.gif)

## Features
- Beautiful default **django-theme**
- Themes management and customization *(you can **customize admin title, logo and colors**)*
- Responsive
- List filter dropdown *(optional)*
- `NEW` **Related modal** *(instead of the old popup window, optional)*
- `NEW` **Environment name/marker**
- `NEW` **Language chooser**
- Compatibility / Style optimizations for:
  - `django-ckeditor`
  - `django-dynamic-raw-id`
  - `django-json-widget`
  - `django-modeltranslation`
  - `django-tabbed-admin`
  - `sorl-thumbnail`

## Installation
- Run `pip install django-admin-interface`
- Add `admin_interface`, `flat_responsive`, `flat` and `colorfield` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    'admin_interface',
    'flat_responsive', # only if django version < 2.0
    'flat', # only if django version < 1.9
    'colorfield',
    #...
    'django.contrib.admin',
    #...
)

X_FRAME_OPTIONS='SAMEORIGIN' # only if django version >= 3.0
```
- Run ``python manage.py migrate``
- Run ``python manage.py collectstatic``
- Restart your application server

#### Upgrade
- Run `pip install django-admin-interface --upgrade`
- Run ``python manage.py migrate`` *(add* ``--fake-initial`` *if you are upgrading from 0.1.0 version)*
- Run ``python manage.py collectstatic --clear``
- Restart your application server

## Optional themes
This package ships with optional themes as fixtures, they can be installed using the [loaddata admin command](https://docs.djangoproject.com/en/1.11/ref/django-admin/#django-admin-loaddata). Optional themes are activated on installation.

##### [Django](https://www.djangoproject.com/) theme (default):
Run ``python manage.py loaddata admin_interface_theme_django.json``

##### [Bootstrap](http://getbootstrap.com/) theme:
Run ``python manage.py loaddata admin_interface_theme_bootstrap.json``

##### [Foundation](http://foundation.zurb.com/) theme:
Run ``python manage.py loaddata admin_interface_theme_foundation.json``

##### [U.S. Web Design Standards](https://standards.usa.gov/) theme:
Run ``python manage.py loaddata admin_interface_theme_uswds.json``

### Add more themes
You can add a theme you've created through the admin to this repository by [sending us a PR](http://makeapullrequest.com/). Here are the steps to follow to add:

1. Export your exact theme as fixture using the `dumpdata` admin command:
``python manage.py dumpdata admin_interface.Theme --indent 4 -o admin_interface_theme_{{name}}.json --pks=N``

2. Copy the generated json file into the fixtures folder *(making sure its name starts with* `admin_interface_theme_` *to avoid clashes with fixtures that might be provided by other third party apps)*.

3. Remove the `"pk"` from the fixture and make sure the `active` field is set to `true` *(in this way a theme is automatically activated when installed)*.

4. Edit the section above to document your theme.

### Add theme support to third-party libraries
You can add **theme support to existing third-party libraries** using the following **css variables**:

- `--admin-interface-title-color`
- `--admin-interface-logo-color`
- `--admin-interface-env-color`
- `--admin-interface-header-background-color:`
- `--admin-interface-header-text-color`
- `--admin-interface-header-link-color`
- `--admin-interface-header-link_hover-color`
- `--admin-interface-module-background-color`
- `--admin-interface-module-text-color`
- `--admin-interface-module-link-color`
- `--admin-interface-module-link-hover-color`
- `--admin-interface-generic-link-color`
- `--admin-interface-generic-link-hover-color`
- `--admin-interface-save-button-background-color`
- `--admin-interface-save-button-background-hover-color`
- `--admin-interface-save-button-text-color`
- `--admin-interface-delete-button-background-color`
- `--admin-interface-delete-button-background-hover-color`
- `--admin-interface-delete-button-text-color`
- `--admin-interface-related-modal-background-color`
- `--admin-interface-related-modal-background-opacity`


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

## FAQ
- #### I already have a custom `base_site.html`, how can I make it work?

You can use [django-apptemplates](https://github.com/bittner/django-apptemplates), then add `{% extends "admin_interface:admin/base_site.html" %}` to your `base_site.html`

## Testing
```bash
# create python virtual environment
virtualenv testing_django_admin_interface

# activate virtualenv
cd testing_django_admin_interface && . bin/activate

# clone repo
git clone https://github.com/fabiocaccamo/django-admin-interface.git src && cd src

# install dependencies
pip install -r requirements.txt

# run tests
tox
# or
python setup.py test
# or
python -m django test --settings "tests.settings"
```

## License
Released under [MIT License](LICENSE.txt).

---

## See also

- [`django-colorfield`](https://github.com/fabiocaccamo/django-colorfield) - simple color field for models with a nice color-picker in the admin. 🎨

- [`django-extra-settings`](https://github.com/fabiocaccamo/django-extra-settings) - config and manage typed extra settings using just the django admin. ⚙️

- [`django-maintenance-mode`](https://github.com/fabiocaccamo/django-maintenance-mode) - shows a 503 error page when maintenance-mode is on. 🚧 🛠️

- [`django-redirects`](https://github.com/fabiocaccamo/django-redirects) - redirects with full control. ↪️

- [`django-treenode`](https://github.com/fabiocaccamo/django-treenode) - probably the best abstract model / admin for your tree based stuff. 🌳

- [`python-benedict`](https://github.com/fabiocaccamo/python-benedict) - dict subclass with keylist/keypath support, I/O shortcuts (base64, csv, json, pickle, plist, query-string, toml, xml, yaml) and many utilities. 📘

- [`python-codicefiscale`](https://github.com/fabiocaccamo/python-codicefiscale) - encode/decode Italian fiscal codes - codifica/decodifica del Codice Fiscale. 🇮🇹 💳

- [`python-fsutil`](https://github.com/fabiocaccamo/python-fsutil) - file-system utilities for lazy devs. 🧟‍♂️
