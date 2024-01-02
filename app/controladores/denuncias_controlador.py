from app import db
from app.modelos.denuncias_modelo  import ModeloDenuncia
from http import HTTPStatus


class DenunciaControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloDenuncia

    def listar_denuncias(self):
        try:
            registros = self.model.all()
            respuesta = []
            for registro in registros:
                respuesta.append(registro.toJson())
            return respuesta, HTTPStatus.OK

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar denuncias",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def listar_denuncias_fecha(self, fecha):
        try:
            registros = self.model.where(fecha=fecha).all()
            respuesta = []
            for registro in registros:
                respuesta.append(registro.toJson())
            return respuesta, HTTPStatus.OK

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar denuncias",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def listar_denuncias_usuario(self, id_usuario):
        try:
            registros = self.model.where(id_usuario=id_usuario).all()
            respuesta = []
            for registro in registros:
                respuesta.append(registro.toJson())
            return respuesta, HTTPStatus.OK

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

    def actualizar_atendido(self, id):
        try:
            registro = self.model.where(id=id).first()
            if registro:
                registro.update(estado="atendido")
                self.db.session.add(registro)
                self.db.session.commit()
                return {
                    "mensaje": f"La denuncia con id {id} se ha actualizado como atendida"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontro denuncias del usuario con id {id}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error desabilitar denuncia por id",
                "error": str(e)
            }
        finally:
            self.db.session.close()