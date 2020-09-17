from flask import Flask
from loguru import logger

from project.apis import api

# Logger da aplicação
logger.add('api_teste.log', rotation="100 MB")

# Instância app Flask
app = Flask(__name__)

# Forma lazy: api é instanceada em apis com argumentos e aqui só inicializada
api.init_app(app)
