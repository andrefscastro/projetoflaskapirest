from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
from .controller import aluno_controller, professor_controller, turma_controller, disciplina_controller, cursos_controller
from .models import aluno_model, professor_model, turma_model, disciplina_model, curso_model