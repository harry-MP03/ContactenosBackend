from .settings import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'mssql',  # <-- Este es el valor correcto que estamos forzando
        'NAME': config('NAME_DATABASE'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'), # Tu contraseña real
        'HOST': config('HOST'),
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
        },
    }
}