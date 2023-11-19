from app.modelos.zonas_modelo import ModeloZona
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_restx import fields


class ZonaRequestEsquema:
    
    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model("Crear Zona", {
            "nombre": fields.String(required=True, max_length=50)
        })
    
    def update(self):
        return self.ns.model("Actualizar Zona", {
            "nombre": fields.String(required=True, max_length=50)
        })


class ZonaResponseEsquema(SQLAlchemyAutoSchema):
    class Meta:
        model = ModeloZona