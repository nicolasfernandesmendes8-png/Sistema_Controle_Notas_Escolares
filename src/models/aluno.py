
class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso

    def exibir_dados(self):
        return (
            f"Matrícula: {self.matricula}\n"
            f"Nome: {self.nome}\n"
            f"Curso: {self.curso}"
        )
