# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from flask.json import dump
from app.api_v1 import api
from app.controllers import ExampleController as Controller


@api.route('/index', methods=['GET'])
def get_index():
    response = Controller.get_index()
    return jsonify(data=response)

#obtenemos todos los registros
@api.route('/example', methods=['GET'])
def get_example():
    response = Controller.get_example()
    return jsonify(response)

# creamos un nuevo registro
@api.route('/example', methods=['POST'])
def post_example():
    response = Controller.post_example(request.json)
    return jsonify(response)

# actualizamos un registro
@api.route('/example/<int:id>', methods=['PATCH'])
def patch_example(id):
    response = Controller.patch_example(id, request.json)
    return jsonify(response)

#eliminamos un registro
@api.route('/example/<int:id>', methods=['DELETE'])
def delete_example(id):
    response = Controller.delete_example(id)
    return jsonify({
        'message': 'Registro eliminado',
        'data': response
    })

