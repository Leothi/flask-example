import os

__version__ = '1.1'

# flask settings
FLASK_ENVIRONMENT = os.environ.get('FLASK_ENVIRONMENT', 'development')
FLASK_SERVER_NAME = os.environ.get('FLASK_SERVER_NAME', None)
FLASK_HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
FLASK_PORT = os.environ.get('FLASK_PORT', '8080')
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', True)
FLASK_RESTPLUS_VALIDATE = os.environ.get('FLASK_RESTPLUS_VALIDATE', True)
FLASK_RESTPLUS_MASK_SWAGGER = os.environ.get(
    'FLASK_RESTPLUS_MASK_SWAGGER', False)

# swagger
SWAGGER_DOC = '/docs'
SWAGGER_TITLE = 'Api Teste'
SWAGGER_DESCRIPTION = 'Treinamento de Flask'
SWAGGER_VERSION = __version__

# Namespaces e rotas
# NAMESPACE 1
NAMESPACE_1 = os.environ.get('NAMESPACE_1', 'namespace1')
NAMESPACE_1_DESCRIPTION = os.environ.get('NAMESPACE_1_DESCRIPTION',
                                         'Primeiro namespace.')

ENDPOINT_1_ROUTE = os.environ.get(
    'ENDPOINT_1_ROUTE', '/hello')
ENDPOINT_2_ROUTE = os.environ.get(
    'ENDPOINT_2_ROUTE', '/bye')
ENDPOINT_3_ROUTE = os.environ.get(
    'ENDPOINT_3_ROUTE', '/string/string_upper')
ENDPOINT_4_ROUTE = os.environ.get(
    'ENDPOINT_4_ROUTE', '/messaging/message')

# NAMESPACE 2
NAMESPACE_2 = os.environ.get('NAMESPACE_2', 'namespace2')
NAMESPACE_2_DESCRIPTION = os.environ.get('NAMESPACE_2_DESCRIPTION',
                                         'Segundo namespace')

# gunicorn settings
bind = os.environ.get('GUNICORN_BIND', f'{FLASK_HOST}:{FLASK_PORT}')
workers = os.environ.get('GUNICORN_WORKERS', 1)
threads = os.environ.get('GUNICORN_THREADS', 1)
reload = os.environ.get('GUNICORN_RELOAD', True)
timeout = os.environ.get('GUNICORN_TIMEOUT', 30)
graceful_timeout = os.environ.get('GUNICORN_GRACEFUL_TIMEOUT', 30)
loglevel = os.environ.get('GUNICORN_LOGLEVEL', 'info')
