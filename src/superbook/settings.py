"""
Django settings for superbook project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: BASE_DIR / "directory"
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
###from pathlib import Path
###BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

###TEMPLATE_DIRS = [str(BASE_DIR / 'templates'), ]
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
            ],
        },
    },
]

###STATICFILES_DIRS = [str(BASE_DIR / 'static'), ]

# Use 12factor inspired environment variables or from a file
import environ
root = environ.Path(BASE_DIR) - 1 # one folder back
###env = environ.Env()
env = environ.Env(DEBUG=(bool, False),)

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
###env_file = BASE_DIR.parent / 'local.env'
env_file = os.path.abspath(BASE_DIR + "/../") + '/local.env'
###if env_file.is_file():
###    environ.Env.read_env(str(env_file))
environ.Env.read_env(env_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

###TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Turn off debug while imported by Celery with a workaround
# See http://stackoverflow.com/a/4806384
import sys
if "celery" in sys.argv[0]:
    DEBUG = False

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'crispy_forms',

    'profiles',
    'posts',
    'sightings',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',)

ROOT_URLCONF = 'superbook.urls'

WSGI_APPLICATION = 'superbook.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db(),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Django Debug Toolbar
if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar.apps.DebugToolbarConfig',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',)
