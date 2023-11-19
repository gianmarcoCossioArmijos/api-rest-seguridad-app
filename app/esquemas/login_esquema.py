from flask_restx import fields
from flask_restx.reqparse import RequestParser


class LoginRequestEsquema:

    def __init__(self, namespace):
        self.ns = namespace

    def login(self):
        return self.ns.model("Iniciar Sesion", {
            "email": fields.String(required=True, max_length=50),
            "clave": fields.String(required=True, max_length=20)
        })
    
    def refresh(self):
        parser = RequestParser()
        parser.add_argument("Authorization",
                            type=str,
                            location="headers",
                            help="refresh token")
        return parser
    
    def reset(self):
        return self.ns.model("Reseteo de Contraseña", {
            "email": fields.String(required=True)
        })