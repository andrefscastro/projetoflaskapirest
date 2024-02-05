from api import ma
from ..models import turma_model
from marshmallow import fields

class TurmaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = turma_model.TurmaModel
        load_instance = True
        fields = ("id", "nome", "descricao", "data_inicio", "data_fim", "curso_id")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_inicio = fields.Date(required=True)
    data_fim = fields.Date(required=True)
    curso_id = fields.String(required=True)