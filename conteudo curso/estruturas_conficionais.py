saldo = 2000
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("realizado saque")

else:
    print("saldo insuficiente")


opcao = int(input("informe uma opcao:\n [1] sacar \n [2] extrato"))

if opcao == 1:
    print("sacar valor")

elif opcao == 2:
    print("extrato")

else:
    print("nenhuma opcao valida")