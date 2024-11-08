from flask import Flask, jsonify, request
import json


app = Flask(__name__)

@app.route("/<int:id>")

def pessoas(id):
    return jsonify({"id":id, "nome": "Evandro"})

@app.route("/somar/<int:valor1>/<int:valor2>/")
def somar(valor1, valor2):
    return jsonify({"somar" :valor1 + valor2})

@app.route("/soma", methods=["POST","GET"])
def soma():
    if request.method =="POST":
        dados = json.loads(request.data)
        print(dados)
        total = sum(dados["valores"])
    elif request.method =="GET":
        total = 10 + 10
    return jsonify({"soma":total})

if __name__=="__main__":
    app.run(debug=True)