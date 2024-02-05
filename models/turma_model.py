from api import db

class TurmaModel(db.Model):
    __tablename__ = "turma"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    curso_id = db.Column(db.Integer,db.ForeignKey("curso.id"), nullable=False)
