
class Boletim:
    def __init__(self, aluno, disciplina):
        self.aluno = aluno
        self.disciplina = disciplina
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def calcular_media(self):
        if not self.avaliacoes:
            return 0

        total_pontos = sum(
            avaliacao.calcular_pontuacao()
            for avaliacao in self.avaliacoes
        )

        total_pesos = sum(
            avaliacao.peso
            for avaliacao in self.avaliacoes
        )

        return total_pontos / total_pesos

    def verificar_situacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        return "Reprovado"
