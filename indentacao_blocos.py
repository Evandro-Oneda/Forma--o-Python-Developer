
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")

    print("obrigado por ser nosso cliente")

def depositar(valor):
    saldo = 500

    saldo += valor
    print("total da conta:", saldo)

sacar(500)

depositar(1000)