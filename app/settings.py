"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import dj_database_url
import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration


load_dotenv(verbose=True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("DEBUG") == "True":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "admin.quizanthropocene.fr",
    "quiz-anthropocene.osc-fr1.scalingo.io",
]


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",  # django-cors-headers
    "anymail",  # django-anymail[sendinblue]
    "simple_history",  # django-simple-history
    "django_bootstrap5",  # django-bootstrap5
    "django_tables2",  # django-tables2
    "rest_framework",  # djangorestframework
    "drf_spectacular",  # drf-spectacular
    "django_extensions",  # django-extensions
    "import_export",  # django-import-export
    "ckeditor",  # django-ckeditor
    "fieldsets_with_inlines",  # django-fieldsets-with-inlines
    "solo",  # django-solo
    "dal",
    "dal_select2",
]

LOCAL_APPS = [
    "core",
    "users",
    "categories",
    "tags",
    "questions",
    "quizs",
    "contributions",
    "glossary",
    "api",
    "stats",
    "history",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # whitenoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # django-cors-headers
    "simple_history.middleware.HistoryRequestMiddleware",  # django-simple-history
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # custom
                "core.utils.settings_context_processors.expose_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# ------------------------------------------------------------------------------

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600)


# Authentication
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

LOGIN_URL = "auth:login"
LOGIN_REDIRECT_URL = "pages:home"
LOGOUT_REDIRECT_URL = "pages:home"

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/
# ------------------------------------------------------------------------------

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# ------------------------------------------------------------------------------

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"


# CORS
# ------------------------------------------------------------------------------

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "https://quiz-anthropocene.netlify.com",
    "https://quiz-anthropocene.netlify.app",
    "https://quiztaplanete.fr",
    "https://quizanthropocene.fr",
]

CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https:\/\/deploy-preview-\w+--quiz-anthropocene\.netlify\.app$",
]


# Security
# ------------------------------------------------------------------------------

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False if os.getenv("SESSION_COOKIE_SECURE") in ["False", False] else True
CSRF_COOKIE_SECURE = False if os.getenv("CSRF_COOKIE_SECURE") in ["False", False] else True

SECURE_SSL_REDIRECT = False if os.getenv("SECURE_SSL_REDIRECT") in ["False", False] else True
SECURE_HSTS_SECONDS = os.getenv("SECURE_HSTS_SECONDS")


# Models
# ------------------------------------------------------------------------------

AUTH_USER_MODEL = "users.User"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Django Simple History
# https://django-simple-history.readthedocs.io/
# ------------------------------------------------------------------------------

SIMPLE_HISTORY_HISTORY_ID_USE_UUID = True


# Emails
# ------------------------------------------------------------------------------

SIB_API_KEY = os.getenv("SIB_API_KEY")
ANYMAIL = {
    "SENDINBLUE_API_KEY": SIB_API_KEY,
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
if not DEBUG:
    EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"

DEFAULT_FROM_EMAIL = "Quiz de l'Anthropocène <noreply@quizanthropocene.fr>"
DEFAULT_FROM_NAME = "Quiz de l'Anthropocène"
SERVER_EMAIL = os.getenv("TECH_EMAIL")
ADMINS = eval(os.getenv("ADMINS", "[]"))

SIB_CONTRIBUTOR_LIST_ID = os.getenv("SIB_CONTRIBUTOR_LIST_ID")
SIB_NEWSLETTER_LIST_ID = os.getenv("SIB_NEWSLETTER_LIST_ID")
SIB_NEWSLETTER_DOI_TEMPLATE_ID = os.getenv("SIB_NEWSLETTER_DOI_TEMPLATE_ID")
SIB_CONTACT_ENDPOINT = "https://api.sendinblue.com/v3/contacts"
SIB_CONTACT_DOI_ENDPOINT = "https://api.sendinblue.com/v3/contacts/doubleOptinConfirmation"


# Errors
# https://glitchtip.com/
# ------------------------------------------------------------------------------

if not DEBUG:
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_GLITCHTIP_DSN"),
        integrations=[DjangoIntegration()],
        auto_session_tracking=False,
        traces_sample_rate=0,
    )


# Object storage : Scaleway (S3-like)
# ------------------------------------------------------------------------------

