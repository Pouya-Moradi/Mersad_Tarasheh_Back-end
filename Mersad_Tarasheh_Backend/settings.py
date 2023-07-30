"""
Django settings for Mersad_Tarasheh_Backend project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path
import pytz

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0a6-@k*s9s!%a)6439$m(hqw)$s^*0_2no!&j#@1a3qk)46ph('

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

    'azbankgateways',
    'djoser',
    'corsheaders',
    'rest_framework',

    'authentication',
    'cart',
    'order',
    'store',
    'payments'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    #...
    '127.0.0.1',
    #...
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8001',
    'http://127.0.0.1:8001',
]

ROOT_URLCONF = 'Mersad_Tarasheh_Backend.urls'

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

WSGI_APPLICATION = 'Mersad_Tarasheh_Backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mersad_tarasheh_db',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'pouya'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'authentication.User'

TIME_ZONE = 'Asia/Tehran'

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10)
}

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'authentication.serializers.UserCreateSerializer',
        'current_user': 'authentication.serializers.UserSerializer'
    }
}


AZ_IRANIAN_BANK_GATEWAYS = {
   'GATEWAYS': {
       #بانک ملی
       'BMI': {
           'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
           'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
           'SECRET_KEY': '<YOUR SECRET CODE>',
       },
       #بانک سامان
       'SEP': {
           'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
           'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
       },
       #زرین پال
       'ZARINPAL': {
           'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
           'SANDBOX': 0,  # 0 disable, 1 active
       },
       #آی دی پی
       'IDPAY': {
           'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
           'METHOD': 'POST',  # GET or POST
           'X_SANDBOX': 0,  # 0 disable, 1 active
       },
       #زیبال
       'ZIBAL': {
           'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
       },
       #باهمتا
       'BAHAMTA': {
           'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
       },
       #بانک ملت
       'MELLAT': {
           'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
           'USERNAME': '<YOUR USERNAME>',
           'PASSWORD': '<YOUR PASSWORD>',
       },
       #پی ورژن 1
       'PAYV1': {
           'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
           'X_SANDBOX': 0,  # 0 disable, 1 active
       },
   },
   'IS_SAMPLE_FORM_ENABLE': True, # اختیاری و پیش فرض غیر فعال است
   'DEFAULT': 'BMI',
   'CURRENCY': 'IRR', # اختیاری
   'TRACKING_CODE_QUERY_PARAM': 'tc', # اختیاری
   'TRACKING_CODE_LENGTH': 16, # اختیاری
   'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', # اختیاری
   'BANK_PRIORITIES': [
       'BMI',
       'SEP',
       # and so on ...
   ], # اختیاری
   'IS_SAFE_GET_GATEWAY_PAYMENT': False, #اختیاری، بهتر است True بزارید.
   'CUSTOM_APP': None, # اختیاری
}