from app import db
from app.modelos.noticias_modelo import ModeloNoticia
from app.esquemas.noticias_esquema import NoticiaResponseEsquema
from http import HTTPStatus


class NoticiaControlador:

    def __init__(self):
        self.db = db
        self.model = ModeloNoticia
        self.esquema = NoticiaResponseEsquema

    def listar_noticias(self):
        try:
            registros = self.model.all()
            respuesta = self.esquema(many=True)
            return respuesta.dump(registros), HTTPStatus.OK
        
        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al listar noticias",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def registrar(self, datos):
        try:
            nuevo_registro = self.model.create(**datos)
            self.db.session.add(nuevo_registro)
            self.db.session.commit()
            return {
                "mensaje": f"La noticia {datos['titulo']} se registro exitosamente"
            }, HTTPStatus.CREATED

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al registrar noticia",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()

    def actualizar(self, id, datos):
        try:
            registro = self.model.where(id=id).first()
            if registro:
                registro.update(**datos)
                self.db.session.add(registro)
                self.db.session.commit()
                return {
                    "mensaje": f"Se actulizo noticia con id {id}"
                }, HTTPStatus.OK
            return {
                "mensaje": f"No se encontro la noticia con id {id}"
            }, HTTPStatus.NOT_FOUND

        except Exception as e:
            return {
                "mensaje": "Ocurrio un error al actualizar noticia",
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        finally:
            self.db.session.close()
        