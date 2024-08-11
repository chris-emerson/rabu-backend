import os
from pathlib import Path

DEBUG = os.environ.get('DEBUG') == 'True'

#ENVRC Secrets
SECRET_KEY = os.environ.get('SECRET_KEY')

# Mapbox API is required for geocoding feature
# https://docs.mapbox.com/api/search/geocoding/
MAPBOX_API_TOKEN = os.environ.get('MAPBOX_API_TOKEN')

# This app requires a Custom Google Promgrammable Search Endpoint
# https://developers.google.com/custom-search/v1/introduction
GOOGLE_IMAGE_API_KEY = os.environ.get('GOOGLE_IMAGE_API_KEY')
GOOGLE_IMAGE_CX = os.environ.get('GOOGLE_IMAGE_CX')
    
BASE_DIR = Path(__file__).resolve().parent.parent

# CELERY SETTINGS
CELERY_BROKER_URL = 'pyamqp://127.0.0.1:5672'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TIMEZONE = 'Europe/London'

ALLOWED_HOSTS = ["127.0.0.1"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000"
]
CORS_ALLOW_HEADERS = "*"
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000"
]

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "django_celery_results",
    "planner"
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware"
,
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.AllowAny',
    ],
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',  # application/vnd.api+json
        'rest_framework.renderers.BrowsableAPIRenderer',  # text/html: ?format=api
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_json_api.filters.QueryParameterValidationFilter',  # for query parameter validation
        'rest_framework_json_api.filters.OrderingFilter',  # for sort
        'rest_framework_json_api.django_filters.DjangoFilterBackend',    # for `filter[field]` filtering
        'rest_framework.filters.SearchFilter',    # for keyword filtering across multiple fields
    ),
    'SEARCH_PARAM': 'filter[search]',
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),
}

JSON_API_FORMAT_TYPES = 'underscore'
JSON_API_PLURALIZE_TYPES = True

ROOT_URLCONF = "trabu_backend.urls"

ASGI_APPLICATION = "trabu_backend.asgi.application"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "trabu_backend.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
