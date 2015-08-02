from __future__ import print_function

import logging
import logging.config

from jsonrpc_helpers.validation import validated
from jsonrpc_helpers.log import build_instance_method_decorator


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
logged = build_instance_method_decorator(logger=logger)


SCHEMA = {
    'type': 'object',
    'properties': {
        'baz': {'type': 'integer'},
        'qux': {'type': 'string'},
    }
}


class Foo(object):
    @logged()
    @validated(SCHEMA)
    def bar(self, baz, qux=''):
        return baz * baz


foo = Foo()
result = foo.bar(10)
print(result)
