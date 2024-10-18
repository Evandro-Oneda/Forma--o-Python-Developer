class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura, marca):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        self.marca = marca
    
    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "-":
            print("diminuir canal")
        else:
            print("opcao invalida")


lg = ControleRemoto("preto", 10, 15, 2, "LG")
print(lg.cor,lg.altura, lg.profundidade, lg.largura, lg.marca )

lg.passar_canal("+")
lg.passar_canal("-")
lg.passar_canal(".")

