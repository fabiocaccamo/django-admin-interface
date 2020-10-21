# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-admin-interface'

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
]

if django.VERSION < (1, 9):
    # ONLY if django version < 1.9
    INSTALLED_APPS += [
        'flat',
    ]

if django.VERSION < (2, 0):
    # ONLY if django version < 2.0
    INSTALLED_APPS += [
        'flat_responsive',
    ]

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
]

if django.VERSION < (2, 0):
    MIDDLEWARE_CLASSES = [
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware'
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]
else:
    MIDDLEWARE = [
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ]
    },
},]

database_engine = os.environ.get('DATABASE_ENGINE', 'sqlite')
database_config = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
    # 'mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'admin_interface',
    #     'USER': 'mysql',
    #     'PASSWORD': 'mysql',
    #     'HOST': '',
    #     'PORT': '',
    # },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'admin_interface',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '',
        'PORT': '',
    }
}

DATABASES = {
    'default': database_config.get(database_engine),
}

USE_I18N = True
LANGUAGES = (
    ('en', 'English', ),
    ('it', 'Italian', ),
)
LANGUAGE_CODE = 'en'

ROOT_URLCONF = 'tests.urls'

MEDIA_ROOT = os.path.join(BASE_DIR, 'admin_interface/public/media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'admin_interface/public/static/')
STATIC_URL = '/static/'

