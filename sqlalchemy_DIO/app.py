from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa (Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                "nome":pessoa.nome,
                "idade":pessoa.idade,
                "ID":pessoa.id
            }
        except AttributeError:
            response = {
                "status": "erro",
                "mensagem ":f"Nome {nome} nao encontrado"
            }
        return response
    
    
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if "nome" in dados:
            pessoa.nome = dados["nome"]
        if "idade" in dados:
            pessoa.idade = dados["idade"]
        pessoa.save()
        response = {
            "Resposta":" Dados alterados",
            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        }
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {
            "status":"sucesso", 
            "mensagem": f"cadastro de {nome} excluido com sucesso"
            }


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id": i.id, "nome": i.nome, "idade" :i.idade} for i in pessoas]
        return  response
    
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados["nome"], idade = dados["idade"])
        pessoa.save()
        response = {
            "Mensagem: ": "Usuario adicionado!",
            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        }
        return response



class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{"atividade": i.atividade, "pessoa_id": i.pessoa_id, } for i in atividades]
        return  response
    
    def post(self):
        dados = request.json
        atividade = Atividades(atividade=dados["atividade"], pessoa_id = dados["pessoa_id"])
        atividade.save()
        response = {
            "Mensagem: ": "Atividade adicionada!",
            "Atividade": atividade.atividade,
            "pessoa_id": atividade.pessoa_id,
        }
        return response



api.add_resource(Pessoa, "/pessoa/<string:nome>/")
api.add_resource(ListaPessoas, "/pessoa/")
api.add_resource(ListaAtividades, "/atividade/")

if __name__ == "__main__":
    app.run(debug=True)
