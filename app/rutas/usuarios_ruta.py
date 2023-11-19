from app import api
from app.esquemas.usuarios_esquema import UsuarioRequestEsquema
from flask_restx import Resource
from app.controladores.usuarios_controlador import UsurioControlador
from flask import request
from flask_jwt_extended import jwt_required


usuario_namespace = api.namespace(
    name="Usuarios",
    path="/usuarios",
    description="Rutas de usuarios"
)

esquema_request = UsuarioRequestEsquema(usuario_namespace)

@usuario_namespace.route("")
@usuario_namespace.doc(security="Bearer")
class Usuario(Resource):
    
    @jwt_required()
    def get(self):
        ''' Listar todos los usuarios '''
        controlador = UsurioControlador()
        return controlador.listar_todos()
    
    @usuario_namespace.expect(esquema_request.create(), validate=True)
    def post(self):
        ''' Registrar nuevo usuario'''
        controlador = UsurioControlador()
        return controlador.registrar(request.json)

@usuario_namespace.route("/<int:id>")
@usuario_namespace.doc(security="Bearer")
class UsuariosPorId(Resource):
    
    @jwt_required()
    def get(self, id):
        ''' Listar usuario por id '''
        controlador = UsurioControlador()
        return controlador.encontrar_por_id(id)
    
    @jwt_required()
    @usuario_namespace.expect(esquema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar usuario por id '''
        controlador = UsurioControlador()
        return controlador.actualizar(id, request.json)
    
    @jwt_required()
    def delete(self, id):
        ''' Eliminar usuario por id '''
        controlador = UsurioControlador()
        return controlador.eliminar(id)