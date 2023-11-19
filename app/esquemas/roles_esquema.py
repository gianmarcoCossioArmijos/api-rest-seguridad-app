from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.modelos.roles_modelo import ModeloRol


class RolRequestEsquema:

    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model("Crear Rol", {
            "nombre": fields.String(required=True, max_length=15)
        })
    
    def update(self):
        return self.ns.model("Actualizar Rol", {
            "nombre": fields.String(required=True, max_length=15)
        })
    

class RolResponseEsquema(SQLAlchemyAutoSchema):
    
    class Meta:
        model = ModeloRol