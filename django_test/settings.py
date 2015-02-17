# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import dj_database_url 

PROJECT_DIRECTORY = os.getcwd()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n%_s8-xtab-idlj8*mmny7uzf73@x%nvqrsqbf&(%jf_khu+7v'

# List of callables that know how to import templates from various sources. 
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#   'django.template.loaders.eggs.Loader',
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 
#TEMPLATE_DEBUG = DEBUG
TEMPLATE_DEBUG = True

ADMINS = (
    ('Deanna Robertazzi', 'deanna.robertazzi@gmail.com')
)

MANAGERS = ADMINS 

ALLOWED_HOSTS = []

EMAIL_HOST = 'localhost'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'article',
    'tastypie',
    'django.contrib.formtools',
    'userprofile',
    'storages',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins':{
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
         'django.request': {
             'handlers': ['mail_admins'],
             'level': 'ERROR',
             'propogate': True,
         },
    }
}
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_test.urls'

WSGI_APPLICATION = 'django_test.wsgi.application'

TEMPLATE_DIRS = ('/home/deanna/django_test/templates',
                 'home/deanna/django_test/articles/templates',)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
    
    
    #'default': { #Good for offline work
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': '/home/deanna/django_test/storage.db',
    #}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = '/assets/'

MEDIA_URL = ''


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_DIRECTORY, 'static/')

STATICFILES_DIRS = ('assets', os.path.join(os.getcwd(), 'static//')),

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
SITE_ID = 1

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

UPLOAD_FILE_PATTERN = "assets/upload_files/%s_%s"

try:
    from local_settings import *
except Exception as e:
    print e.message 
    
if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/assets/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL