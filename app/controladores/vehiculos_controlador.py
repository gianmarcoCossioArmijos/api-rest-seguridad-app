from app import db
from app.modelos.vehiculos_modelo import ModeloVehiculo
from app.esquemas.vehiculos_esquema import VehiculoResponseEsquema
from http import HTTPStatus


class VehiculoControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloVehiculo
        self.esquema = VehiculoResponseEsquema

    def listar_todos(self):
        try:
            registros = self.model.where(estado=True).all()
            respuesta = self.esquema(many=True)
            return respuesta.dump(registros), HTTPStatus.OK
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar vehiculos",
                "error": str(e)
            }
        
    def registrar(self, datos):
        try:
            nuevo_registro = self.model.create(**datos)
            self.db.session.add(nuevo_registro)
            self.db.session.commit()
            return {
                "mensaje": f"El vehiculo {datos['placa']} ha sido registrado exitosamente"
            }, HTTPStatus.CREATED
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar vehiculo",
                "error": str(e)
            }
        
        finally:
            self.db.session.close()

    def encontrar_por_id(self, id):
        try:
            registro = self.model.where(estado=True, id=id).first()
            if registro:
                respuesta = self.esquema(many=False)
                return respuesta.dump(registro), HTTPStatus.OK
            return {
                "mensaje": f"No se ha encontrado al vehiculo con id {id}"
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un errir al listar vehiculo por id",
                "error": str(e)
            }
        
    def actualizar(self, id, datos):
        try:
            registro = self.model.where(estado=True, id=id).first()
            if registro:
                registro.update(**datos)
                self.db.session.add(registro)
                self.db.session.commit()
                return {
                    "mensaje": f"El vehiculo con id {id} se actualizado"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se ha encontrado al vehiculo con id {id}"
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar vehiculo por id",
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
                    "mensaje": f"El vehiculo con {id} se eliminado exitosamente",
                }, HTTPStatus.NO_CONTENT
            return {
                "mensaje": "Ocurrio un error al eliminar vehiculo",
                "error": str(e)
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al eliminar vehiculo",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()