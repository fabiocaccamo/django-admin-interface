#django-admin-interface
django-admin-interface is a modern **flat admin interface customizable by the admin itself**.

You can use the builtin **django-theme** or create your own and **customize** **title, logo and colors**.

##Requirements
- Python 2.6, Python 2.7, Python 3.4
- Django 1.6.5 through Django 1.9

##Installation
- Run `pip install django-admin-interface`
- Add `admin_interface`, `flat` and `colorfield` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    'admin_interface',
    'flat',
    'colorfield',
    #...
    'django.contrib.admin',
    #...
)
```
- Run ``python manage.py migrate`` *(add ``--fake-initial`` if you are upgrading from 0.1.0 version)*
- Run ``python manage.py collectstatic``
- Restart your application server

##Screenshots
######Admin login
![django-admin-interface_login](https://cloud.githubusercontent.com/assets/1035294/11240233/55c8d4ba-8df1-11e5-9568-00fdc987ede8.gif)
---
######Admin dashboard
![django-admin-interface_dashboard](https://cloud.githubusercontent.com/assets/1035294/11240239/627c0362-8df1-11e5-81fa-216366a5d8da.gif)
---
######Admin themes management
![django-admin-interface_themes_management](https://cloud.githubusercontent.com/assets/1035294/11240245/6cd1c342-8df1-11e5-928b-f22217474d3d.gif)
---
######Admin theme customization
![django-admin-interface_theme_customization](https://cloud.githubusercontent.com/assets/1035294/11240250/7350d942-8df1-11e5-9b28-f2f54c333cdc.gif)

####Thanks
- [django-flat-theme](https://github.com/elky/django-flat-theme/)
- [django-colorfield](https://github.com/jaredly/django-colorfield/)

##License
The MIT License (MIT)

Copyright (c) 2016 Fabio Caccamo - fabio.caccamo@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
