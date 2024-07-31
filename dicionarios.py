pessoa = {"nome": "guilherme", "idade":28}

pessoa["telefone"] = "3333-1234"

print(pessoa)

print(pessoa["nome"])

pessoa["nome"] = "evandro"
print(pessoa["nome"])

contatos ={
    "teste1":{"nome1": "nome1", "telefone1":"telefone1"},
    "teste2":{"nome2": "nome2", "telefone1":"telefone2"},
    "teste3":{"nome3": "nome3", "telefone1":"telefone3"}
}
print(contatos["teste1"]["telefone1"])


for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)