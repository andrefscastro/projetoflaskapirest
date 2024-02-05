from api import db

class Professor(db.Model):
    __tablename__ = "professor"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    data_nascimento = db.Column(db.String, nullable=False)