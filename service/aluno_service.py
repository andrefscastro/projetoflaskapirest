from ..models import aluno_model
from api import db

def cadastrar_aluno(aluno):
    aluno_db = aluno_model.Aluno(nome=aluno.nome, data_nascimento=aluno.data_nascimento)
    db.session.add(aluno_db)
    db.session.commit()
    return aluno_db

def listar_alunos():
    alunos = aluno_model.Aluno.query.all()
    return alunos

def listar_alunos_id(parm_id):
    aluno = aluno_model.Aluno.query.filter_by(id=parm_id).first()
    return aluno

def atualizar_aluno(aluno_db, aluno_atualizado):
    aluno_db.nome = aluno_atualizado.nome
    aluno_db.data_nascimento = aluno_atualizado.data_nascimento
    db.session.commit()

def excluir_aluno(aluno):
    db.session.delete(aluno)
    db.session.commit()

