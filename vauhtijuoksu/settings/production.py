import botocore.config

from .base import *
from decouple import config, Csv
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

DEBUG = False

# Needed for django-allauth to resolve callback urls properly
ACCOUNT_DEFAULT_HTTP_PROTOCOL = config('ACCOUNT_DEFAULT_HTTP_PROTOCOL', default='https')

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
        'CONN_MAX_AGE': 600,  # in seconds
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

if config('STORAGE_BACKEND', default='') == 'upcloud':
    DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
    AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CLIENT_CONFIG=botocore.config.Config(
        request_checksum_calculation="when_required",
        response_checksum_validation="when_required"
    )
