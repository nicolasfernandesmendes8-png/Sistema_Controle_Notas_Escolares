
class Disciplina:
    def __init__(self, codigo, nome, carga_horaria):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria

    def exibir_dados(self):
        return (
            f"Código: {self.codigo}\n"
            f"Disciplina: {self.nome}\n"
            f"Carga horária: {self.carga_horaria} horas"
        )