S3_ENDPOINT = os.getenv("S3_ENDPOINT")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_BUCKET_REGION = os.getenv("S3_BUCKET_REGION")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")

QUESTION_FOLDER_NAME = "questions"
QUIZ_FOLDER_NAME = "quizs"


# Django Bootstrap5
# https://django-bootstrap5.readthedocs.io/
# ------------------------------------------------------------------------------

BOOTSTRAP5 = {
    "required_css_class": "form-group-required",
    "set_placeholder": False,
    # Label class to use in horizontal forms.
    "horizontal_label_class": "col-4 col-sm-2",  # "col-sm-2"
    # Field class to use in horizontal forms.
    "horizontal_field_class": "col-8 col-sm-10",  # "col-sm-10"
}


# Django Tables2
# https://django-tables2.readthedocs.io/
# ------------------------------------------------------------------------------

DJANGO_TABLES2_PAGE_RANGE = 5


# Django REST Framework (DRF)
# https://www.django-rest-framework.org/
# ------------------------------------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DATETIME_FORMAT": "%Y-%m-%d",
}


# DRF Spectacular
# https://drf-spectacular.readthedocs.io/en/latest/settings.html
# ------------------------------------------------------------------------------


# Django Debug Toolbar
# https://django-debug-toolbar.readthedocs.io/
# ------------------------------------------------------------------------------

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]  # django-debug-toolbar
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = ["127.0.0.1"]


# Django Import Export
# ------------------------------------------------------------------------------

IMPORT_EXPORT_SKIP_ADMIN_LOG = True


# Shell Plus
# ------------------------------------------------------------------------------

SHELL_PLUS = "ipython"
SHELL_PLUS_IMPORTS = [
    "import csv, json, yaml",
    "from datetime import datetime, date, timedelta",
    "from core import constants",
    "from core.utils import utilities, notion, github, sendinblue, s3",
    "from stats import utilities as utilities_stats",
]


# Github
# ------------------------------------------------------------------------------

GITHUB_BACKEND_REPO = "quiz-anthropocene/admin-backend"
GITHUB_FRONTEND_REPO = "quiz-anthropocene/public-frontend"
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
GITHUB_CRON_ACTION_TOKEN = os.getenv("GITHUB_CRON_ACTION_TOKEN")


# Notion.so
# ------------------------------------------------------------------------------

NOTION_API_SECRET = os.getenv("NOTION_API_SECRET")
NOTION_API_VERSION = "2021-08-16"
NOTION_QUESTION_TABLE_ID = os.getenv("NOTION_QUESTION_TABLE_ID")
NOTION_CONTRIBUTION_TABLE_ID = os.getenv("NOTION_CONTRIBUTION_TABLE_ID")

NOTION_TOKEN_V2 = os.getenv("NOTION_TOKEN_V2")
NOTION_QUESTIONS_TABLE_URL = os.getenv("NOTION_QUESTIONS_TABLE_URL")
NOTION_CONTRIBUTION_TABLE_URL = os.getenv("NOTION_CONTRIBUTION_TABLE_URL")
NOTION_IMPORT_STATS_TABLE_URL = os.getenv("NOTION_IMPORT_STATS_TABLE_URL")
NOTION_GLOSSARY_TABLE_URL = os.getenv("NOTION_GLOSSARY_TABLE_URL")


# django-ckeditor
# ------------------------------------------------------------------------------

CKEDITOR_CONFIGS = {
    "default": {
        "height": 200,
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline"],
            ["NumberedList", "BulletedList"],
            ["Link", "Unlink"],
            ["SpecialChar"],
            # ['HorizontalRule', 'Smiley'],
            ["Undo", "Redo"],
            ["RemoveFormat", "Source"],
        ],
        # avoid special characters encoding
        "basicEntities": False,
        "entities": False,
    }
}


# Misc
# ------------------------------------------------------------------------------

METABASE_GENERAL_DASHBOARD_PUBLIC_URL = os.getenv("METABASE_GENERAL_DASHBOARD_PUBLIC_URL", "")
METABASE_QUIZ_DASHBOARD_PUBLIC_URL = os.getenv("METABASE_QUIZ_DASHBOARD_PUBLIC_URL", "")
