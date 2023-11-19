from flask_restx import Resource
from app import api
from app.esquemas.vehiculos_esquema import VehiculoRequestEsquema
from app.controladores.vehiculos_controlador import VehiculoControlador
from flask import request
from flask_jwt_extended import jwt_required


vehiculo_namespace = api.namespace(
    name="Vehiculos",
    path="/vehiculos",
    description="Rutas de vehiculos"
)

equema_request = VehiculoRequestEsquema(vehiculo_namespace)

@vehiculo_namespace.route("")
@vehiculo_namespace.doc(security="Bearer")
class Vehiculos(Resource):

    @jwt_required()
    def get(self):
        ''' Listar todos los vehiculos '''
        controlador = VehiculoControlador()
        return controlador.listar_todos()
    
    @jwt_required()
    @vehiculo_namespace.expect(equema_request.create(), validate=True)
    def post(self):
        ''' Registrar nuevo vehiculo '''
        controlador = VehiculoControlador()
        return controlador.registrar(request.json)

@vehiculo_namespace.route("/<int:id>")
@vehiculo_namespace.doc(security="Bearer")
class VehiculosPorId(Resource):

    @jwt_required()
    def get(self, id):
        ''' Listar vehiculo por id '''
        controlador = VehiculoControlador()
        return controlador.encontrar_por_id(id)
    
    @jwt_required()
    @vehiculo_namespace.expect(equema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar vehiculo por id '''
        controlador = VehiculoControlador()
        return controlador.actualizar(id, request.json)
    
    @jwt_required()
    def delete(self, id):
        ''' Eliminar vehiculo por id '''
        controlador = VehiculoControlador()
        return controlador.eliminar(id)
