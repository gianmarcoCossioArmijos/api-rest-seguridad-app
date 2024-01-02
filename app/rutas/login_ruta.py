from app import api
from flask import request
from flask_restx import Resource
from app.esquemas.login_esquema import LoginRequestEsquema
from app.controladores.login_controlador import LoginControlador
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

login_namespace = api.namespace(
    name="Autentificacion",
    path="/auth",
    description="Rutas de autentificacion"
)

esquema_request = LoginRequestEsquema(login_namespace)

@login_namespace.route("/login")
class IniciarSesion(Resource):

    @login_namespace.expect(esquema_request.login(), validate=True)
    def post(self):
        ''' Iniciar sesion '''
        controlador = LoginControlador()
        return controlador.iniciar_sesion(request.json)
    
@login_namespace.route("/refresh")
class NuevoToken(Resource):

    @jwt_required(refresh=True)
    @login_namespace.expect(esquema_request.refresh(), validate=True)
    def post(self):
        ''' Obtener un nuevo access token '''
        identity = get_jwt_identity()
        controlador = LoginControlador()
        return controlador.refresh_token(identity)
    
@login_namespace.route("/restablecer")
class RestablecerClave(Resource):

    @login_namespace.expect(esquema_request.reset(), validate=True)
    def post(self):
        ''' Restablecer contraseña '''
        controlador = LoginControlador()
        return controlador.reseteo_clave(request.json)
    
@login_namespace.route("/actualizar")
class RestablecerClave(Resource):

    @login_namespace.expect(esquema_request.update(), validate=True)
    def post(self):
        ''' Actualizar contraseña '''
        controlador = LoginControlador()
        return controlador.actualizar_clave(request.json)