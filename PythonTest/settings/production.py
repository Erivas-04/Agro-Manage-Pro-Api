from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agro-manage-pro',
        'HOST': 'agro-manage-pro-db.c940asue891b.us-east-2.rds.amazonaws.com',
        'USER': 'adminegarcia',
        'PASSWORD': 'Admin.2024',
        'PORT': 3306
    }
}

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
