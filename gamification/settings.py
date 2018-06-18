"""
Django settings for gamification project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
# import env                                                                      ## comment out for testing purposes & for heroku deployment
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

## Swap secret keys for testing purposes
# SECRET_KEY = "SecretKeyForUseOnTravis"                                        ## activate for travis ci
SECRET_KEY = os.environ.get('SECRET_KEY')                                       ## comment out for testing purposes

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False                                                                   ## swap for heroku

## C9 HOST
ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME'), 'projectgamification.herokuapp.com']        ## add heroku for hosting



# Application definition

INSTALLED_APPS = [
    'projects',
    'accounts',
    'charity_choice',
    'charity_donation',
    'storages',                                                                 ## for S3 image hosting
    'django_forms_bootstrap',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'                                                   ## allow stats
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gamification.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],                          
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'charity_choice.contexts.donation_contents'
            ],
        },
    },
]

WSGI_APPLICATION = 'gamification.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


## HEROKU DB as priority for hosting, else - sqlite3 local DB

if "DATABASE_URL" in os.environ:        
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    print("Database URL not found. USing SQLite instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.CaseInsensitiveAuth']
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

###### AWS S3 CONFIG ###########################################################

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Fri, 31 Dec 2055 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
    
}

AWS_STORAGE_BUCKET_NAME = 'project-gamification'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")                         ## hidden
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")                 ## hidden

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME          



STATICFILES_LOCATION = 'static'                                                 ## comment out for testing
STATICFILES_STORAGE = 'custom_storages.StaticStorage'                           ## comment out for testing


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )

MEDIAFILES_LOCATION = 'media'                                                   ## comment out for testing
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'                           ## comment out for testing

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)      ## comment out for testing
# MEDIA_URL = '/media/'                                                         ## activate for testing

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
