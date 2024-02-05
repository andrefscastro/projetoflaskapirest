from api import ma
from ..models import professor_model
from marshmallow import fields

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_model.Professor
        load_instance = True
        fields = ("id", "nome", "data_nascimento")


    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)