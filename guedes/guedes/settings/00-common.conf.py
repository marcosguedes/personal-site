import os
import sys

gettext = lambda s: s
PROJECT_PATH = os.path.join(os.path.realpath(os.path.dirname(__file__)), '../')

# add apps folders
for d in ['plugins', 'apps', 'lib']:
    sys.path.insert(0, os.path.join(PROJECT_PATH, '../', d))

DEBUG = True

ADMINS = (
    ('Marcos', 'marcos@guedes.com.pt'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',  # Or path to database file if using sqlite3.
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Lisbon'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (('en', _('English')),)

LOCALE_PATHS = (os.path.join(PROJECT_PATH, '../locale/'), )

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/queo.pt/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, '../../media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://queo.pt/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/queo.pt/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '../static/')

# URL prefix for static files.
# Example: "http://queo.pt/static/"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    ('site', os.path.join(PROJECT_PATH, 'static/')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dummy-secret-key'


TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(PROJECT_PATH, "templates"), ],
    #'APP_DIRS': True,
    'OPTIONS': {'context_processors': ['django.contrib.auth.context_processors.auth',
                                       'django.contrib.messages.context_processors.messages',
                                       'django.template.context_processors.debug',
                                       'django.template.context_processors.i18n',
                                       'django.template.context_processors.media',
                                       'django.template.context_processors.static',
                                       'django.template.context_processors.request',
                                       'guedes.context_processors.is_debug',
                                       'sekizai.context_processors.sekizai',
                                       ],
                'loaders': [('django.template.loaders.cached.Loader', ['django.template.loaders.filesystem.Loader',
                                                                       'django.template.loaders.app_directories.Loader',
                                                                       ]),
                            ],
                },

}]


MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
INTERNAL_IPS = ('127.0.0.1',)
ROOT_URLCONF = 'guedes.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'guedes.wsgi.application'


GOOGLE_ANALYTICS_MODEL = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flat',
    'django.contrib.admin',

    'compressor',
    'sekizai',
    'robots',
    'colorful',
    'easy_thumbnails',
    'filer',
    'ckeditor',
    'ckeditor_uploader',
    'solo',
    
    'aboutme',
    'blog',
    'personalsite',
    'cookiedisclaimer',
    'randomfunctionalities',
]


APPEND_SLASH = True

# Silences Deprecation warning about GoogleAnalytics Site unique foreignKey
SILENCED_SYSTEM_CHECKS = ["fields.W342"]

# COMPRESSOR
COMPRESS_ENABLED = True

DEFAULT_FROM_EMAIL = '@guedes.com.pt'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '@guedes.com.pt'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOG_DIR = os.path.join(PROJECT_PATH, '../logs')
try:
    os.mkdir(LOG_DIR)
except Exception as ex:
    pass


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_PATH, '../logs/default.log'),
            'maxBytes': 1024 * 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        # uncomment this to enable root log
        #'': {
        #    'handlers': ['default'],
        #    'level': 'DEBUG',
        #    'propagate': False
        #},
        #'django.db': {
        #    # django also has database level logging
        #},
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

    }
}
