from api import db
from .curso_model import CursoModel


curso_disciplina = db.Table("curso_disciplina",
                            db.Column("curso_id", db.Integer, db.ForeignKey("curso.id"), primary_key=True, nullable=False),
                            db.Column("disciplina_id", db.Integer, db.ForeignKey("disciplina.id"), primary_key=True, nullable=False))
class DisciplinaModel(db.Model):
    __tablename__ = "disciplina"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    cursos = db.relationship(CursoModel, secondary="curso_disciplina", back_populates="disciplinas")