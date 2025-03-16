from pathlib import Path
import os
from dotenv import load_dotenv

# ✅ Load Environment Variables from .env File
load_dotenv()

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")  # No fallback, force setting in .env

DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# ✅ Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Security Settings
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "change-this-in-production")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# ✅ Installed Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ Custom Apps
    'encryption_app',
    'authentication',

    # ✅ Django-Allauth for Google Authentication
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# ✅ Required for django-allauth
SITE_ID = 1

# ✅ Authentication Backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
    # ✅ REQUIRED for django-allauth
    'allauth.account.middleware.AccountMiddleware',
]

# ✅ Root URL Configuration
ROOT_URLCONF = 'encryption_project.urls'

# ✅ Templates Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'authentication/templates'],
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

# ✅ WSGI Application
WSGI_APPLICATION = 'encryption_project.wsgi.application'

# ✅ Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static & Media Files
STATIC_URL = '/static/'
#STATICFILES_DIRS = [BASE_DIR / "static"]
#STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ✅ Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Authentication & Redirects
LOGIN_URL = '/auth/login/'  
LOGIN_REDIRECT_URL = '/encryption/encrypt/'  
LOGOUT_REDIRECT_URL = "/auth/login/"

# ✅ Django-Allauth Settings
#ACCOUNT_LOGIN_METHODS = ["email"]  # ✅ Correct setting
ACCOUNT_EMAIL_VERIFICATION = "none"  # ✅ Disable email verification
#ACCOUNT_SIGNUP_FIELDS = ["email", "password1", "password2"]  # ✅ Use a list

# ✅ Google OAuth Settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }
}

# ✅ Securely Load Google OAuth Credentials
SOCIAL_AUTH_GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
SOCIAL_AUTH_GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
