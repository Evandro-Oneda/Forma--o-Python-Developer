saldo = 2000
cheque_especial = 450
conta = int(input("[1] conta normal \n[2] conta universitaria\ninforme uma opcao:\n"))

if conta == 1:
    saque = float(input("informe o valor do saque: "))
    if saldo >= saque:
        print("saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com sucesso com uso de cheque especial")
    else:
        print("saldo insuficiente conta normal")



elif conta == 2:
    saque = float(input("informe o valor do saque: "))
    if saldo >= saque:
        print("saque realizado com sucesso")

    else:
        print("saldo insuficiente")

else:
    print("conta invalida")

