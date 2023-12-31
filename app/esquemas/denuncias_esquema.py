from flask_restx import fields

class DenunciaRequestEsquema:

    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model("Crear Denuncia", {
            "tipo": fields.String(required=True, max_length=50),
            "descripcion": fields.String(required=True, max_length=255),
            "telefono": fields.String(required=True, max_length=9),
            "ubicacion": fields.String(required=True, max_length=100),
            "id_usuario": fields.Integer(required=True),
        })