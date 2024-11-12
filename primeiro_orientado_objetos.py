class bicicleta:
    def __init__(self,cor,modelo,ano, valor):
        self.cor =cor
        self.modelo =modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("buzinando")

    def parar(self):
        print("parado")
        print("biciclata parada")

    def correr(self):
        print("correndo!!!!")

    def get_cor(self):
        return self.cor
    
    #def __str__(self):
     #   return f"Bicicleta:cor ={self.cor}, modelo= {self.modelo}, ano= {self.ano},valor= {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}:{','.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"
 

        
caloi = bicicleta("vermelha","caloi",2022,680)
caloi.buzinar()
caloi.parar()
caloi.correr()
print(caloi.cor,caloi.modelo, caloi.ano, caloi.valor)
print(caloi.get_cor())

print(caloi)
