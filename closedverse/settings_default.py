"""
Django settings for closedverse project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY="secret"

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
    
    'markdown_deux',
    'closedverse_main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'closedverse_main.middleware.ClosedMiddleware',
]

ROOT_URLCONF = 'closedverse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'closedverse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = None


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

# Disable internationalization because Closedverse doesn't use it
USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Define static files in the base directory
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

# Closedverse models and routes for Django
AUTH_USER_MODEL = 'closedverse_main.User'
CSRF_FAILURE_VIEW = 'closedverse_main.views.csrf_fail'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/login/'

# User-uploaded media paths for Closedverse
MEDIA_URL = '/media/'
# Must end with a trailing slash
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Settings for markdown_deux, a module
# that Closedverse uses in user messages
MARKDOWN_DEUX_STYLES = {
    'default': {
        'extras': {
            'code-friendly': None,
        },
        'safe_mode': 'escape',
    },
}
# Settings unique to Closedverse

# This option enables some production-specific pages
# and routines, such as HTTPS scheme redirection and
# proxy detection via IPHub.
CLOSEDVERSE_PROD = False

# Initialize version and Git URL
CLOSEDVERSE_GIT_VERSION = 'unknown'
CLOSEDVERSE_GIT_URL = ''
CLOSEDVERSE_GIT_HAS_CHANGES = False

# Only set git version/URL if .git folder exists
if os.path.isdir(os.path.join(BASE_DIR, '.git')):
    # Get version from Git. This is shown in the layout
    git_process = os.popen('git rev-parse HEAD', 'r')
    CLOSEDVERSE_GIT_VERSION = git_process.read()[:-1]

    # if this command returns a non-zero exit code, then
    # there have been some changes so let's indicate that
    if os.system('git diff-index --quiet HEAD --'):
        CLOSEDVERSE_GIT_HAS_CHANGES = True

    git_process = os.popen('git remote get-url origin', 'r')
    CLOSEDVERSE_GIT_URL = git_process.read()[:-1]

    try:
        git_url_without_ext = CLOSEDVERSE_GIT_URL.split('.git')[0]
    except IndexError:
        pass
    else:
        CLOSEDVERSE_GIT_URL = git_url_without_ext + '/commit/' + CLOSEDVERSE_GIT_VERSION

# Google reCAPTCHA (v2) settings
# This feature won't work if these fields are not populated.
RECAPTCHA_PUBLIC_KEY = None
RECAPTCHA_PRIVATE_KEY = None

# Key for IPHub service for Closedverse, which detects proxies.
IPHUB_KEY = None
# If this is set to True, then users will receive an error
# upon trying to sign up for the site behind a proxy.
# Uses IPHub service and requires an API key defined above.
DISALLOW_PROXY = False

# Setting this to True forces every user to log in/
# sign up for the site to view any content.
FORCE_LOGIN = False
# A list of URLs that are always accessible
# whether the above value is set or not.
LOGIN_EXEMPT_URLS = {
    r'^login/$',
    r'^signup/$',
    r'^logout/$',
    r'^reset/$',
    r'^help/rules$',
    r'^help/contact$',
    r'^help/login$',
}

# Action to perform on images belonging to posts/
# comments when they are deleted
# 0: keep, 1: move to 'rm' folder, 2: delete
IMAGE_DELETE_SETTING = 2

# List of NNIDs that aren't allowed to be used on the site.
NNID_FORBIDDEN_LIST = os.path.join(BASE_DIR, 'forbidden.json')