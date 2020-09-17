from flask_restplus.reqparse import RequestParser
from flask_restplus import fields


parser = RequestParser()
parser.add_argument('mensagem', location='args',
                    required=True, help="Não pode ser em branco",
                    default="Teste", nullable=False)

schema_post = {
    'mensagem_post': fields.String(required=True, example="Mensagem de Teste")
}
