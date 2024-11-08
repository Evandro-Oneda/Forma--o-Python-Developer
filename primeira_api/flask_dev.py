from flask import Flask, jsonify, request
import json


app = Flask(__name__)


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


@app.route("/dev/<int:id>/", methods = ["GET","PUT","DELETE"])

# funcao para consultar / alterar / deletar usuario pela ID
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "desenvolvedor de ID {} não existe". format(id)
            response = {"status" : "erro", "mensagem" : mensagem}
        except Exception:
            mensagem = "Erro desonhecido. Procure o administrador da API"
            response = {"status" : "erro", "mensagem" : mensagem}
        return jsonify(response)
    
    elif request.method =="PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify ({"status": "sucesso", "mensagem" : "registro excluido"})


#listar todos os desenvolvedores e inclui novo desenvolvedor
@app.route("/dev/", methods= ["POST", "GET"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    
    elif request.method =="GET":
        return jsonify(desenvolvedores)



if __name__=="__main__":
    app.run(debug=True)