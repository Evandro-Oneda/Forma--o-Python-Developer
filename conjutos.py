"""x=set([1,2,3,1,3,4])
print(x)

x=set("abacaxi")
print(x)

x=set(("palio", "gol", "celta","palio"))
x= list(x)
print(type(x))
"""

carros = {"gol","celta","palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#conjunto_a = {1,2}
#conjunto_b = {3,4}

#print(conjunto_a.union(conjunto_b))

conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.intersection(conjunto_b))

print(conjunto_a.difference(conjunto_b))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_b))

sorteio ={1,23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)