from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.modelos.unidades_modelo import ModeloUnidad


class UnidadRequestEsquema:

    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model("Crear Unidad", {
            "codigo": fields.String(required=True, max_length=50),
            "tipo_unidad": fields.String(required=True, max_length=50),
            "chofer": fields.String(required=False, max_length=120),
            "policia": fields.String(required=False, max_length=120),
            "operador": fields.String(required=False, max_length=120),
            "agentes": fields.String(required=True, max_length=120),
            "descripcion": fields.String(required=True, max_length=255),
            "id_zona": fields.Integer(required=True),
            "id_vehiculo": fields.Integer(required=False)
        })
    
    def update(self):
        return self.ns.model("Actualizar Unidad", {
            "codigo": fields.String(required=True, max_length=50),
            "tipo_unidad": fields.String(required=True, max_length=50),
            "chofer": fields.String(required=False, max_length=120),
            "policia": fields.String(required=False, max_length=120),
            "operador": fields.String(required=False, max_length=120),
            "agentes": fields.String(required=True, max_length=120),
            "descripcion": fields.String(required=True, max_length=255)
        })
    
class UnidadResponseEsquema(SQLAlchemyAutoSchema):

    class Meta:
        model = ModeloUnidad