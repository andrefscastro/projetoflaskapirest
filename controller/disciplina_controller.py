from flask_restful import Resource
from api import api
from ..schemas import disciplina_schema
from ..dto import disciplina_dto
from ..service import disciplina_service
from flask import request, make_response, jsonify


class DisciplinaController(Resource):
    def get(self):
        disciplinas = disciplina_service.listar_disciplinas()
        validate = disciplina_schema.DisciplinaSchema(many=True)
        return make_response(validate.jsonify(disciplinas), 200)

    def post(self):
        disciplinaSchema = disciplina_schema.DisciplinaSchema()
        validate = disciplinaSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            novaDisciplina = disciplina_dto.DisciplinaDTO(nome=nome)
            retorno = disciplina_service.cadastrar_disciplina(novaDisciplina)
            disciplinaJson = disciplinaSchema.jsonify(retorno)
            return make_response(disciplinaJson, 201)

    def put(self, id):
        disciplina = disciplina_service.listar_disciplina_id(id)
        if disciplina is None:
            return make_response(jsonify("Disciplina não encontrada"), 404)

        disciplinaSchema = disciplina_schema.DisciplinaSchema()
        validate = disciplinaSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            novaDisciplinaAlterada = disciplina_dto.DisciplinaDTO(nome)
            disciplina_service.atualizar_disciplina(disciplina, novaDisciplinaAlterada)
            disciplinaAtualizada = disciplina_service.listar_disciplina_id(id)
            return make_response(disciplinaSchema.jsonify(disciplinaAtualizada), 200)

    def delete(self, id):
        disciplinaDB = disciplina_service.listar_disciplina_id(id)
        if disciplinaDB is None:
            return make_response(jsonify("Disciplina não encontrada"), 404)

        disciplina_service.excluir_disciplina(disciplinaDB)
        return make_response(jsonify("Disciplina excluída com sucesso."), 204)


class DisciplonaDetailController(Resource):
    def get(self, id):
        disciplina = disciplina_service.listar_disciplina_id(id)
        if disciplina is None:
            return make_response(jsonify("Disciplina não encontrada"), 404)

        validate = disciplina_schema.DisciplinaSchema()
        if validate:
            return make_response(validate.jsonify(disciplina), 200)


api.add_resource(DisciplinaController, "/disciplina")
api.add_resource(DisciplonaDetailController, "/disciplina/<int:id>")
api.add_resource(DisciplinaController, "/disciplina/<int:id>", endpoint="alterar_disciplina", methods=["PUT"])
api.add_resource(DisciplinaController, "/disciplina/<int:id>", endpoint="excluir_disciplina", methods=["DELETE"])
