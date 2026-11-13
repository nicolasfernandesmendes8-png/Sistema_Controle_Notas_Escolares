
from src.models.aluno import Aluno
from src.models.disciplina import Disciplina
from src.models.avaliacao import Avaliacao
from src.models.boletim import Boletim

# Criando um aluno
aluno = Aluno("2026001", "João Silva", "Ciência da Computação")

# Criando uma disciplina
disciplina = Disciplina(
    "POO01",
    "Programação Orientada a Objetos",
    80
)

# Criando o boletim
boletim = Boletim(aluno, disciplina)

# Registrando as avaliações
prova = Avaliacao("Prova 1", 8.0, 2)
trabalho = Avaliacao("Trabalho", 9.0, 1)

boletim.adicionar_avaliacao(prova)
boletim.adicionar_avaliacao(trabalho)

# Exibindo os resultados
print("SISTEMA DE CONTROLE DE NOTAS")
print("----------------------------")
print(aluno.exibir_dados())
print()
print(disciplina.exibir_dados())
print()
print("Média:", round(boletim.calcular_media(), 2))
print("Situação:", boletim.verificar_situacao())
