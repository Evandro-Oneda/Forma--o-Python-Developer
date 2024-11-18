class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basico", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("plano invalido")
        self.plano = plano

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print(f"plano alterado para: {novo_plano}")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print("ver filme")

        elif self.plano != plano_filme:
            print("mudar plano")
        else:
            print("plano invalido")



evandro = Cliente("evandro", "evandro.oneda@hotmail.com", "basico")
print(evandro.plano)
# lira = Cliente("lira", "lira@hotmail.com", "super")
# print(lira.plano)

evandro.mudar_plano("premium")
print(evandro.plano)

evandro.ver_filme("madagascar", "premium")
evandro.ver_filme("madagascar", "basico")


