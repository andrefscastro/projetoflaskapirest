from api import db


class CursoModel(db.Model):
    __tablename__ = "curso"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    disciplinas = db.relationship("DisciplinaModel", secondary="curso_disciplina", back_populates="cursos")
