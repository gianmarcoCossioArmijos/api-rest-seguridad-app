from app import db
from app.modelos.unidades_modelo  import ModeloUnidad
from http import HTTPStatus


class UnidadControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloUnidad

    def listar_unidades(self, fecha):
        try:
            registros = self.model.where(estado=True, fecha=fecha).all()
            respuesta = []
            for registro in registros:
                respuesta.append(registro.toJson())
            return respuesta, HTTPStatus.OK

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
                return registro.toJson(), HTTPStatus.OK
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