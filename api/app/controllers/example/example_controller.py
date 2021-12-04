# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from flask.json import dump, dumps
from app.exception import InternalServerError
from app.models import ExampleModel
from marshmallow import Schema, fields, schema
from app import db


class ExampleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    identification = fields.Str(required=True)
    status = fields.Boolean(required=True)


class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def get_example():
        try:
            get_example = ExampleModel.query.all()
            schema = ExampleSchema()
            return schema.dump(get_example, many=True)
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod

    def post_example(data):
        try:
            example = ExampleModel(
                name=data['name'],
                identification=data['identification'],
                description=data['description'],
                status=data['status']
            )
            db.session.add(example)
            db.session.commit()
            schema = ExampleSchema()
            return schema.dump(example)
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def patch_example(id,data):
        try:
            example = ExampleModel.query.filter_by(id=id).first()
            example.name = data['name']
            example.identification = data['identification']
            example.description = data['description']
            db.session.commit()
            schema = ExampleSchema()
            return schema.dump(example)
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def delete_example(id):
        try:
            example = ExampleModel.query.filter_by(id=id).first()
            db.session.delete(example)
            db.session.commit()
            schema = ExampleSchema()
            return schema.dump(example)
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)