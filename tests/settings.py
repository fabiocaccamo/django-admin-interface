import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "django-admin-interface"

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
]


INSTALLED_APPS += [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
]

MIDDLEWARE = [
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ]
        },
    },
]

database_engine = os.environ.get("DATABASE_ENGINE", "sqlite")
database_config = {
    "sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
    # 'mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'admin_interface',
    #     'USER': 'mysql',
    #     'PASSWORD': 'mysql',
    #     'HOST': '',
    #     'PORT': '',
    # },
    "postgres": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "admin_interface",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "",
        "PORT": "",
    },
    "postgres_replica": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "admin_interface_2",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "",
        "PORT": "",
    },
}

github_workflow = os.environ.get("GITHUB_WORKFLOW")
if github_workflow:
    database_config["postgres"]["NAME"] = "postgres"
    database_config["postgres"]["HOST"] = "127.0.0.1"
    database_config["postgres"]["PORT"] = "5432"
    database_config["postgres_replica"]["HOST"] = "127.0.0.1"
    database_config["postgres_replica"]["PORT"] = "5432"

replica_engine = (
    "postgres_replica" if database_engine == "postgres" else database_engine
)

DATABASES = {
    "default": database_config.get(database_engine),
    "replica": database_config.get(replica_engine),
}


DATABASE_ROUTERS = ["tests.routers.DatabaseAppsRouter"]

USE_I18N = True
LANGUAGES = (
    ("de", "Deutsch"),
    ("en", "English"),
    ("es", "Español"),
    ("fa", "Farsi"),
    ("fr", "Français"),
    ("it", "Italiano"),
    ("pl", "Polski"),
    ("pt-BR", "Português"),
    ("ru", "Русский"),
    ("tr", "Türk"),
)
LANGUAGE_CODE = "en"

LOCALE_PATHS = (os.path.join(BASE_DIR, "admin_interface/locale/"),)

ROOT_URLCONF = "tests.urls"

MEDIA_ROOT = os.path.join(BASE_DIR, "admin_interface/public/media/")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "admin_interface/public/static/")
STATIC_URL = "/static/"
