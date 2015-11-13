# django-admin-interface
django-admin-interface is a modern **admin interface customizable by the admin itself (title, logo and colors)**.

##Requirements
- Python 2.6, Python 2.7
- Django 1.6.5 through Django 1.8.4

##Installation
- Run `pip install django-admin-interface`
- Add `admin_interface`, `flat` and `colorfield` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    'flat',
    'colorfield',
    'admin_interface', 
    #...
    'django.contrib.admin',
    #...
)
```
- Run ``python manage.py collectstatic``
- Restart your application server

##Thanks
- [django-flat-theme](https://github.com/elky/django-flat-theme/)
- [django-colorfield](https://github.com/jaredly/django-colorfield/)

##License
The MIT License (MIT)

Copyright (c) 2015 Fabio Cacccamo - fabio.caccamo@gmail.com

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
