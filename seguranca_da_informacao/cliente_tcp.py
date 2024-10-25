import socket
import sys

def main ():
    try:
        s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro: 
        print("A conexão falhou!!!")
        print(f'Erro: {erro}')
        sys.exit()
    print("socket criado com sucesso")

    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f"Cliente TCP conectado com sucesso no host: {HostAlvo} na porta: {PortaAlvo}")
    except socket.error as erro: 
        print(f"A conexão falhou ao tentar se conectar ao host : {HostAlvo} porta {PortaAlvo}")
        print(f'Erro: {erro}')
        sys.exit()

if __name__ == "__main__":
    main()

