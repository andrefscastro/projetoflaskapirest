from ..models import professor_model
from api import db

def cadastrar_professor(professor):
    professor_db = professor_model.Professor(nome=professor.nome, data_nascimento=professor.data_nascimento)
    db.session.add((professor_db))
    db.session.commit()
    return professor_db


def listar_professores():
    professores = professor_model.Professor.query.all()
    return professores

def listar_professor_id(parm_id):
    professor = professor_model.Professor.query.filter_by(id=parm_id).first()
    return professor

def atualizar_professor(professor_db, professor_atualizado):
    professor_db.nome = professor_atualizado.nome
    professor_db.data_nascimento = professor_atualizado.data_nascimento
    db.session.commit()

def excluir_professor(professor):
    db.session.delete(professor)
    db.session.commit()
