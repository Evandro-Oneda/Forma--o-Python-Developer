def exibir_mensagem():
    print("ola mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="anonimo"):
    print(f"seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="chapie")




def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucesso(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucesso(10))


def salvar_carro(marca,modelo,ano, placa):
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("fiat", "palio", 1999, "abc-1234")
salvar_carro(marca="fiat", modelo="palio", ano=1999, placa="abc-1234")
salvar_carro(**{"marca": "fiat", "modelo":"palio", "ano":1999, "placa":"abc-1234"})
salvar_carro(*("fiat", "palio", 1999, "abc-1234"))


def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "sex, 26 de agosto de 2022"
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)
