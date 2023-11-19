from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.modelos.noticias_modelo import ModeloNoticia


class NoticiaRequestEsquema:

    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model("Crear Noticia", {
            "imagen": fields.String(required=True, max_length=255),
            "titulo": fields.String(required=True, max_length=50),
            "descripcion": fields.String(required=True, max_length=120),
            "sector": fields.String(required=True, max_length=50)
        })
    
    def update(self):
        return self.ns.model("Actualizar Noticia", {
            "imagen": fields.String(required=True, max_length=255),
            "titulo": fields.String(required=True, max_length=50),
            "descripcion": fields.String(required=True, max_length=120),
            "sector": fields.String(required=True, max_length=50)
        })
    
class NoticiaResponseEsquema(SQLAlchemyAutoSchema):
    
    class Meta:
        model = ModeloNoticia