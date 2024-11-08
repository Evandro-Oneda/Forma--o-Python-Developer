from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades, ListaHabilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        "id": "0",
        "nome": "evandro",
        "habilidades": ["Python"]
    },
     
    {
        "id": "1",
        "nome": "joao",
        "habilidades": ["java"]
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "desenvolvedor de ID {} não existe". format(id)
            response = {"status" : "erro", "mensagem" : mensagem}
        except Exception:
            mensagem = "Erro desonhecido. Procure o administrador da API"
            response = {"status" : "erro", "mensagem" : mensagem}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status" : "sucesso", "mensagem" : "registro excluido"}
    

class ListaDesenvolvedores(Resource):
    def get (self):
        return desenvolvedores
    def post (self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    
api.add_resource(Desenvolvedor, "/dev/<int:id>/" )
api.add_resource(ListaDesenvolvedores, "/dev/")
api.add_resource(Habilidades, "/dev/habilidades/<int:id>")
api.add_resource(ListaHabilidades,"/dev/habilidades/")

if __name__ =="__main__":
    app.run(debug=True)