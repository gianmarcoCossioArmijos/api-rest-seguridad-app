from app import db
from app.modelos.unidades_modelo  import ModeloUnidad
from app.esquemas.unidades_esquema import UnidadResponseEsquema
from http import HTTPStatus


class UnidadControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloUnidad
        self.esquema = UnidadResponseEsquema

    def listar_unidades(self, fecha):
        try:
            registros = self.model.where(estado=True, fecha=fecha).all()
            respuesta = self.esquema(many=True)
            return respuesta.dump(registros), HTTPStatus.OK

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar unidades",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def registrar(self, datos):
        try:
            nuevo_registro = self.model.create(**datos)
            self.db.session.add(nuevo_registro)
            self.db.session.commit()
            return {
                "mensaje": f"La unidad {datos['codigo']} se ha registrado exitosamente"
            }, HTTPStatus.CREATED

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar unidad",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def encontrar_por_codigo(self, codigo):
        try:
            registro = self.model.where(codigo=codigo).first()
            if registro:
                respuesta = self.esquema(many=False)
                return respuesta.dump(registro), HTTPStatus.OK
            return {
                "mensaje": f"No se encontro la unidad con codigo {codigo}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar unidad",
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
                    "mensaje": f"La unidad con id {id} se ha actualizado"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontro la unidad con id {id}"
            }, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar unidad",
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
                    "mensaje": f"La unidad con id {id} se ha desabilitado"
                }, HTTPStatus.NO_CONTENT
            return {
                "mensaje": f"No se econtro la unidad con id {id}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar unidad",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()