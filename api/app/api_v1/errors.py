# -*- coding: utf-8 -*-
#########################################################
from flask import jsonify

from app.api_v1 import api
from app.exception import (InternalServerError, BadRequest, NotFound, MethodNotAllowed)


@api.errorhandler(InternalServerError)
def internal_server_error(e):
    response = jsonify(
        {
            'status': 500,
            'error': 'internal server error',
            'message': str(e.args[0])
        }
    )
    response.status_code = 500
    return response


@api.errorhandler(BadRequest)
def bad_request(e):
    response = jsonify(
        {
            'status': 400,
            'error': 'bad request',
            'message': str(e.args[0])
        }
    )
    response.status_code = 400
    return response


@api.errorhandler(NotFound)
def not_found(e):
    response = jsonify(
        {
            'status': 404,
            'error': 'not found',
            'message': str(e.args[0])
        }
    )
    response.status_code = 404
    return response


@api.errorhandler(MethodNotAllowed)
def method_not_allowed(e):
    response = jsonify(
        {
            'status': 405,
            'error': 'method not found',
            'message': str(e.args[0])
        }
    )
    response.status_code = 405
    return response
