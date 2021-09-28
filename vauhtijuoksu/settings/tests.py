from .base import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3'
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
