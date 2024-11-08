from flask_restful import Resource, request
import json

lista_habilidades = [
    {"id": "0","habilidade" : "Python"}, 
    {"id": "1","habilidade" : "Java"},
    {"id": "2","habilidade" : "PHP"},
    {"id": "3","habilidade" : "HTML"},
    ]

class Habilidades(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            mensagem = "Habilidade de ID {} não existe". format(id)
            response = {"status" : "erro", "mensagem" : mensagem}
        except Exception:
            mensagem = "Erro desonhecido. Procure o administrador da API"
            response = {"status" : "erro", "mensagem" : mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados
    def delete(self, id):
        lista_habilidades.pop(id)
        return {"status" : "sucesso", "mensagem" : "habilidade excluida"}
    
class ListaHabilidades(Resource):
    def get (self):
        return lista_habilidades
    
    def post (self):
        dados = json.loads(request.data)
        if dados in lista_habilidades:
            return "habilidade ja existe"

        else:
            posicao = len(lista_habilidades)
            dados["id"] = posicao
            lista_habilidades.append(dados)
            
            return lista_habilidades[posicao]




          
    