from flask import request
from flask_restplus import Namespace, Resource, fields, marshal_with

from project import settings
from project.core.models.namespace1 import parser, schema_post

api = Namespace(name=settings.NAMESPACE_1,
                description=settings.NAMESPACE_1_DESCRIPTION)

schema_post = api.model('schema', schema_post)


@api.route(settings.ENDPOINT_3_ROUTE)
class String(Resource):
    @api.doc(body=schema_post, description='Retorna tudo em upper case')
    def post(self):
        return {'response': f"{request.json['mensagem_post'].upper()}"}


@api.route(settings.ENDPOINT_4_ROUTE)
class Messaging(Resource):

    @api.doc(body=parser, description='Envia uma mensagem.',)
    def get(self):
        input_data = request.args.get("mensagem")
        return {'response': f'A mensagem enviada foi: {input_data}'}
