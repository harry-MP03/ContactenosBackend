# config/settings/prod.py
import dj_database_url

from .settings import *

from decouple import config

# --- CONFIGURACIÓN DE PRODUCCIÓN ---
SECRET_KEY = config('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# La configuración de la base de datos se lee del mismo .env
DATABASE_URL = config('DIRECCION_DATABASE')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}