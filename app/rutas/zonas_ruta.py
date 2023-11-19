from flask_restx import Resource
from app import api
from app.esquemas.zonas_esquema import ZonaRequestEsquema
from app.controladores.zonas_controlador import ZonaControlador
from flask import request
from flask_jwt_extended import jwt_required


zona_namespace = api.namespace(
    name="Zonas",
    path="/zonas",
    description="Rutas de zonas"
)

esquema_request = ZonaRequestEsquema(zona_namespace)

@zona_namespace.route("")
@zona_namespace.doc(security="Bearer")
class Zonas(Resource):
    
    @jwt_required()
    def get(self):
        ''' Listar todas las zonas '''
        controlador = ZonaControlador()
        return controlador.listar_todos()
    
    @jwt_required()
    @zona_namespace.expect(esquema_request.create(), validate=True)
    def post(self):
        ''' Registrar nueva zona '''
        controlador = ZonaControlador()
        return controlador.registrar(request.json)

@zona_namespace.route("/<int:id>")
@zona_namespace.doc(security="Bearer")
class ZonasPorId(Resource):
    
    @jwt_required()
    def get(self, id):
        ''' Listar zona por id '''
        controlador = ZonaControlador()
        return controlador.encontrar_por_id(id)
    
    @jwt_required()
    @zona_namespace.expect(esquema_request.update(), validate=True)
    def patch(self, id):
        ''' Actulizar zona por id '''
        controlador = ZonaControlador()
        return controlador.actualizar(id, request.json)
    
    @jwt_required()
    def delete(self, id):
        ''' Eliminar zona por id '''
        controlador = ZonaControlador()
        return controlador.eliminar(id)