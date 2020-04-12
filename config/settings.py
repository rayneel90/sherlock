"""
contain configuration settings for sherlock project
"""
import os

# set the top level project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# In order to take care of all the change in settings required between local,
# UAT and PROD environment, we create following flag
ENV = "local"  # todo: set value (local/UAT/PROD) acc to the deployment environment

# SECURITY WARNING: keep the secret key used in production secret!
if ENV == 'local':
    SECRET_KEY = 'uf@^c5^f79!52ew7q!4)%)mw*k-#apmd(fnz9%ec^d@p+-+3nc'
else:
    with open('/etc/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()  # in UAT and prod env, a large random string shall be read off a file in server
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV != 'PROD'  # False in production env, true otherwise

ALLOWED_HOSTS = ['127.0.0.1']  # todo: add ip of your server before deployment


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # todo: if you create any more app, add here
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database shall be read from a file.
# todo: store the database settings in a file named db.cnf in project root
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'db.cnf',
        },
    }
}

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static related settings
# todo: run 'py manage.py collectstatic'
STATIC_URL = '/static/'  # the url on which static files are served.
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # location where static files are stored

# media files will be stored and delivered using these settings. media is used for storing the batch files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# crispy form related settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # crispy will use bootstrap4, which is used by the rest of the project

# login_required decorator or mixin will redirect to this page
LOGIN_URL = 'cust_auth:login'

# security middleware related settings
SECURE_BROWSER_XSS_FILTER = True  # stop page from loading if cross site scripts are detected
SECURE_CONTENT_TYPE_NOSNIFF = True

# session related settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 1209600 if ENV == 'local' else 600 # session shall expire in 10 minutes for UAT and PROD
SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_SAMESITE = 'Strict'

# encryption related settings - allow only if site is being served through ssl
SESSION_COOKIE_SECURE = False if ENV == "local" else True
CSRF_COOKIE_SECURE = False if ENV == "local" else True
CSRF_COOKIE_HTTPONLY = True  # javascript can not access csrf-cookie


