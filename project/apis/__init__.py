from flask_restplus import Api, Resource

from project import settings
from project.apis.namespace1 import api as ns_1
from project.apis.namespace2 import api as ns_2

# Instância da API de extensão do Flask Restplus
api = Api(doc=settings.SWAGGER_DOC, title=settings.SWAGGER_TITLE,
          description=settings.SWAGGER_DESCRIPTION, version=settings.SWAGGER_VERSION,
          validate=settings.FLASK_RESTPLUS_VALIDATE)


# Namespaces
api.add_namespace(ns_1)
api.add_namespace(ns_2)
