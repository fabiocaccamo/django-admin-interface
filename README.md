#django-admin-interface
django-admin-interface is a modern **flat admin interface customizable by the admin itself**.

You can use the builtin **django-theme** or create your own and **customize** **title, logo and colors**.

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

##Screenshots
######Admin login
![django-admin-interface_login](https://cloud.githubusercontent.com/assets/1035294/11153338/887e6d14-8a38-11e5-815e-8d91825ffa20.jpg)
---
######Admin dashboard
![django-admin-interface_dashboard](https://cloud.githubusercontent.com/assets/1035294/11152620/f3ac9e30-8a33-11e5-9886-5772c219a634.jpg)
---
######Admin themes management
![django-admin-interface_themes_management](https://cloud.githubusercontent.com/assets/1035294/11153350/9c377cd8-8a38-11e5-8ee8-e663589453ea.jpg)
---
######Admin theme customization
![django-admin-interface_theme_customization](https://cloud.githubusercontent.com/assets/1035294/11153155/361c4c86-8a37-11e5-8f82-b4c145004a35.jpg)

####Thanks
- [django-flat-theme](https://github.com/elky/django-flat-theme/)
- [django-colorfield](https://github.com/jaredly/django-colorfield/)

##License
The MIT License (MIT)

Copyright (c) 2015 Fabio Caccamo - fabio.caccamo@gmail.com

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
