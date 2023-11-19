from app import db
from app.modelos.zonas_modelo import ModeloZona
from app.esquemas.zonas_esquema import ZonaResponseEsquema
from http import HTTPStatus


class ZonaControlador:
    
    def __init__(self):
        self.db = db
        self.model = ModeloZona
        self.esquema = ZonaResponseEsquema

    def listar_todos(self):
        try:
            registros = self.model.where(estado=True).all()
            respuesta = self.esquema(many=True)
            return respuesta.dump(registros), HTTPStatus.OK
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar zonas",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def registrar(self, datos):
        try:
            nuevo_registro = self.model.create(**datos)
            self.db.session.add(nuevo_registro)
            self.db.session.commit()
            return {
                "mansaje": f"La zona {datos['nombre']} fue creada exitosamente"
            }, HTTPStatus.CREATED
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar zona",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def encontrar_por_id(self, id):
        try:
            registro = self.model.where(estado=True, id=id).first()
            if registro:
                respuesta = self.esquema(many=False)
                return respuesta.dump(registro), HTTPStatus.OK
            return {
                "Mensaje": f"No se encontro la zona con id {id}"
            }, HTTPStatus.OK
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar zona",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def actualizar(self, id, datos):
        try:
            registro = self.model.where(estado=True, id=id).first()
            if registro:
                registro.update(**datos)
                self.db.session.add(registro)
                self.db.session.commit()
                return {
                    "mensaje": f"La zona con id {id} fue actualizada"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontro la zona con id {id}"
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al actulizar zona por id",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()

    def eliminar(self, id):
        try:
            registro = self.model.where(estado=True, id=id).first()
            if registro:
                registro.update(estado=False)
                self.db.session.add(registro)
                self.db.session.commit()
                return {
                    "mensaje": f"La zona con id {id} fue eliminada"
                }, HTTPStatus.NO_CONTENT
            return {
                "mensaje:" f"No se encontro la zona con id {id}"
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al eliminar zona",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()