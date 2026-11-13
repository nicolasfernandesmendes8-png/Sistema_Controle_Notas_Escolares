
class Avaliacao:
    def __init__(self, descricao, nota, peso=1):
        self.descricao = descricao
        self.nota = nota
        self.peso = peso

    def calcular_pontuacao(self):
        return self.nota * self.peso

    def exibir_dados(self):
        return (
            f"Avaliação: {self.descricao}\n"
            f"Nota: {self.nota}\n"
            f"Peso: {self.peso}"
        )
