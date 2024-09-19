frutas = ["laranja", "maca", "uva"]

letras = list("Python")

numeros = list(range(10))

lista_carro = ["ferrari", "f8", 420000, 2020,2900, "sao paulo", True]

print(frutas[-1])
print(frutas[1])

matriz =[
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"]
]

print(matriz[0])
print(matriz [0][0])
print(matriz [0][-1])
print(matriz  [1][-1])

lista = ["p","y","t","h","o","n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

for carro in lista_carro:
    print(carro)

for indice, carro in enumerate(lista_carro):
    print(f"{indice}:{carro}")

lista.append("m")
print(lista)

