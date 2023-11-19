from app.modelos.vehiculos_modelo import ModeloVehiculo
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_restx import fields


class VehiculoRequestEsquema:

    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model("Crear Vehiculo", {
            "tipo": fields.String(required=True, max_length=50),
            "placa": fields.String(required=True, max_length=10),
            "marca": fields.String(required=True, max_length=50),
            "modelo": fields.String(required=True, max_length=100),
            "año": fields.Date(required=True),
        })
    
    def update(self):
        return self.ns.model("Actulizar Vehiculo", {
            "tipo": fields.String(required=True, max_length=50),
            "placa": fields.String(required=True, max_length=10),
            "marca": fields.String(required=True, max_length=50),
            "modelo": fields.String(required=True, max_length=100),
            "año": fields.Date(required=True),
        })

class VehiculoResponseEsquema(SQLAlchemyAutoSchema):
    class Meta:
        model = ModeloVehiculo