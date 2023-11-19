from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS

from app.configuracion import entorno;


ENVIRONMENT = entorno[getenv("FLASK_ENV")]

app = Flask(__name__)
app.config.from_object(ENVIRONMENT)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)
cors = CORS(app)

authorizations = {
    "Bearer": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

api = Api(
    app,
    title='Alerta Jaen',
    version='0.1',
    description='Rutas de App',
    doc='/documentacion',
    authorizations=authorizations
)