"""
Django settings for vauhtijuoksu project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8uvqb1l%txv#3u56j&@3#d8z8abp2e3$jqife%8@ze8djlj&dc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []

# Required for django.contrib.sites

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cms',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_text_ckeditor',
    'menus',
    'treebeard',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'mptt',
    'sass_processor',
    'bootstrap5',
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'vauhtijuoksu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

# List of templates that can be used for CMS pages
CMS_TEMPLATES = [
    ('vauhtijuoksu/vj2021plus.html', 'VJ 2021+ theme'),
    ('vauhtijuoksu/vj2021.html', 'VJ 2021 theme'),
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

WSGI_APPLICATION = 'vauhtijuoksu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = [
    ('en', 'English'),
    ('fi', 'Suomi')
]

CMS_LANGUAGES = {
    1: [
        {
            'code': 'fi',
            'name': 'Suomi',
            'public': True,
            'fallbacks': ['en']
        }
    ]
}

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATICFILES_STORAGE ='whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = config('DJANGO_STATIC_URL', default='/static/')
STATIC_ROOT = config('DJANGO_STATIC_ROOT', default=BASE_DIR / 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'node_modules' / 'bootstrap' / 'dist' / 'js',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

# Include node_modules to import Bootstrap styles in SASS
SASS_PROCESSOR_INCLUDE_DIRS = [
    str(BASE_DIR / 'node_modules')
]

SASS_PRECISION = 8

# Media

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'