class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18


    def __str__(self) -> str:
        return f"{self.nome} - {self.idade}"


p =Pessoa("Evandro", 30)
print(p)

p2 = Pessoa.criar_apartir_data_nascimento(1996, 7, 25, "joao")
print(p2)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))