from models import Pessoas

def insere_pessoas():
    pessoa= Pessoas(nome= "Rafaela", idade = 28)
    print(f"Usuario(a): {pessoa} adicionado")
    pessoa.save()

def consulta_todos():
    pessoa = Pessoas.query.all()
    print(f"Usuarios cadastrados: {pessoa}")

def costulta_usuario():
    usuario = Pessoas.query.filter_by(nome="Rafaela").first()
    print(f"Usuario: {usuario.nome}")
    print(f"Idade: {usuario.idade}")

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Rafaela").first()
    pessoa.idade = 29
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Rafaela").first()
    pessoa.delete()

if __name__ == "__main__":
    #insere_pessoas()
    consulta_todos()
    #costulta_usuario()
    #altera_pessoa()
    #exclui_pessoa()

