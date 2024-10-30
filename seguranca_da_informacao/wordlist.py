import itertools

string = input("Informe a string a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for caracter in resultado:
    print("".join(caracter))