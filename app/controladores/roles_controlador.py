from app import db
from app.modelos.roles_modelo import ModeloRol
from app.esquemas.roles_esquema import RolResponseEsquema
from http import HTTPStatus


class RolControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloRol
        self.esquema = RolResponseEsquema

    def listar_todos(self):
        try:
            registros = self.model.where(estado=True).all()
            respuesta = self.esquema(many=True)
            return respuesta.dump(registros), HTTPStatus.OK
        except Exception as e:
            return {
                "mensaje": f"Ocurrio un error al listar roles",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
    
    def registrar(self, datos):
        try:
            nuevo_registro = self.model.create(**datos)
            self.db.session.add(nuevo_registro)
            self.db.session.commit()
            return {
                "mensaje": f"El rol {datos['nombre']} se creo exitosamente"
            }, HTTPStatus.CREATED
        
        except Exception as e:
            self.db.session.rollback()
            return {
                "mensaje": "Ocurrio un error al crear nuevo rol",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def encontrar_por_id(self, id):
        try:
            registro = self.model.where(estado=True, id=id).first()
            if (registro):
                respuesta = self.esquema(many=False)
                return respuesta.dump(registro), HTTPStatus.OK
            return {
                "mensaje": f"No se encontro un rol con id {id}"
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar rol",
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
                    "mensaje": f"El rol con id {id} se ha actualizado"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontro el rol on id {id}"
            }, HTTPStatus.INTERNAL_SERVER_ERROR

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al actualizar rol",
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
                    "mensaje": f"El rol con id {id} se ha eliminado"
                }, HTTPStatus.NO_CONTENT
            return {
                "mensaje": f"No se encontro el rol con id {id}",
                "error": str(e)
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al eliminar rol",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()