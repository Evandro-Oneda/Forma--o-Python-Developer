from sqlalchemy import create_engine, Column, String, Integer,Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo =True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)


#crud  
# criar 
lira = Usuario (nome = "lira", email="teste@teste.com", senha="123")
session.add(lira)
session.commit()

livro = Livro (titulo="teste1",qtde_paginas=10, dono="usuario")
session.add(livro)
session.commit()



# ler
# lista_usuarios = session.query(Usuario).all()
# print(lista_usuarios)
usuario_lira = session.query(Usuario). filter_by(nome="evandro").first()
# print(lista_usuarios)
#usuario_lira = session.query(Usuario). filter_by(email="teste@teste.com").all()
print(usuario_lira)
# print(usuario_lira.nome)
# print(usuario_lira.email)
# print(usuario_lira.senha)



# vento_levou= Livro (titulo="vento_levou",qtde_paginas=100, dono=usuario_lira.id)
# session.add(vento_levou)
# session.commit()

# update

# usuario_lira.nome = "joao lira"
# session.add(usuario_lira)
# session.commit()

# deletar

session.delete(usuario_lira)
session.commit()

