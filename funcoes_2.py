def somar(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    return a//b

def multi(a, b):
    return a*b


def exibir_resultado(a,b, funcao):
    resultado = funcao(a,b)
    print(f"o resultado da operacao = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, sub)
exibir_resultado(10, 10, div)
exibir_resultado(10, 10, multi)