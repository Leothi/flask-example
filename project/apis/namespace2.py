from flask_restplus import Namespace, Resource

from project import settings


api = Namespace(name=settings.NAMESPACE_2,
                description=settings.NAMESPACE_2_DESCRIPTION)


@api.route(settings.ENDPOINT_1_ROUTE)
class Hello(Resource):
    
    @api.doc(description='Envia uma mensagem de Olá',)
    def get(self):
        return {"Resposta": 'Olá!'}
