import hashlib

string = input("digite a o texto a ser transformado: ")

menu = int(input('''
                 
########MENU ########
             
Digite o numero do hash desejado:
1) MD5
2)SHA1
3)SHA256
4)SHA512
             
'''))

if menu ==1:
    resultado = hashlib.md5(string.encode("utf-8"))
    print("o hash da string é: ", resultado.hexdigest())


elif menu == 2:
    resultado = hashlib.sha1(string.encode("utf-8"))
    print("o hash SHA1 é: ", resultado.hexdigest())

elif menu == 3:

    resultado = hashlib.sha256(string.encode("utf-8"))
    print("o hash sha256 é: ", resultado.hexdigest())

elif menu == 4:

    resultado = hashlib.sha512(string.encode("utf-8"))
    print("o hash sha512 é: ", resultado.hexdigest())

else:
    print("opcao invalida!!!")