from app import db
from app.modelos.denuncias_modelo  import ModeloDenuncia
from app.esquemas.denuncias_esquema import DenunciaResponseEsquema
from http import HTTPStatus


class DenunciaControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloDenuncia
        self.esquema = DenunciaResponseEsquema

    def listar_denuncias(self, fecha):
        try:
            registros = self.model.where(fecha=fecha).all()
            respuesta = self.esquema(many=True)
            return respuesta.dump(registros), HTTPStatus.OK

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar denuncias",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def registrar(self, datos):
        try:
            nuevo_registro = self.model.create(**datos)
            self.db.session.add(nuevo_registro)
            self.db.session.commit()
            return {
                "mensaje": "La denuncia se registro exitosamente"
            }, HTTPStatus.CREATED

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar denuncia",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def encontrar_por_id(self, id):
        try:
            registros = self.model.where(id_usuario=id).all()
            if registros:
                respuesta = self.esquema(many=True)
                respuesta.dump(registros), HTTPStatus.OK
            return {
                "mensaje": f"No se encontro denuncias del usuario con id {id}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error listar denuncias por id",
                "error": str(e)
            }