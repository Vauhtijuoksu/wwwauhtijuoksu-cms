from .base import *
from decouple import config, Csv
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SECRET_KEY = config('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB_NAME'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT', default='5432'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
    }
}

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': config('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

if config('STORAGE_AZURE', default=True, cast=bool):
    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
    AZURE_ACCOUNT_NAME = config('STORAGE_ACCOUNT_NAME')
    AZURE_ACCOUNT_KEY = config('STORAGE_ACCOUNT_KEY')
    AZURE_CONTAINER = config('STORAGE_CONTAINER')
    AZURE_SSL = True
    AZURE_LOCATION = 'media'
