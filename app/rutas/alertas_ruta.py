from app import api
from flask_restx import Resource
from app.esquemas.alertas_esquema import AlertaResquestEsquema
from app.controladores.alertas_controlador import AlertaControlador
from flask import request
from flask_jwt_extended import jwt_required


alerta_namespace = api.namespace(
    name="Alertas",
    path="/alertas",
    description="Rutas de alertas"
)

esquema_request = AlertaResquestEsquema(alerta_namespace)

@alerta_namespace.route("")
@alerta_namespace.doc(security="Bearer")
class Alerta(Resource):
    
    @jwt_required()
    def get(self):
        ''' Listar todas las alertas pendientes'''
        controlador = AlertaControlador()
        return controlador.listar_pendientes()
    
    @alerta_namespace.expect(esquema_request.create(), validate=True)
    def post(self):
        ''' Registar nueva alerta '''
        controlador = AlertaControlador()
        return controlador.registrar(request.json)

@alerta_namespace.route("/<int:id>") 
@alerta_namespace.doc(security="Bearer")
class AlertaPorId(Resource):

    @jwt_required()
    def get(self, id):
        ''' Listar alerta por id '''
        controlador = AlertaControlador()
        return controlador.encontrar_por_id(id)
    
    @jwt_required()
    def patch(self, id):
        ''' Actualizar alerta como atendida '''
        controlador = AlertaControlador()
        return controlador.actualizar_atendido(id)

@alerta_namespace.route("/<string:fecha>")
@alerta_namespace.doc(security="Bearer")
class AlertaPorFecha(Resource):

    @jwt_required()
    def get(self, fecha):
        ''' Listar alertas por fecha '''
        controlador = AlertaControlador()
        return controlador.encontrar_por_fecha(fecha)