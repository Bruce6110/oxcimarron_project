"""
Django settings for oxcimarron project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("BASE_DIR", BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # new
    'crispy_forms',
    'users.apps.UsersConfig',  # new
    'oxcimarron',  # this is needed in order to find oxcimarron/utils.py
    'skiing.apps.SkiingConfig',
    'reading.apps.ReadingConfig',
    'french.apps.FrenchConfig',
    'articles.apps.ArticlesConfig',
    'wordcount.apps.WordCountConfig',
    'sensors.apps.SensorsConfig',
    'techstuff.apps.TechstuffConfig'
]


CRISPY_TEMPLATE_PACK = 'bootstrap4'  # new

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oxcimarron.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # new

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oxcimarron.wsgi.application'


AUTH_USER_MODEL = 'users.CustomUser'  # new

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'oxcimarron/static/')
    # os.path.join(BASE_DIR,'static')  #for whitenoise?
]

# STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFileStorage'

# this is where CollectStatic will put things.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles') #for whitenoise
STATIC_URL = '/static/'

MEDIA_URL = '/media/'  # typical name
# "media" is the name that people typically use
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ENVIRONMENT = 'development'


# Additional settings for PRODUCTION environment
# TODO: Insert a mechanism for dynamically determining PROD/DEV environment
if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    DEBUG = False
    ALLOWED_HOSTS = []  # enter digitalocean or heroku info here
    SECURE_SSL_REDIRECT = True  # ? already handled in prod some other way?
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    


# print(traceback.extract_stack())
try:
    from .local_settings import *
    print("Imported Local Settings")

except ImportError:
    print("No Local Settings Found")
