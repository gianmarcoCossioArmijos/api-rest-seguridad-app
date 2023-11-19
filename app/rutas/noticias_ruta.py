from app import api
from flask_restx import Resource
from app.esquemas.noticias_esquema import NoticiaRequestEsquema
from app.controladores.noticias_controlador import NoticiaControlador
from flask import request
from flask_jwt_extended import jwt_required


noticia_namespace = api.namespace(
    name="Noticias",
    path="/noticias",
    description="Rutas de noticias"
)

esquema_request = NoticiaRequestEsquema(noticia_namespace)

@noticia_namespace.route("")
@noticia_namespace.doc(security="Bearer")
class Noticia(Resource):

    @jwt_required()
    def get(self):
        ''' Listar todas las noticias '''
        controlador = NoticiaControlador()
        return controlador.listar_noticias()
    
    @jwt_required()
    @noticia_namespace.expect(esquema_request.create(), validate=True)
    def post(self):
        ''' Registrar nueva noticia '''
        controlador = NoticiaControlador()
        return controlador.registrar(request.json)
    
@noticia_namespace.route("/<int:id>")
@noticia_namespace.doc(security="Bearer")
class NoticiaPorId(Resource):

    @jwt_required()
    @noticia_namespace.expect(esquema_request.update(), validate=True)
    def patch(self, id):
        ''' Actulizar noticia por id '''
        controlador = NoticiaControlador()
        return controlador.actualizar(id, request.json)