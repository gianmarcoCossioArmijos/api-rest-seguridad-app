from app import db
from app.modelos.usuarios_modelo import ModeloUsuario
from http import HTTPStatus


class UsurioControlador:
    def __init__(self):
        self.db = db
        self.model = ModeloUsuario

    def listar_todos(self):
        try:
            registros = self.model.where(estado=True).all()
            response = []
            for registro in registros:
                response.append(registro.toJson())
            return response, HTTPStatus.OK
        except Exception as e:
            return {
                "mensaje": f"Ocurrio un error al listar usuarios",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def registrar(self, datos):
        try:
            email = datos["email"]
            registro = self.model.where(email=email).first()
            if registro:
                return {
                    "mensaje": "El usuario ya se encuentra registrado"
                }, HTTPStatus.BAD_REQUEST
            nuevo_registro = self.model.create(**datos)
            nuevo_registro.hash_clave()
            self.db.session.add(nuevo_registro)
            self.db.session.commit()
            return {
                "mensaje": f"El usuario {datos['nombres']} ha sido registrado con exito"
            }, HTTPStatus.CREATED
        
        except Exception as e:
            return {
                "mensaje": f"Ocurrio un error al registrar usuario",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def encontrar_por_id(self, id):
        try:
            registro = self.model.where(estado=True, id=id).first()
            if registro:
                return registro.toJson(), HTTPStatus.OK
            return {
                "mensaje": f"No se encontro al usuario con id {id}"
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar usuario por id",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def encontrar_por_email(self, email):
        try:
            registro = self.model.where(estado=True, email=email).first()
            if registro:
                return registro.toJson(), HTTPStatus.OK
            return {
                "mensaje": f"No se encontro al usuario con email {email}"
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar usuario por email",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def actualizar(self, id, datos):
        try:
            registro = self.model.where(estado=True, id=id).first()
            if registro:
                registro.update(**datos)
                self.db.session.add(registro)
                self.db.session.commit()
                return {
                    "mensaje": f"El Usuario con id {id} se ha actualizado"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontro al usuario con id {id}"
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al actualizar usuario por id",
                "error": str(e)
            }
        
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
                    "mensaje": f"El Usuario con id {id} se ha eliminado"
                }, HTTPStatus.NO_CONTENT
            return {
                "mensaje": f"No se encontro al usuario con id {id}"
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al eliminar usuario por id",
                "error": str(e)
            }
        
        finally:
            self.db.session.close()