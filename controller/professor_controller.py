from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from ..service import professor_service
from flask import request, make_response, jsonify
from ..dto import professor_dto

class ProfessorController(Resource):
    def get(self):
        professores = professor_service.listar_professores()
        validate = professor_schema.ProfessorSchema(many=True)
        return make_response(validate.jsonify(professores), 200)

    def post(self):
        professorSchema = professor_schema.ProfessorSchema()
        validate = professorSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novoProfessor = professor_dto.ProfessorDTO(nome=nome, data_nascimento=data_nascimento)
            retorno = professor_service.cadastrar_professor(novoProfessor)
            professorJson = professorSchema.jsonify(retorno)
            return make_response(professorJson, 201)


    def put(self, id):
        professor = professor_service.listar_professor_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado"), 404)

        professorSchema = professor_schema.ProfessorSchema()
        validate = professorSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novoProfessorAlterado = professor_dto.ProfessorDTO(nome, data_nascimento)
            professor_service.atualizar_professor(professor, novoProfessorAlterado)
            professorAtualizado = professor_service.listar_professor_id(id)
            return make_response(professorSchema.jsonify(professorAtualizado), 200)


    def delete(self, id):
        professorDB = professor_service.listar_professor_id(id)
        if professorDB is None:
            return make_response(jsonify("Professor não encontrado"), 404)

        professor_service.excluir_professor(professorDB)
        return make_response(jsonify("Professor excluído com sucesso."), 204)




class ProfessorDetailController(Resource):
    def get(self, id):
        professor = professor_service.listar_professor_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado"), 404)

        validate = professor_schema.ProfessorSchema()
        return make_response(validate.jsonify(professor), 200)





api.add_resource(ProfessorController, "/professor")
api.add_resource(ProfessorController, "/professor/<int:id>", endpoint="alterar_professor", methods=["PUT"])
api.add_resource(ProfessorController, "/professor/<int:id>", endpoint="excluir_professor", methods=["DELETE"])
api.add_resource(ProfessorDetailController, "/professor/<int:id>")