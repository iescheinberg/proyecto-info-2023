from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
ALLOWED_HOSTS = ['iescheinberg.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#ESTA ES LA CONFIGURACION PARA BD SQLITE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}