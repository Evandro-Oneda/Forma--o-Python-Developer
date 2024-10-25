import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("socket criado com sucesso")

host = "localhost"
porta = 5432

s.bind((host, porta))
mensagem = " ola cliente"

while 1:
    dados, endereco =  s.recvfrom(4096)

    if dados:
        print("servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), endereco)