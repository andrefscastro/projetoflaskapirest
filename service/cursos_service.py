from ..models import curso_model
from api import db
from .disciplina_service import listar_disciplina_id


def cadastrar_curso(curso):
    curso_db = curso_model.CursoModel(nome=curso.nome)
    for i in curso.disciplinas:
        disciplina = listar_disciplina_id(i)
        curso_db.disciplinas.append(disciplina)
    db.session.add(curso_db)
    db.session.commit()
    return curso_db

def listar_cursos():
    cursos = curso_model.CursoModel.query.all()
    return cursos

def listar_curso_id(parm_id):
    curso = curso_model.CursoModel.query.filter_by(id=parm_id).first()
    return curso

def atualizar_curso(curso_db, curso_atualizado):
    curso_db.nome = curso_atualizado.nome
    curso_db.disciplinas = []
    for i in curso_atualizado.disciplinas:
        disciplina = listar_disciplina_id(i)
        curso_db.disciplinas.append(disciplina)

    db.session.commit()

def excluir_curso(curso):
    db.session.delete(curso)
    db.session.commit()





