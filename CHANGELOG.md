# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.14.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.14.2) - 2021-01-04
-  Fixed tabular inline scroll bar. #101
-  Fixed module header selected link color. #102
-  Fixed main content width when `admin.site.enable_nav_sidebar = False`. #105

## [0.14.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.14.1) - 2020-11-12
-  Fixed sticky list-filter floating. #100

## [0.14.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.14.0) - 2020-10-15
-  Added list filter sticky option (only for `django >= 3.1.2`).
-  Enabled list filter dropdown by default.
-  Fixed changelist searchbar style.

## [0.13.7](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.7) - 2020-10-14
-  Improved responsive widgets style.
-  Prevented body horizontal scroll.
-  Fixed tabular inline horizontal scroll.
-  Fixed changelist filter min-width.
-  Fixed changelist and toolbar theme rounded corners.
-  Fixed calendar and timelist buttons theme color.
-  Fixed list filter select size.
-  Fixed content max-width with `django >= 3.1`.

## [0.13.6](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.6) - 2020-10-14
-  Added persian language. #98
-  Fixed logo max-width on small screens.
-  Fixed content max-width when nav-sidebar is collapsed.
-  Fixed changelist max-width on medium screens.

## [0.13.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.5) - 2020-09-15
-  Fixed loaddata error with initial_data.json fixture. #97
-  Fixed tests warning (admin.W411).
-  Fixed changelist thead links color.
-  Fixed changelist filter links hover color.

## [0.13.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.4) - 2020-09-04
-  Added conditional imports to avoid Django deprecation warnings. #92
-  Changed admin header content vertical align to top.

## [0.13.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.3) - 2020-09-02
-  Added `django-json-widget` theming support.

## [0.13.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.2) - 2020-08-21
-  Fixed related modal not closing on edit save and create with django 3.1 - #96

## [0.13.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.1) - 2020-08-18
-  Improved header and nav-sidebar style.
-  Added `max-width` to logo.
-  Added `requirements-dev.txt`

## [0.13.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.0) - 2020-08-05
-  Improved nav-sidebar style (`django>=3.1` support).
-  Improved header style.

## [0.12.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.12.3) - 2020-07-20
-   Fixed unreadable text in autocomplete multi-selects. #83

## [0.12.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.12.2) - 2020-04-07
-   Fixed popup javascript error when related modal is inactive. #76
-   Fixed js self invoking anonymous function expression.

## [0.12.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.12.1) - 2020-02-21
-   Updated `.travis` config.
-   Fixed custom django admin header. #75
-   Bumped `django-colorfield` version to `0.2.0`.
-   Added `tr` language.
-   Removed hard-coded favicon type.
-   Improved code-quality.

## [0.12.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.12.0) - 2019-12-02
-   Added `python 3.8` and `django 3.0` compatibility.

## [0.11.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.11.2) - 2019-09-27
-   Fixed `select2` background color.

## [0.11.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.11.1) - 2019-09-04
-   Added language chooser display option.

## [0.11.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.11.0) - 2019-09-03
-   Added language chooser.

## [0.10.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.10.5) - 2019-05-09
-   Fixed broken migration on postgres/windows. #52

## [0.10.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.10.4) - 2019-03-29
-   Added `django 2.2` to `tox` and `travis`.
-   Fixed admin duplicated count query.
-   Added admin theme caching to remove duplicated queries. #19
-   Added `django-dynamic-raw-id` support. #61
-   Updated `it` localization.

## [0.10.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.10.3) - 2019-03-28
-   Fixed idempotent deploy support. #40

## [0.10.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.10.2) - 2019-03-22
-   Fixed `raw-id-field` whith `django-admin-interface`. #58

## [0.10.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.10.1) - 2019-03-20
-   Updated `fr` localization.

## [0.10.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.10.0) - 2019-02-21
-   Updated messages.
-   Added related modal close button. #45
-   Updated fields verbose names.
-   Added environment options. #56

## [0.9.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.9.3) - 2019-02-06
-   Enabled travis pip cache.
-   Splitted tests to multiple files.
-   Added env badge to favicon.

## [0.9.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.9.2) - 2019-01-11
-   Fixed cancel button does not work. #53
-   Fixed IntegrityError on postgres

## [0.9.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.9.1) - 2019-01-11
-   Fixed missing migration. #51

## [0.9.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.9.0) - 2018-11-13
-   Added French localization.
-   Added Italian localization.
-   Added Spanish localization.
-   Added internationalization support.

## [0.8.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.8.2) - 2018-10-24
## [0.8.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.8.1) - 2018-10-11
## [0.8.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.8.0) - 2018-08-31
## [0.7.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.7.0) - 2018-02-06
## [0.6.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.6.3) - 2018-02-05
## [0.6.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.6.2) - 2018-02-01
## [0.6.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.6.1) - 2018-01-31
## [0.6.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.6.0) - 2017-11-23
## [0.5.9](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.9) - 2017-10-04
## [0.5.8](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.8) - 2017-09-29
## [0.5.7](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.7) - 2017-09-29
## [0.5.6](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.6) - 2017-09-29
## [0.5.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.5) - 2017-09-27
## [0.5.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.4) - 2017-09-27
## [0.5.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.3) - 2017-08-24
## [0.5.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.2) - 2017-07-13
## [0.5.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.1) - 2017-06-13
## [0.5.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.5.0) - 2017-06-09
## [0.4.6](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.4.6) - 2017-05-24
## [0.4.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.4.5) - 2017-05-19
## [0.4.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.4.4) - 2017-05-18
## [0.4.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.4.3) - 2017-05-16
## [0.4.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.4.2) - 2017-05-11
## [0.4.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.4.1) - 2017-05-04
## [0.4.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.4.0) - 2017-04-14
## [0.3.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.3.2) - 2017-03-29
## [0.3.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.3.1) - 2017-03-29
## [0.3.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.3.0) - 2017-02-09
## [0.2.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.2.1) - 2016-11-08
## [0.2.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.2.0) - 2016-09-10
## [0.1.9](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.9) - 2016-09-04
## [0.1.8](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.8) - 2016-08-05
## [0.1.7](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.7) - 2016-06-29
## [0.1.6](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.6) - 2016-04-13
## [0.1.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.5) - 2016-02-24
## [0.1.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.4) - 2016-02-15
## [0.1.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.3) - 2015-12-03
## [0.1.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.2) - 2015-11-25
## [0.1.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.1.1) - 2015-11-13
## [0.0.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.0.1) - 2015-11-13
