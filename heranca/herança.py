class veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_roda = numero_rodas
        

    def ligar_motor(self):
        print("ligando motor")

    def __str__(self):
       return f"{self.__class__.__name__}:{','.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"

    
class motocicleta(veiculo):
    
    pass
class Carro(veiculo):
    pass
class Caminhao(veiculo):
    def __init__(self,cor,placa,numero_rodas,carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado=carregado

    def esta_carregado(self):
        print(f"{'sim' if self.carregado else 'nao'} estou carregado")
        
    pass


moto =motocicleta("vermelha","abc-1234", 2)
moto.ligar_motor()

carro = Carro("azul","adf-2587", 4)
print(carro)
carro.ligar_motor()

caminhao = Caminhao("preto", "dsf-6547", 8, False)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
print(moto)
print(carro)