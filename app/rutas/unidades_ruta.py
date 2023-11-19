from app import api
from app.esquemas.unidades_esquema import UnidadRequestEsquema
from flask_restx import Resource
from app.controladores.unidades_controlador import UnidadControlador
from flask import request
from flask_jwt_extended import jwt_required


unidad_namespace = api.namespace(
    name="Unidades",
    path="/unidades",
    description="Rutas de unidades"
)

esquema_request = UnidadRequestEsquema(unidad_namespace)

@unidad_namespace.route("")
@unidad_namespace.doc(security="Bearer")
class Unidad(Resource):

    @jwt_required()
    @unidad_namespace.expect(esquema_request.create(), validate=True)
    def post(self):
        ''' Registrar nueva unidad '''
        controlador = UnidadControlador()
        return controlador.registrar(request.json)

@unidad_namespace.route("/<string:fecha>")
@unidad_namespace.doc(security="Bearer")
class UnidadPorFecha(Resource):

    @jwt_required()
    def get(self, fecha):
        ''' Listar todas las unidades por fecha'''
        controlador = UnidadControlador()
        return controlador.listar_unidades(fecha)
    
@unidad_namespace.route("/codigo/<string:codigo>")
@unidad_namespace.doc(security="Bearer")
class UnidadPorCodigo(Resource):

    @jwt_required()
    def get(self, codigo):
        ''' Listar unidad por codigo '''
        controlador = UnidadControlador()
        return controlador.encontrar_por_codigo(codigo)
    
@unidad_namespace.route("/<int:id>")
@unidad_namespace.doc(security="Bearer")
class UnidadPorId(Resource):

    @jwt_required()
    @unidad_namespace.expect(esquema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar unidad por id '''
        controlador = UnidadControlador()
        return controlador.actualizar(id, request.json)
    
    @jwt_required()
    def delete(self, id):
        ''' Desabilitar unidad por id '''
        controlador = UnidadControlador()
        return controlador.eliminar(id)