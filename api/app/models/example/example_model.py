# -*- coding: utf-8 -*-
#########################################################
# All rights by Softpymes
# Models Example
#########################################################

from app import db
from app.models import BaseModel
from app.exception import InternalServerError
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import validates
from sqlalchemy.sql import or_
from app.utils import FieldValidations


class ExampleModel(BaseModel):
    __tablename__ = 'example'

    name = db.Column(db.String(50), unique=True, nullable=False, comment='Nombre de Ejemplo')
    identification = db.Column(db.String(100), nullable=False, unique=True, comment='Identificación de Ejemplo')
    description = db.Column(db.String(100), nullable=True, comment='Descripción de Ejemplo')
    status = db.Column(TINYINT(1), default=0, nullable=False, comment='Estado 0=Inactivo, 1=Activo')

    def export_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'identification': self.identification,
            'status': bool(self.status)
        }
    @validates(('name', 'identification'))
    def validate_name_permit(self, key, name):
        try:
            FieldValidations.is_none(key, name)
            FieldValidations.is_empty(key, name)
            return name
        except Exception as e:
            print(e)
            raise InternalServerError(e)

    @validates('status')
    def validate_status(self, key, status):
        try:
            FieldValidations.is_none(key, status)
            FieldValidations.is_empty(key, status)
            return status
        except Exception as e:
            print(e)
            raise InternalServerError(e)

