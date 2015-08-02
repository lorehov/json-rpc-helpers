json-rpc-helpers
================

.. image:: https://travis-ci.org/lorehov/json-rpc-helpers.png
     :target: https://travis-ci.org/lorehov/json-rpc-helpers
     :alt: Build Status


Overview
--------

**json-rpc-helpers** library is a set of helpers that can be used with
almost any jsonrpc library in Python. More then, this lib can be used
even without jsonrpc library.

Currently it solves following problems:

    * logging;
    * validation.


Logging
-------

Usually when bootstrapping `jsonrpc` API following problems are raise:

    * log call with method name, params and some context
    (request id, user identity, etc);
    * provide context for logger in handlers;
    * log call result and execution time;
    * log errors.

Usage:

    import logging

    from jsonrpc_helpers.log import build_instance_method_decorator



    logger = logging.getLogger()
    logged = build_instance_method_decorator(logger=logger)

    class Handler(object):

        @logged()
        def handle(self, foo=None, bar="bar"):
            self.logger.info("Method called")
            return "something"


Validation
----------

This is not usual problem :) But it still can be useful to validate call
arguments BEFORE these pass to handler. More then - to validate these against
some declarative scheme that can be shared with API consumers.

Usage:

    from jsonrpc_helpers.validation import validated


    SCHEMA = {
        'type': 'object',
        'properties': {
            'baz': {'type': 'integer'},
            'qux': {'type': 'string'},
        },
        'required': ['baz']
    }

    validated(SCHEMA)
    def handler(baz, quz):
        return baz * baz


Install
-------

    pip install json-rpc-helpers

Tests
-----

    tox


