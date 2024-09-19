texto = input("informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print()

lista_precos = [10,20,200,50,300,1000]

for preco in lista_precos:
    imposto = preco *0.1
    total = imposto + preco
    print(int(total))

for numero in range(0,11):
    print(numero, end=" ")
print()
for numero in range(0, 51, 5):
    print(numero, end=" ")