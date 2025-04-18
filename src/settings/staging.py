from .base import *

DEBUG = False

ALLOWED_HOSTS = ["staging.example.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "staging_db",
        "USER": "staging_user",
        "PASSWORD": "staging_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
