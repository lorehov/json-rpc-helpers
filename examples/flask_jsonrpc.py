"""
Additional requirements for this example:
  - Flask>=0.10.1
  - json-rpc>=1.10.1
"""
import logging
import logging.config

from flask import Flask, g
from jsonrpc.backend.flask import api
from jsonrpc_helpers.log import build_flask_decorator
from jsonrpc_helpers.validation import validated

app = Flask(__name__)
app.register_blueprint(api.as_blueprint())


logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s|%(module)s|%(message)s|%(method)s|'}},
    'handlers': {
        'stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'}},
    'loggers': {
        'default': {
            'handlers': ['stdout'],
            'level': 'DEBUG'}}})

logger = logging.getLogger('default')
logged = build_flask_decorator(logger=logger)


SCHEMA = {
    'type': 'object',
    'properties': {
        'phone': {'type': 'number'},
        'name': {'type': 'string'},
    }
}


@api.dispatcher.add_method
@logged(args_to_skip=['photo'])
@validated(schema=SCHEMA, args_to_skip=['photo'])
def register(name, phone, photo=None):
    g.get('logger').info('someone registered.')
    return {name: phone}

app.run(host='127.0.0.1', port=3000, debug=True)
