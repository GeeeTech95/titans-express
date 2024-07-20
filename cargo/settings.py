import dj_database_url
import os
import pdfkit
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '24q_*&tn+5k_*6h6$nsccghwwb#8b%v4i)1h(wd08_02_-(czt'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO"},
    },
}


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Titans Express Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Titans Express",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Titans Express",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "main/img/logo-jazz.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "main/img/logo-jazz.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "logo",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "logo",

    "custom_css": "css/style.css",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    #"site_icon": "img/favicon.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome Admin!",

    # Copyright on the footer
    "copyright": "Titans Express",
}



# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Users.apps.UsersConfig',
    'company.apps.CompanyConfig',
    'core.apps.CoreConfig',
    'myadmin.apps.MyadminConfig',
    'logistics.apps.LogisticsConfig',
    'crispy_forms',

    #3rd party
    'whitenoise.runserver_nostatic',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'cargo.urls'

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'), 
            os.path.join(BASE_DIR,'Users/templates'), 
            os.path.join(BASE_DIR,'core/templates'), 
            os.path.join(BASE_DIR,'core/templates/email'), 
            os.path.join(BASE_DIR,'templates/registration'),
            os.path.join(BASE_DIR,'core/templates/email/logistics'),
            os.path.join(BASE_DIR,'templates/admin dashboard'),  
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'core.context.core',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cargo.wsgi.application'

AUTH_USER_MODEL = 'Users.User'
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



if DEBUG :
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            "OPTIONS": {
                "timeout": 30,
            }
        },
        "OPTIONS": {
        # ...
        "timeout": 30,
        # ...
    }
    }

else :
    # Replace the SQLite DATABASES configuration with PostgreSQL:
    DATABASES = {
   'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

"""
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
"""


#EMAIL FOR ZOHO
EMAIL_HOST  = "smtp.zoho.com"
EMAIL_HOST_USER_TRANSACTION = "logistics@titansexpress.com"
EMAIL_HOST_USER_LOGISTICS = "logistics@titansexpress.com"
EMAIL_HOST_USER_SUPPORT = "support@titansexpress.com"
PASSWORD = "!@pdt7gu123!!X"

#TAWKTO
EMAIL = "chukwudipeter97@gmail.com"
PASSWORD = "!@pdt7gu123!!X" 


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")

STATICFILES_DIRS = [

os.path.join(BASE_DIR,"static")
]

SITE_NAME = "Titan Express"


if DEBUG : 
    SITE_URL = "http://127.0.0.4:4000"
else :
    SITE_URL  = "https://www.titansexpress.com"  


STATIC_ROOT = os.path.join(BASE_DIR,"asset")

STATIC_URL = '/static/'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
 



PDFKIT_CONFIG =  pdfkit.configuration(wkhtmltopdf="") #pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_CMD', '/usr/local/bin/wkhtmltopdf'))

