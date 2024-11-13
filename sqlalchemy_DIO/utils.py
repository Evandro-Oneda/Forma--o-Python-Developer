from models import Pessoas, Usuarios


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

def novo_login(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == "__main__":
    #insere_pessoas()
    #consulta_todos()
    #costulta_usuario()
    #altera_pessoa()
    #exclui_pessoa()
    # novo_login("Matheus", "123")
    # novo_login("Mari","123")
    novo_login("Evandro","123")
    novo_login("Andreia","123")
    novo_login("Rafaela","123")
    consulta_usuarios()

