from ..models import turma_model
from api import db

def cadastrar_turma(turma):
    turma_db = turma_model.TurmaModel(nome=turma.nome, descricao=turma.descricao, data_inicio=turma.data_inicio,
                                      data_fim=turma.data_fim, curso_id=turma.curso_id)
    db.session.add((turma_db))
    db.session.commit()
    return turma_db


def listar_turma():
    turmas = turma_model.TurmaModel.query.all()
    return turmas

def listar_turma_id(parm_id):
    turma = turma_model.TurmaModel.query.filter_by(id=parm_id).first()
    return turma

def atualizar_turma(turma_db, turma_atualizada):
    turma_db.nome = turma_atualizada.nome
    turma_db.descricao = turma_atualizada.descricao
    turma_db.data_inicio = turma_atualizada.data_inicio
    turma_db.data_fim = turma_atualizada.data_fim
    turma_db.curso_id = turma_atualizada.curso_id
    db.session.commit()

def excluir_turma(turma):
    db.session.delete(turma)
    db.session.commit()
