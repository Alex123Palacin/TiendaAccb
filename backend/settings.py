# Tus importaciones y BASE_DIR permanecen igual
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Mantenemos el SECRET_KEY y DEBUG en modo desarrollo
SECRET_KEY = os.environ.get('SECRET_KEY', default='sdfds66fs6d6f6ds6f6')
DEBUG = 'RENDER' not in os.environ

# En modo desarrollo, incluye en ALLOWED_HOSTS localhost y 127.0.0.1
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Resto de la configuración permanece igual
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'clientes',
    'productos',
    'carritos',
    'detallecarro',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Puedes agregar rutas a tus plantillas si es necesario
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

WSGI_APPLICATION = 'backend.wsgi.application'

# Configuración de la base de datos (puede seguir igual o ajustarla si quieres otra)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TiendaAcc',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',  # localhost
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Configuración básica de idiomas y timezone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'

# Autorizaciones CORS para localhost
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000"  # Puedes agregar otros si los usas
]

# Si quieres que XDtodo funcione en tu entorno local sin tanto problema durante desarrollo, tambien puedes poner
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']