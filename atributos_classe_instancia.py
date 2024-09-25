class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrat_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno_1 = Estudante("Guilhemre",1)
aluno_2 = Estudante("Evandro", 2)

print(aluno_1)
print(aluno_2)
mostrat_valores(aluno_1, aluno_2)

aluno_1.matricula = 3
mostrat_valores(aluno_1, aluno_2)
Estudante.escola = "Python"
aluno_3 = Estudante("Pedro", 3)
mostrat_valores(aluno_1, aluno_2, aluno_3)
