from app import api
from flask_restx import Resource
from flask import Response
from http import HTTPStatus


health_ns = api.namespace(
    name='Healthcheck',
    path='/check',
    description='Ruta de verificacion de estado del servicio'
)

@health_ns.route('')
class HealthCheck(Resource):
    def get(self):
        ''' Verificar estado de servicio del servicio web '''
        return Response(status=HTTPStatus.OK)