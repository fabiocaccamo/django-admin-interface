# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.29.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.29.4) - 2025-01-17
-   [html] Guard variables that are not always defined. (by [@merwok](https://github.com/merwok) in #418)

## [0.29.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.29.3) - 2025-01-11
-   [html] Fix old nocache md5. (by [@merwok](https://github.com/merwok) in #417)
-   [ci] Bump `pre-commit` hooks.
-   [ci] Bump `codecov` action.

## [0.29.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.29.2) - 2024-11-20
-   [js] Highlight tab button with errors. #287 (thanks to [@EricPobot](https://github.com/EricPobot))
-   [css] Improve related widget links style.
-   [css] Improve user reset-password form appearance.
-   [css] Don't show datetime widget on single-line in inlines.
-   [ci] Bump `pre-commit` hooks.
-   [ci] Bump test requirements.

## [0.29.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.29.1) - 2024-10-23
-   [css] Hide dashboard app elements when all their models are filtered-out (hidden) by quick-search filters.
-   [ci] Bump `pre-commit` hooks.

## [0.29.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.29.0) - 2024-10-17
-   [python] Drop `Python 3.8`, `Python 3.9` and `Django 3.x` support.
-   [python] Add support for admin `show_facets` option. #396
-   [python] Fix serving static files from third-party services. #384 #385
-   [css] Improve list filter style.
-   [css] Set changelist table cell max-width.
-   [ci] Add `Django 5.1` to `tox` test matrix.
-   [ci] Update `pyupgrade` and `django-upgrade` hooks target versions.
-   [ci] Bump `pre-commit` hooks.
-   [ci] Bump test requirements.

## [0.28.9](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.9) - 2024-09-13
-   [css] Add missing background color variable.
-   [css] Fix fieldsets border color.
-   [css] Fix fieldset collapse header style.
-   [css] Prevent changelist table text wrapping.
-   [html] Show theme toggle.
-   [ci] Bump test requirements.
-   [ci] Bump `pre-commit` hooks.

## [0.28.8](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.8) - 2024-06-26
-   [js] Fix invalid assignment to const `iframeInternalModalClass`.

## [0.28.7](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.7) - 2024-06-23
-   [html] Fix missing check for showing inlines as tabs. #390
-   [css] Improve m2m selector style.
-   [css] Fix m2m selector not styled correctly. #393
-   [css] Update related-widget links margins.
-   [css] Use `position: fixed;` for related modal.
-   [css] Improve html list preview rendering with `django-streamfield`.
-   [js] Code refactoring for adding modal params to url and use `const` and `let` instead of `var`.
-   [ci] Bump `pre-commit` hooks.

## [0.28.6](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.6) - 2024-03-07
-   [python] Fix date hierarchy params. #374 (by [@jeroenpeters1986](https://github.com/jeroenpeters1986) in #375)
-   [js] Open any link with `_popup=1` query-string parameter in a modal window.
-   [ci] Bump requirements.
-   [ci] Bump `pre-commit` hooks.

## [0.28.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.5) - 2024-01-30
-   [css] Fix related widget height and buttons alignment when there is a multiline label.
-   [css] Fix inputs height when there is a multiline label.

## [0.28.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.4) - 2024-01-29
-   [css] Fix header logo not displayed correctly.

## [0.28.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.3) - 2024-01-08
-   [css] Fix help text horizontal alignment when using `show-fieldsets-as-tabs` / `show-inlines-as-tabs` theme options. #317
-   [css] Fix file-upload widget margin-left.
-   [css] Fix related widget links add button position on `many-to-many` selector.
-   [css] Fix related widget links margin from `select2` (`autocomplete_fields`).
-   [css] Reduce paginator vertical padding.

## [0.28.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.2) - 2024-01-08
-   [css] Fix related widget icon alignment. #348 #350

## [0.28.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.1) - 2023-12-28
-   [python] Fix `TemplateDoesNotExist` when using `django-nested-admin` by returning custom template for other third-party packages. #341 (by [@markdrrr](https://github.com/markdrrr) in #342)
-   [html] Display language chooser language name uppercase.
-   [css] Move save buttons to right in change form.
-   [css] Fix related widget links icons size and vertical alignment.
-   [css] Fix admin `raw_id_fields` appearance.
-   [css] Fix `autocomplete_fields` appearance.
-   [ci] Bump requirements.

### Contributors
-   [@markdrrr](https://github.com/markdrrr)

## [0.28.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.28.0) - 2023-12-21
-   [html] Remove old `flat-theme` body class.
-   [html] Remove `type="text/css"` and `type="text/javascript"` attributes.
-   [css] Fix filter input fields collapsing on different layouts. #338
-   [css] Fix paginator buttons height.
-   [css] Fix `foldable-apps` +/- button vertical alignment.
-   [css] Split `admin-interface-fix.css` CSS file into multiple files for easier debugging.
-   [css] Rename `form-controls.css` to `sticky-form-controls.css`.
-   [css] Move third-party compatibility CSS files to a `third-party` folder.
-   [css] Move `related-modal.css` to related-modal plugin folder.
-   [third-party] Update compatibility with `django-streamfield`.
-   [ci] Replace `Black` and `isort` with `Ruff-format`.
-   [ci] Bump `pre-commit` hooks.

## [0.27.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.27.0) - 2023-12-05
-   Add `Python 3.12` support.
-   Add `Django 5.0` support.
-   Fix broken language-chooser with `i18n_patterns(..., prefix_default_language=False)`. #327 (by [@julianwachholz](https://github.com/julianwachholz) in #328)
-   Simplify language-chooser. #327 (by [@julianwachholz](https://github.com/julianwachholz) in #328)
-   Speed-up test workflow.
-   Bump requirements.
-   Bump `pre-commit` hooks.

### Contributors
-   [@julianwachholz](https://github.com/julianwachholz)

## [0.26.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.26.1) - 2023-09-05
-   Fix logout and theme buttons style. #246
-   Add Russian translation. (by [@rustzzdevel](https://github.com/rustzzdevel) in #295)
-   Update Italian translations.
-   Update Spanish translations. (by [@smunoz-ml](https://github.com/smunoz-ml) in #307)
-   Prevent multiple `.collapse-toggle` button.
-   Bump requirements.
-   Bump `pre-commit` hooks.

## [0.26.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.26.0) - 2023-05-11
-   Add options for collapsible inlines. #263 (by [@fabiocaccamo](https://github.com/fabiocaccamo) in #282)
-   Bump requirements.
-   Bump `pre-commit` hooks.

## [0.25.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.25.0) - 2023-04-18
-   Add `Django 4.2` support.
-   Drop `Django 2.2` support.
-   Fix `date_hierarchy` with multiple fields (`ForeignKey`). #244
-   Fix tabs not working with non-ASCII alphanumeric characters. #237
-   Fix multidb tests.
-   Add `css_generic_link_active_color` field to use on active tab (tabbed changeform). #232
-   Replace `flake8` with `Ruff`.
-   Switch from `setup.py` to `pyproject.toml`.
-   Add `pyupgrade` to `pre-commit` config.
-   Add `django-upgrade` to `pre-commit` hooks.
-   Upgrade syntax for `Python >= 3.8`.
-   Run `pre-commit` also with `tox`.
-   Reformat migrations.
-   Bump requirements.
-   Bump `pre-commit` hooks.
-   Pin test requirements.
-   Add pull request template.
-   Add `CODE_OF_CONDUCT.md`. #238
-   Rename default branch from `master` to `main`.

## [0.24.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.24.2) - 2022-12-19
-   Fix modal and popup opening at the same time. #228
-   Make `Theme.get_active_theme` class method a manager method. (by [@MounirMesselmeni](https://github.com/MounirMesselmeni) in #230)

## [0.24.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.24.1) - 2022-12-14
-   Fix modal opener buttons not working when added to the DOM asynchronously. #228
-   [css] Improve changelist filter margins.

## [0.24.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.24.0) - 2022-12-11
-   Drop `Python < 3.8` and `Django < 2.2` versions support. (by [@merwok](https://github.com/merwok) in #220)
-   Replace `str.format` with `f-strings`.
-   Remove `post_migrate` signal handler and multi db test.
-   Add german translation. (by [@derzinn](https://github.com/derzinn) in #222)
-   Include date hierarchy in quick removal links (by [@merwok](https://github.com/merwok) in #218)
-   Fix broken tabbed inline name. (by [@VaZark](https://github.com/VaZark) in #221)
-   Minor cleanups. (by [@merwok](https://github.com/merwok) in #225)
-   Bump actions and requirements.
-   [css] Fix inlines vertical alignement. (by [@VaZark](https://github.com/VaZark) in #201)
-   [css] Fix tabbed changeform tabs text color on focus. (by [@VaZark](https://github.com/VaZark) in #223)
-   [CI] Add Farsi language to `tests.settings.LANGUAGES`. (by [@merwok](https://github.com/merwok))
-   [CI] Update `pre-commit` config.
-   [CI] Automate package build and publish on PyPI.

## [0.23.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.23.0) - 2022-11-30
-   Add `Python 3.11` support.
-   Add tabbed changeform support. (by [@VaZark](https://github.com/VaZark) in #211)
-   Fix #208 / Do not assume active DB when not specified. (by [@VaZark](https://github.com/VaZark) in #210)
-   Update translations.
-   Bump actions and requirements.
-   [css] Adjust list filter dropdown vertical margins.
-   [css] Improve nav filter style. #214
-   [css] Improve language chooser style.
-   [css] Reduce secondary scrollbars size.
-   [CI] Update `dependabot.yml`
-   [CI] Add `pre-commit-autoupdate.yml` workflow.
-   [CI] Update `pre-commit` hooks.

## [0.22.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.22.2) - 2022-11-18
-   [CI] Add `django 4.1` to tests.
-   [CI] Add `pre-commit` with `black`, `isort` and `flake8`.
-   Respect `using` in signals. #199 (by [@VaZark](https://github.com/VaZark) in #200)
-   Remove translations line numbers to avoid `lint` step failures.

## [0.22.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.22.1) - 2022-10-13
-   Fix `KeyError` raised by `django-rangefilter`.
-   [css] Add `django-rangefilter` style optimizations.
-   [css] Fix list-filter dropdown vertical margins.
-   [css] Fix calendar prev/next arrows style.

## [0.22.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.22.0) - 2022-10-12
-   Add CI checks for migrations and translations. #184 (by [@merwok](https://github.com/merwok) in #186)
-   Add option for list filter quick remove. #181 (by [@merwok](https://github.com/merwok) in #183)
-   [css] Fix left/right scrolling broken with django-import-export. #165
-   [html] Fix duplicated welcome message. #185

## [0.21.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.21.0) - 2022-10-06
-   Add language chooser control option (default select, minimal select). #136
-   Add option to make active list filters more visible. #174 (by [@merwok](https://github.com/merwok) in #178)
-   Add support for collapsible fieldsets that start expanded. #173 (by [@merwok](https://github.com/merwok) in #177)
-   [js] Fix modal window not closing on save with `django >= 4.0`. #169
-   [css] Move `language-chooser` style to its own CSS file.
-   [css] Fix sticky list filter scrolling. #175
-   [css] Fix paginator missing `border-top` on mobile.

## [0.20.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.20.0) - 2022-08-25
-   Add `django-streamfield` compatibility.

## [0.19.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.19.2) - 2022-08-04
-   Fix `hashlib` compatibility with `FIPS` enabled systems. #167 (by [@jonlev1n](https://github.com/jonlev1n) in #168)

## [0.19.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.19.1) - 2022-05-14
-   [css] Fixed dashboard alignment when recent-actions are not visible.

## [0.19.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.19.0) - 2022-03-08
-   Converted dynamic inline CSS to external static CSS using CSS variables. #157 #93 (thanks to [@Mustafa-Abu-Ghazy](https://github.com/Mustafa-Abu-Ghazy))

## [0.18.7](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.18.7) - 2022-02-24
-   Removed public disclosures of the lib's version. #154 (thanks to [@mintyPT](https://github.com/mintyPT))
-   Reformatted code with **Black**.

## [0.18.6](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.18.6) - 2022-02-04
-   Added polish (`pl`) localization by [paduszyk](https://github.com/paduszyk). #152
-   Fixed login logo `max-width` and title `color`.

## [0.18.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.18.5) - 2022-01-21
-   Added portuguese brazil (`pt_BR`) localization by [leandromsd](https://github.com/leandromsd). #149
-   Fixed body scroll reset to top when opening related modal. #150

## [0.18.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.18.4) - 2022-01-05
-   Added official django 4.0 support.
-   Added link to admin home page on logo and title. #147
-   Fixed collapsed inlines rounded bottom borders.
-   Fixed missing comma in tests settings `MIDDLEWARE_CLASSES`. #145

## [0.18.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.18.3) - 2021-12-07
-   Added official python 3.10 support.
-   Replaced travis with GitHub action workflow. #142
-   Fixed `check_installed_apps` checks.
-   Fixed django default appconfig deprecation warning. #141

## [0.18.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.18.2) - 2021-10-25
-   Fixed migration error.

## [0.18.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.18.1) - 2021-10-25
-   Removed wrong migration.

## [0.18.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.18.0) - 2021-10-24
-   Added foldable apps support. #117
-   Removed `css` field from `Theme` model.

## [0.17.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.17.3) - 2021-10-12
-   Fixed `FileExtensionValidator` `TypeError` on django < 1.11.

## [0.17.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.17.2) - 2021-10-08
-   Fixed `FileExtensionValidator` `TypeError` on django < 1.11.

## [0.17.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.17.1) - 2021-09-24
-   Fixed `TemplateDoesNotExist` error on `django==4.0.a1` removing checking condition for `colorfield` package. #134
-   Fixed favicon fetching incompatible with `django-storages` `S3`. #128

## [0.17.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.17.0) - 2021-09-16
-   Added `logo_max_width` and `logo_max_height`. #127

## [0.16.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.16.4) - 2021-09-04
-   Fixed `0020_module_selected_colors` migration for multiple dbs. #132
-   Fixed sticky pagination `width` and `border-bottom`.
-   Fixed inlines vertical overlow.
-   Improved header elements vertical alignment.

## [0.16.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.16.3) - 2021-04-26
-   Added `compat` module.
-   Added missing `0021_file_extension_validator` migration. #126
-   Formatted migrations.

## [0.16.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.16.2) - 2021-04-23
-   Added `python 3.9` and `django 3.2` to CI.
-   Added `FileExtensionValidator` to `logo` and `favicon` fields. #112
-   Fixed `models.W042` warning on `django 3.2`.
-   Fixed header `min-height`.
-   Fixed selects `min-width`.
-   Fixed changelist search, actions and submit button horizontal margins.
-   Fixed related widget wrapper margin/padding with normal select and in inlines.
-   Fixed tabular inlines horizontal scroll.

## [0.16.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.16.1) - 2021-04-07
-   Fixed style of "Delete" and "Save" buttons in the delete confirmation page. #123
-   Overridden dark-mode css variables introduced in `django 3.2`. #124

## [0.16.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.16.0) - 2021-03-30
-   Added customizable colors for selected apps and models in dashboard. #122
-   Added `responsive_rtl.css` stylesheet. #98
-   Updated `vazir-font` version to `27.2.2`. #98

## [0.15.6](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.15.6) - 2021-03-26
-   Fixed `show_change_link` related modal support. #120
-   Fixed inline changelink style.
-   Made globally available `presentRelatedObjectModal` and `presentRelatedObjectModalOnClickOn` js functions.

## [0.15.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.15.5) - 2021-03-02
-   Fixed sticky submit and pagination `z-index` issue with related modal.

## [0.15.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.15.4) - 2021-03-01
-   Fixed sticky submit and pagination `z-index` issue with sticky `list_filter` and `django-json-widget`.

## [0.15.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.15.3) - 2021-02-08
-   Fixed sticky submit and pagination width when `admin.site.enable_nav_sidebar = False`. #113

## [0.15.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.15.2) - 2021-02-03
-   Fixed body classes template rendering.
-   Improved sticky submit and pagination backward compatibility.

## [0.15.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.15.1) - 2021-02-03
-   Fixed and improved sticky form controls and pagination style.

## [0.15.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.15.0) - 2021-02-03
-   Added sticky form controls and pagination options. #110
-   Added support to 4-digit language code in language chooser. #111
-   Added theme css variables for third-party libraries.
-   Fixed app module section link hover color.

## [0.14.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.14.2) - 2021-01-04
-   Fixed tabular inline scroll bar. #101
-   Fixed module header selected link color. #102
-   Fixed main content width when `admin.site.enable_nav_sidebar = False`. #105

## [0.14.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.14.1) - 2020-11-12
-   Fixed sticky list-filter floating. #100

## [0.14.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.14.0) - 2020-10-15
-   Added list filter sticky option (only for `django >= 3.1.2`).
-   Enabled list filter dropdown by default.
-   Fixed changelist searchbar style.

## [0.13.7](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.7) - 2020-10-14
-   Improved responsive widgets style.
-   Prevented body horizontal scroll.
-   Fixed tabular inline horizontal scroll.
-   Fixed changelist filter min-width.
-   Fixed changelist and toolbar theme rounded corners.
-   Fixed calendar and timelist buttons theme color.
-   Fixed list filter select size.
-   Fixed content max-width with `django >= 3.1`.

## [0.13.6](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.6) - 2020-10-14
-   Added persian language. #98
-   Fixed logo max-width on small screens.
-   Fixed content max-width when nav-sidebar is collapsed.
-   Fixed changelist max-width on medium screens.

## [0.13.5](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.5) - 2020-09-15
-   Fixed loaddata error with initial_data.json fixture. #97
-   Fixed tests warning (admin.W411).
-   Fixed changelist thead links color.
-   Fixed changelist filter links hover color.

## [0.13.4](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.4) - 2020-09-04
-   Added conditional imports to avoid Django deprecation warnings. #92
-   Changed admin header content vertical align to top.

## [0.13.3](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.3) - 2020-09-02
-   Added `django-json-widget` theming support.

## [0.13.2](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.2) - 2020-08-21
-   Fixed related modal not closing on edit save and create with django 3.1 - #96

## [0.13.1](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.1) - 2020-08-18
-   Improved header and nav-sidebar style.
-   Added `max-width` to logo.
-   Added `requirements-dev.txt`

## [0.13.0](https://github.com/fabiocaccamo/django-admin-interface/releases/tag/0.13.0) - 2020-08-05
-   Improved nav-sidebar style (`django>=3.1` support).
-   Improved header style.

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
