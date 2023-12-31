from app import api
from flask_restx import Resource
from app.esquemas.denuncias_esquema import DenunciaRequestEsquema
from app.controladores.denuncias_controlador import DenunciaControlador
from flask import request
from flask_jwt_extended import jwt_required


denuncia_namespace = api.namespace(
    name="Denuncias",
    path="/denuncias",
    description="Rutas de denuncias"
)

esquema_request = DenunciaRequestEsquema(denuncia_namespace)

@denuncia_namespace.route("")
@denuncia_namespace.doc(security="Bearer")
class Denuncia(Resource):

    @jwt_required()
    def get(self):
        ''' Listar denuncias '''
        controlador = DenunciaControlador()
        return controlador.listar_denuncias()

    @jwt_required()
    @denuncia_namespace.expect(esquema_request.create(), validate=True)
    def post(self):
        ''' Registrar nueva denuncia '''
        controlador = DenunciaControlador()
        return controlador.registrar(request.json)

@denuncia_namespace.route("/<string:fecha>")
@denuncia_namespace.doc(security="Bearer")
class DenunciaPorFecha(Resource):

    @jwt_required()
    def get(self, fecha):
        ''' Listar denuncias por fecha '''
        controlador = DenunciaControlador()
        return controlador.listar_denuncias_fecha(fecha)
    
@denuncia_namespace.route("/<int:id_usuario>")
@denuncia_namespace.doc(security="Bearer")
class DenunciaPorUsuario(Resource):

    @jwt_required()
    def get(self, id_usuario):
        ''' Listar denuncias por usuario '''
        controlador = DenunciaControlador()
        return controlador.listar_denuncias_usuario(id_usuario)

@denuncia_namespace.route("/<int:id>")
@denuncia_namespace.doc(security="Bearer")
class DenunciaPorId(Resource):

    @jwt_required()
    def patch(self, id):
        ''' Actualizar denuncia como atendida'''
        controlador = DenunciaControlador()
        return controlador.actualizar_atendido(id)