from app import api
from app.esquemas.roles_esquema import RolRequestEsquema
from flask_restx import Resource
from app.controladores.roles_controlador import RolControlador
from flask import request
from flask_jwt_extended import jwt_required


rol_namespace = api.namespace(
    name="Roles",
    path="/roles",
    description="Rutas de roles"
)

esquema_request = RolRequestEsquema(rol_namespace)

@rol_namespace.route("")
@rol_namespace.doc(security="Bearer")
class Roles(Resource):

    @jwt_required()
    def get(self):
        ''' Listar todos los roles '''
        controlador = RolControlador()
        return controlador.listar_todos()
    
    
    @rol_namespace.expect(esquema_request.create(), validate=True)
    def post(self):
        ''' Registrar nuevo rol '''
        controlador = RolControlador()
        return controlador.registrar(request.json)
    
@rol_namespace.route("/<int:id>")
@rol_namespace.doc(security="Bearer")
class RolesPorId(Resource):

    @jwt_required()
    def get(self, id):
        ''' Listar rol por ir '''
        controlador = RolControlador()
        return controlador.encontrar_por_id(id)
    
    @jwt_required()
    @rol_namespace.expect(esquema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar rol por id '''
        controlador = RolControlador()
        return controlador.actualizar(id, request.json)
    
    @jwt_required()
    def delete(self, id):
        ''' Eliminar rol por id '''
        controlador = RolControlador()
        return controlador.eliminar(id)