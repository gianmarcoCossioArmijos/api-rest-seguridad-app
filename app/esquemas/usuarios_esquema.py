from flask_restx import fields

class UsuarioRequestEsquema:
    
    def __init__(self, namespace):
        self.ns = namespace
    
    def create(self):
        return self.ns.model("Crear Usuario", {
            "nombres": fields.String(required=True, max_length=150),
            "nacimiento": fields.String(required=True),
            "email": fields.String(required=True, max_length=100),
            "telefono": fields.String(required=True, max_length=9),
            "clave": fields.String(required=True, max_length=255),
            "direccion": fields.String(required=True, max_length=50),
            "rol_id": fields.Integer(required=True)
        })
    
    def update(self):
        return self.ns.model("Actualizar Usuario", {
            "nombres": fields.String(required=True, max_length=150),
            "telefono": fields.String(required=True, max_length=9),
            "direccion": fields.String(required=True, max_length=50),
        })