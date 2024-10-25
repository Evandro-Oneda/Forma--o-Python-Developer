import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM,)

print("cliente socket criado com sucesso")

host = "localhost"
porta = 5433
mensagem = " ola servidor"

try:
    print(f"Cliente: {mensagem}")
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")
finally:
    print("cliente: fechando a conexão")
    s.close()