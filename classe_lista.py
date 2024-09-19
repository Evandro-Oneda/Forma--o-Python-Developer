cores = ["vermelho", "azul", "verde","azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))


linguagens = ["python","js", "c"]
print(linguagens)
linguagens.extend(["java", "csharp"])
print(linguagens)

print(linguagens.index("java"))
print(linguagens.index("csharp"))

linguagens.pop()
print(linguagens)
linguagens.pop(0)
print(linguagens)

linguagens.remove("c")
print(linguagens)

linguagens.reverse()
print(linguagens)

linguagens.clear()
print(linguagens)

linguagens = ["python","js", "c","java", "csharp"]
linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key=lambda x:len(x))
print(linguagens)

linguagens.sort(key=lambda x:len(x), reverse=True)
print(linguagens)

print(len(linguagens))






