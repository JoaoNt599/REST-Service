from .base import *

DEBUG = False

ALLOWED_HOSTS = ["example.com", "www.example.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "prod_db",
        "USER": "prod_user",
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": "db.example.com",
        "PORT": "5432",
    }
}
