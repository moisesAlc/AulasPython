class Automovel:
    # Variável estática, pertencente à classe Automóvel (veremos mais na próxima aula)
    contagem: int = 1

    def __init__(self, nome: str, marca: str, ano: int, cor: str, alugado: bool):
        self.nome = nome,
        self.marca = marca,
        self.ano = ano,
        self.cor = cor
        self.numero = Automovel.contagem,
        self.situacao_aluguel = alugado
        Automovel.contagem += 1

    def __init__(self, automovel: tuple):
        self.nome = automovel[1],
        self.marca = automovel[2],
        self.ano = automovel[3],
        self.cor = automovel[4],
        self.numero = automovel[0],
        self.situacao_aluguel = bool(automovel[5])
        Automovel.contagem += 1

    def get_nome(self):
        return self.nome[0]

    def get_situacao_aluguel(self):
        return "Alugado" if self.situacao_aluguel else "Disponível para alugar"

    def muda_cor(self, cor):
        self.cor = cor

    def aluga_carro(self):
        self.situacao_aluguel = True

    def libera_carro(self):
        self.situacao_aluguel = False
