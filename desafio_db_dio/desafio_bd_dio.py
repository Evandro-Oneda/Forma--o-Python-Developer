from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float, Select, Connection, Update
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///desafio_db_dio.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    cpf = Column("cpf", String)
    endereco= Column("endereco", String)

    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco


class Conta(Base):
    __tablename__ = "contas"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    tipo = Column("tipo", String)
    agencia = Column("agencia", Integer)
    saldo = Column("saldo",Float)
    id_cliente = Column("id_cliente", ForeignKey("clientes.id"))

    def __init__(self, tipo, agencia, saldo, id_cliente):
        self.tipo = tipo
        self.agencia = agencia
        self.saldo = saldo 
        self.id_cliente = id_cliente

Base.metadata.create_all(bind=db)


# #criar usuarios

evandro = Cliente(nome = "Evandro", cpf = "123.456.789-80", endereco = "Rua maria joao")
session.add(evandro)
session.commit()

maria = Cliente(nome = "Maria", cpf = "987.654.321-10", endereco = "Rua qualquer")
session.add(maria)
session.commit()

paulo = Cliente(nome = "Paulo", cpf = "456.789.123-20", endereco = "Rua mais uma")
session.add(paulo)
session.commit()

#criando contas

conta_corrente_evandro = Conta(tipo="corrente", agencia="1234", saldo = "1000", id_cliente = evandro.id)
session.add(conta_corrente_evandro)
session.commit()

conta_poupanca_maria = Conta(tipo="poupança", agencia="4561", saldo = "5000", id_cliente = maria.id)
session.add(conta_poupanca_maria)
session.commit()

conta_poupanca_evandro = Conta(tipo="poupança", agencia="1234", saldo = "2000", id_cliente = evandro.id)
session.add(conta_poupanca_evandro)
session.commit()

conta_corrente_paulo = Conta(tipo="corrente", agencia="5675", saldo = "8000", id_cliente = paulo.id)
session.add(conta_corrente_paulo)
session.commit()


#consultando informacoes

localizar = session.query(Cliente).filter_by(nome="Evandro").first()
print(f"ID: {localizar.id} NOME: {localizar.nome} CPF:{localizar.cpf} ENDERECO: {localizar.endereco}")

for instace in session.query(Cliente).order_by(Cliente.id):
    print(instace.nome)


#atualizar

mudar_nome = session.query(Cliente).filter_by(nome="Maria").first()
mudar_nome.nome = "marelinda"
session.add(mudar_nome)
session.commit()


#deletar


deletar_usuario = session.query(Cliente).filter_by(nome="marelinda").first()
session.delete(deletar_usuario)
session.commit()