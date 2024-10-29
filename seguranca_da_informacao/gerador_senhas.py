import random, string

tamanho = int(input("Insira o tamanho da senha desejada: "))

chars = string.ascii_letters + string.digits + "ç!@#$%&*"

rnd = random.SystemRandom()

senha = ("".join(rnd.choice(chars) for i in range(tamanho)))

print(senha)