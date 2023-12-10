from os import getenv
from datetime import timedelta


class ConfiguracionBase:

    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('SECRET_KEY')
    MAIL_SERVER = getenv('MAIL_SERVER')
    MAIL_PORT = getenv('MAIL_PORT')
    MAIL_USE_TLS = getenv('MAIL_USE_TLS')
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')


class ConfiguracionDesarrollo(ConfiguracionBase):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=3)
    MAIL_DEBUG = True


class ConfiguracionProduccion(ConfiguracionBase):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=8)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=10)
    MAIL_DEBUG = False
    PROPAGATE_EXCEPTIONS = True


entorno = {
    'desarrollo': ConfiguracionDesarrollo,
    'produccion': ConfiguracionProduccion
}