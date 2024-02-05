from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from ..service import  cursos_service
from ..dto import curso_dto
from flask import request, make_response, jsonify

class CursoController(Resource):
    def get(self):
        cursos = cursos_service.listar_cursos()
        validate = curso_schema.CursoSchema(many=True)
        return make_response(validate.jsonify(cursos), 200)


    def post(self):
        cursoSchema = curso_schema.CursoSchema()
        validate = cursoSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            disciplinas = request.json["disciplinas"]
            novoCurso = curso_dto.CursoDTO(nome=nome, disciplinas=disciplinas)
            retorno = cursos_service.cadastrar_curso(novoCurso)
            cursoJson = cursoSchema.jsonify(retorno)
            return make_response(cursoJson, 200)


    def put(self, id):
        curso = cursos_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("Curso não localizado"), 404)

        cursoSchema = curso_schema.CursoSchema()
        validate = cursoSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            disciplinas = request.json["disciplinas"]
            novoCursoAlterado = curso_dto.CursoDTO(nome=nome,disciplinas=disciplinas)
            cursos_service.atualizar_curso(curso, novoCursoAlterado)
            cursoAtualizado = cursos_service.listar_curso_id(id)
            return make_response(cursoSchema.jsonify(cursoAtualizado), 200)

    def delete(self, id):
        cursoDB = cursos_service.listar_curso_id(id)
        if cursoDB is None:
            return make_response(jsonify("Curso nao encontrado"), 404)

        cursos_service.excluir_curso(cursoDB)
        return make_response(jsonify("Curso excluído com sucesso"), 204)


class CursoDetailController(Resource):
    def get(self, id):
        curso = cursos_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("Curso não encontrado"), 404)

        validate = curso_schema.CursoSchema()
        return make_response(validate.jsonify(curso), 200)



api.add_resource(CursoController, "/curso")
api.add_resource(CursoDetailController, "/curso/<int:id>")
api.add_resource(CursoController, "/curso/<int:id>", endpoint="alterar_curso", methods=["PUT"])
api.add_resource(CursoController, "/curso/<int:id>", endpoint="excluir_curso", methods=["DELETE"])
