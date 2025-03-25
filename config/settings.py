import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9g4_@r*l&bw(ngafy$%q4u@zvm(t))-i-f^99h@kk3i6zuo(+s'
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

    # Third-party apps
    "allauth",
    "allauth.account",
    "crispy_forms",
    "crispy_tailwind",

    # apps
    'app',
    'users.apps.UsersConfig',

    # Dev tools
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # Required by django-allauth
    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "app/templates/app/account",
        ],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTH_USER_MODEL = "users.User"


# ACCOUNT_AUTHENTICATION_METHOD = "email"  # Use email for authentication
# # ACCOUNT_EMAIL_REQUIRED = True  # Ensure email is required
# ACCOUNT_USERNAME_REQUIRED = False  # Disable username requirement
# ACCOUNT_SIGNUP_FIELDS = ["email", "password1", "password2"]  # Corrected fields
# # ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # Email verification is required
# # ACCOUNT_LOGIN_METHODS = {"email"}  # New format for Django 5.x

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']  
ACCOUNT_LOGIN_METHODS = {'email'} 
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*'] 
ACCOUNT_EMAIL_VERIFICATION = "mandatory"



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = "app:dashboard_landing_page"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
