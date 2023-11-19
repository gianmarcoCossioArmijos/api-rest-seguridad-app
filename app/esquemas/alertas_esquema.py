from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.modelos.alertas_modelo import ModeloAlerta


class AlertaResquestEsquema:

    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model("Crear Alerta", {
            "longitud": fields.String(required=True, max_length=30),
            "latitud": fields.String(required=True, max_length=30)
        })
    
class AlertaResponseEsquema(SQLAlchemyAutoSchema):
    
    class Meta:
        model = ModeloAlerta