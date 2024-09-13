[![](https://img.shields.io/pypi/pyversions/django-admin-interface.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-admin-interface?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-admin-interface.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-admin-interface/)
[![](https://static.pepy.tech/badge/django-admin-interface/month)](https://pepy.tech/project/django-admin-interface)
[![](https://img.shields.io/github/stars/fabiocaccamo/django-admin-interface?logo=github&style=flat)](https://github.com/fabiocaccamo/django-admin-interface/stargazers)
[![](https://img.shields.io/pypi/l/django-admin-interface.svg?color=blue)](https://github.com/fabiocaccamo/django-admin-interface/blob/main/LICENSE.txt)

[![](https://results.pre-commit.ci/badge/github/fabiocaccamo/django-admin-interface/main.svg)](https://results.pre-commit.ci/latest/github/fabiocaccamo/django-admin-interface/main)
[![](https://img.shields.io/github/actions/workflow/status/fabiocaccamo/django-admin-interface/test-package.yml?branch=main&label=build&logo=github)](https://github.com/fabiocaccamo/django-admin-interface)
[![](https://img.shields.io/codecov/c/gh/fabiocaccamo/django-admin-interface?logo=codecov)](https://codecov.io/gh/fabiocaccamo/django-admin-interface)
[![](https://img.shields.io/codacy/grade/21cb657283c04e70b56fb935277a1ad1?logo=codacy)](https://www.codacy.com/app/fabiocaccamo/django-admin-interface)
[![](https://img.shields.io/codeclimate/maintainability/fabiocaccamo/django-admin-interface?logo=code-climate)](https://codeclimate.com/github/fabiocaccamo/django-admin-interface/)
[![](https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=black)](https://github.com/psf/black)
[![](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# django-admin-interface
django-admin-interface is a modern **responsive flat admin interface customizable by the admin itself**.

![django-admin-interface-preview](https://user-images.githubusercontent.com/1035294/35631521-64b0cab8-06a4-11e8-8f57-c04fdfbb7e8b.gif)

## Features
- Beautiful default **django-theme**
- Themes management and customization *(you can **customize admin title, logo and colors**)*
- Responsive
- Related modal *(instead of the old popup window)*
- Environment name/marker
- Language chooser
- Foldable apps *(accordions in the navigation bar)*
- [Collapsible fieldsets](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets) can have their initial state expanded instead of collapsed
- `NEW` Collapsible inlines
- `NEW` Tabbed fieldsets and inlines
- `NEW` List filter removal links
- `NEW` List filter highlight selected options
- List filter dropdown
- List filter sticky
- Form controls sticky *(pagination and save/delete buttons)*
- Compatibility / style optimizations for:
  - `django-ckeditor`
  - `django-dynamic-raw-id`
  - `django-json-widget`
  - `django-modeltranslation`
  - `django-rangefilter`
  - `django-streamfield`
  - `django-tabbed-admin`
  - `sorl-thumbnail`
- Translated in many languages: `de`, `es`, `fa`, `fr`, `it`, `pl`, `pt_BR`, `ru`, `tr`

## Installation
- Run `pip install django-admin-interface`
- Add `admin_interface` and `colorfield` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    "admin_interface",
    "colorfield",
    #...
    "django.contrib.admin",
    #...
)

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
```
- Run `python manage.py migrate`
- Run `python manage.py collectstatic --clear`
- Restart your application server

> [!WARNING]
> if you want use modals instead of popup windows, ensure to add `X_FRAME_OPTIONS = "SAMEORIGIN"` setting.

### Optional features
To make a fieldset start expanded with a `Hide` button to collapse, add the class `"expanded"` to its classes:
```python
class MyModelAdmin(admin.ModelAdmin):
    # ...
    fieldsets = [
        ("Section title", {
            "classes": ("collapse", "expanded"),
            "fields": (...),
        }),
    ]
    # ...
```

## Optional themes
This package ships with optional themes as fixtures, they can be installed using the [loaddata admin command](https://docs.djangoproject.com/en/1.11/ref/django-admin/#django-admin-loaddata). Optional themes are activated on installation.

##### [Django](https://www.djangoproject.com/) theme (default):
Run `python manage.py loaddata admin_interface_theme_django.json`

##### [Bootstrap](http://getbootstrap.com/) theme:
Run `python manage.py loaddata admin_interface_theme_bootstrap.json`

##### [Foundation](http://foundation.zurb.com/) theme:
Run `python manage.py loaddata admin_interface_theme_foundation.json`

##### [U.S. Web Design Standards](https://standards.usa.gov/) theme:
Run `python manage.py loaddata admin_interface_theme_uswds.json`

### Add more themes
You can add a theme you've created through the admin to this repository by [sending us a PR](http://makeapullrequest.com/). Here are the steps to follow to add:

1. Export your exact theme as fixture using the `dumpdata` admin command:
`python manage.py dumpdata admin_interface.Theme --indent 4 -o admin_interface_theme_{{name}}.json --pks=N`

2. Copy the generated json file into the fixtures folder *(making sure its name starts with* `admin_interface_theme_` *to avoid clashes with fixtures that might be provided by other third party apps)*.

3. Remove the `pk` from the fixture and make sure the `active` field is set to `true` *(in this way a theme is automatically activated when installed)*.

4. Edit the section above to document your theme.

### Add theme support to third-party libraries
You can add **theme support to existing third-party libraries** using the following **CSS variables**:

#### Header

- `--admin-interface-header-background-color`
- `--admin-interface-header-text-color`
- `--admin-interface-header-link-color`
- `--admin-interface-header-link_hover-color`
- `--admin-interface-title-color`
- `--admin-interface-env-color`

#### Logo

- `--admin-interface-logo-color`
- `--admin-interface-logo-default-background-image`
- `--admin-interface-logo-max-width`
- `--admin-interface-logo-max-height`

#### Modules / Links
- `--admin-interface-module-background-color`
- `--admin-interface-module-background-selected-color`
- `--admin-interface-module-border-radius`
- `--admin-interface-module-text-color`
- `--admin-interface-module-link-color`
- `--admin-interface-module-link-selected-color`
- `--admin-interface-module-link-hover-color`
- `--admin-interface-generic-link-color`
- `--admin-interface-generic-link-hover-color`
- `--admin-interface-generic-link-active-color`

#### Buttons
- `--admin-interface-save-button-background-color`
- `--admin-interface-save-button-background-hover-color`
- `--admin-interface-save-button-text-color`
- `--admin-interface-delete-button-background-color`
- `--admin-interface-delete-button-background-hover-color`
- `--admin-interface-delete-button-text-color`

#### Related Modal
- `--admin-interface-related-modal-background-color`
- `--admin-interface-related-modal-background-opacity`
- `--admin-interface-related-modal-border-radius`
- `--admin-interface-related-modal-close-button-display`

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

## Localization
At the moment, this package has been translated into the following languages: `de`, `es`, `fa`, `fr`, `it`, `pl`, `pt_BR`, `tr`.

### Translate into another language

- Run `python -m django makemessages --ignore ".tox" --ignore "venv" --add-location "file" --extension "html,py" --locale "it"` *(example for Italian localization)*

- Update translations in `admin_interface/locale/it/LC_MESSAGES/django.po`

- Run `python -m django compilemessages --ignore ".tox" --ignore "venv"`

### Update translations

If you do some changes to the project, remember to update translations, because if the translations files are not up-to-date, the `lint` step in the CI will fail:
- Run `tox -e translations`

## Caching

This package uses caching to improve theme load time and overall performance.
You can customise the app caching options using `settings.CACHES["admin_interface"]` setting, otherwise the `"default"` cache will be used:

```python
CACHES = {
    # ...
    "admin_interface": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 60 * 5,
    },
    # ...
}
```

> [!WARNING]
> There is a [known compatibility issue](https://github.com/fabiocaccamo/django-admin-interface/issues/356) when using this package with `django-redis`, more specifically, using the `JSONSerializer` the following error is raised: `TypeError: Object of type Theme is not JSON serializable`, to mitigate this problem, simply use a specific cache for this app that does not use any `json` serializer.

## FAQ

### Custom `base-site.html`
> I already have a custom `base_site.html`, how can I make it work?

You can use [django-apptemplates](https://github.com/bittner/django-apptemplates), then add `{% extends "admin_interface:admin/base_site.html" %}` to your `base_site.html`

### Custom `LocaleMiddleware` warning
> I'm using a `django.middleware.locale.LocaleMiddleware` subclass, but I see an unnecessary warning for missing `django.middleware.locale.LocaleMiddleware`, what can I do?

You can simply ignore the warning (this has been discussed [here](https://github.com/fabiocaccamo/django-admin-interface/issues/354))
```python
import warnings

warnings.filterwarnings("ignore", module="admin_interface.templatetags.admin_interface_tags")
```

### Language Chooser not showing
> I have enabled the **Language Chooser**, but it is not visible in the admin, what should I do?

You must configure multilanguage `settings` and `urls` correctly:
```python
LANGUAGES = (
    ("en", _("English")),
    ("it", _("Italiano")),
    ("fr", _("Français")),
    # more than one language is expected here
)
LANGUAGE_CODE = "en"
USE_I18N = True
MIDDLEWARE = [
    # ...
    "django.middleware.locale.LocaleMiddleware",
    # ...
]
```

```python
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

# ...

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
```

### Open any url in modal window
> I have an application with some cross-links in the admin and I would like to open them in modal windows instead of same/new window, how can I do?

You just need to add `_popup=1` query-string parameter to the urls:
```python
url = reverse(f"admin:myapp_mymodel_change", args=[mymodel_instance.pk])
url = f"{url}?_popup=1"
```

## Testing
```bash
# clone repository
git clone https://github.com/fabiocaccamo/django-admin-interface.git && cd django-admin-interface

# create virtualenv and activate it
python -m venv venv && . venv/bin/activate

# upgrade pip
python -m pip install --upgrade pip

# install requirements
pip install -r requirements.txt -r requirements-test.txt

# install pre-commit to run formatters and linters
pre-commit install --install-hooks

# run tests
tox
# or
python runtests.py
# or
python -m django test --settings "tests.settings"
```

## Contributing
Contributions are always welcome, please follow these steps for submitting good quality PRs:

- :exclamation: **Open an issue**, please don't submit any PR that doesn't refer to an existing issue.
- :computer: **Work on changes**, changes should *preferably* be covered by tests to avoid regressions in the future.
- :globe_with_meridians: **Update the translations** files.
- :test_tube: **Run tests** ensuring that there are no errors.
- :inbox_tray: **Submit a pull-request** and mark it as **"Ready for review"** only if it passes the `CI`.

## License
Released under [MIT License](LICENSE.txt).

---

## Supporting

- :star: Star this project on [GitHub](https://github.com/fabiocaccamo/django-admin-interface)
- :octocat: Follow me on [GitHub](https://github.com/fabiocaccamo)
- :blue_heart: Follow me on [Twitter](https://twitter.com/fabiocaccamo)
- :moneybag: Sponsor me on [Github](https://github.com/sponsors/fabiocaccamo)

## See also

- [`django-cache-cleaner`](https://github.com/fabiocaccamo/django-cache-cleaner) - clear the entire cache or individual caches easily using the admin panel or management command. 🧹✨

- [`django-colorfield`](https://github.com/fabiocaccamo/django-colorfield) - simple color field for models with a nice color-picker in the admin. 🎨

- [`django-extra-settings`](https://github.com/fabiocaccamo/django-extra-settings) - config and manage typed extra settings using just the django admin. ⚙️

- [`django-maintenance-mode`](https://github.com/fabiocaccamo/django-maintenance-mode) - shows a 503 error page when maintenance-mode is on. 🚧 🛠️

- [`django-redirects`](https://github.com/fabiocaccamo/django-redirects) - redirects with full control. ↪️

- [`django-treenode`](https://github.com/fabiocaccamo/django-treenode) - probably the best abstract model / admin for your tree based stuff. 🌳

- [`python-benedict`](https://github.com/fabiocaccamo/python-benedict) - dict subclass with keylist/keypath support, I/O shortcuts (base64, csv, json, pickle, plist, query-string, toml, xml, yaml) and many utilities. 📘

- [`python-codicefiscale`](https://github.com/fabiocaccamo/python-codicefiscale) - encode/decode Italian fiscal codes - codifica/decodifica del Codice Fiscale. 🇮🇹 💳

- [`python-fontbro`](https://github.com/fabiocaccamo/python-fontbro) - friendly font operations. 🧢

- [`python-fsutil`](https://github.com/fabiocaccamo/python-fsutil) - file-system utilities for lazy devs. 🧟‍♂️
