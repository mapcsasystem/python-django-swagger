from pathlib import Path
from corsheaders.defaults import default_headers
import os
import environ
from datetime import timedelta

env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY_DEV')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG_DEV'))

DOMAIN = os.environ.get('DOMAIN_DEV')

SITE_NAME = os.environ.get('SITE_NAME_DEV')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = ['core', 'apps.api', 'apps.task']

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular'
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": env.db("DATABASE_URL_DEV", default="postgres:///db-swagger"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEV')

CORS_ALLOW_HEADERS = list(default_headers) + [
    'content-type',
]

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEV')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# PASSWORD_HASHERS = [
#     "django.contrib.auth.hashers.Argon2PasswordHasher",
#     "django.contrib.auth.hashers.PBKDF2PasswordHasher",
#     "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
#     "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
# ]


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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated'
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'API',
    'DESCRIPTION': 'Description API',
    'VERSION': '1.0.0',
    'CONTACT': {
        'name': 'miguel',
        'email': 'mapcsasystem@gmail.com',
        'url': 'http://axiacore.com'
    },
    'SWAGGER_UI_SETTINGS': {
        'persistAuthorization': True,

    },
    'USE_SESSION_AUTH': False
}

SIMPLE_JWT = {
    'ALGORITHM': 'HS254',
    'AUTH_HEADER_TYPES': ('Bearer', ),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    # 'AUTH_TOKEN_CLASS': 'rest_framework_simplejwt.token.AccessToken',
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'TOKEN_USER_CLASS': 'rest_framework.simplejwt.models.TokenUser'
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10080),
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    # 'ROTATE_REFRESFH_TOKENS': True,
    # 'BLACKLIST_AFTER_ROTATION': True,
    # 'AUTH_TOKEN_CLASSES': (
    #     'rest_framework_simplejwt.tokens.AccessToken',
    # )
}

# FILE_UPLOAD_PERMISSIONS = 0o640

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY_PROD')

    DOMAIN = os.environ.get('DOMAIN_PROD')

    SITE_NAME = os.environ.get('SITE_NAME_PROD')

    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_PROD')

    DATABASES = {
        "default": env.db("DATABASE_URL_PROD", default=env(DATABASE_URL_DEFAULT_PROD)),
    }
    DATABASES["default"]["ATOMIC_REQUESTS"] = True

    CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_PROD')

    CORS_ALLOW_HEADERS = env.list(default_headers) + [
        'contenttype',
    ]

    CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_PROD')

    DEFAULT_FROM_EMAIL = 'Uridium <mail@uridium.network>'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = env('EMAIL_HOST_PROD')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER_PROD')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD_PROD')
    EMAIL_PORT = env('EMAIL_PORT_PROD')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS_PROD')
