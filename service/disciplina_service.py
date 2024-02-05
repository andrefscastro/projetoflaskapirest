from ..models import disciplina_model
from api import db

def cadastrar_disciplina(disciplina):
    disciplina_db = disciplina_model.DisciplinaModel(nome=disciplina.nome)
    db.session.add(disciplina_db)
    db.session.commit()
    return disciplina_db


def listar_disciplinas():
    disciplinas = disciplina_model.DisciplinaModel.query.all()
    return disciplinas

def listar_disciplina_id(parm_id):
    disciplina = disciplina_model.DisciplinaModel.query.filter_by(id=parm_id).first()
    return disciplina

def atualizar_disciplina(disciplina_db, disciplina_atualizada):
    disciplina_db.nome = disciplina_atualizada.nome
    db.session.commit()

def excluir_disciplina(disciplina):
    db.session.delete(disciplina)
    db.session.commit()