pessoa = {"nome": "guilherme", "idade":28}

pessoa["telefone"] = "3333-1234"

print(pessoa)

print(pessoa["nome"])

pessoa["nome"] = "evandro"
print(pessoa["nome"])

contatos ={
    "teste1":{"nome": "nome1", "telefone":"telefone1"},
    "teste2":{"nome": "nome2", "telefone":"telefone2"},
    "teste3":{"nome": "nome3", "telefone":"telefone3"}
}
print(contatos["teste1"]["telefone"])


for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)