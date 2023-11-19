from app import db
from app.modelos.alertas_modelo  import ModeloAlerta
from app.esquemas.alertas_esquema import AlertaResponseEsquema
from http import HTTPStatus


class AlertaControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloAlerta
        self.esquema = AlertaResponseEsquema

    def listar_pendientes(self):
        try:
            registros = self.model.where(estado="pendiente").all()
            respuesta = self.esquema(many=True)
            return respuesta.dump(registros), HTTPStatus.OK
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar alertas",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def registrar(self, datos):
        try:
            nuevo_registro = self.model.create(**datos)
            self.db.session.add(nuevo_registro)
            self.db.session.commit()
            return {
                "mensaje": "La alerta se registro exitosamente"
            }, HTTPStatus.CREATED
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar alerta",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def encontrar_por_id(self, id):
        try:
            registro = self.model.where(id=id).first()
            if registro:
                respuesta = self.esquema(many=False)
                return respuesta.dump(registro), HTTPStatus.OK
            return {
                "mensaje": f"No se encontro con el id {id}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar alerta por id",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def encontrar_por_fecha(self, fecha):
        try:
            registro = self.model.where(fecha=fecha).all()
            if registro:
                respuesta = self.esquema(many=True)
                return respuesta.dump(registro), HTTPStatus.OK
            return {
                "mensaje": f"No se encontraron alertas con fecha {fecha}"
            }, HTTPStatus.NOT_FOUND 

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar alertas por fecha",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def actualizar_atendido(self, id):
        try:
            registro = self.model.where(id=id).first()
            if registro:
                registro.update(estado="atendido")
                self.db.session.add(registro)
                self.db.session.commit()
                return {
                    "mensaje": f"La alerta con id {id} se ha actualizado como atendida"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontraron alerta con id {id}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar alertas por fecha",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()