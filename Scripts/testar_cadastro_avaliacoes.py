
from src.database.avaliacao_dao import AvaliacaoDAO

dao = AvaliacaoDAO()

print("\n===== CADASTRANDO AVALIAÇÕES =====")

resultado1 = dao.cadastrar(
    "2026001",
    "003",
    "Prova 1",
    8.0,
    2
)

resultado2 = dao.cadastrar(
    "2026001",
    "003",
    "Trabalho",
    9.0,
    1
)

if resultado1 and resultado2:
    print("Avaliações cadastradas com sucesso!")
else:
    print("Erro ao cadastrar avaliações.")

print("\n===== CONSULTANDO AVALIAÇÕES =====")

avaliacoes = dao.listar_por_aluno_disciplina(
    "2026001",
    "003"
)

for avaliacao in avaliacoes:
    print(avaliacao)

print("\n===== CALCULANDO MÉDIA =====")

if avaliacoes:
    soma_pontos = sum(
        nota * peso for _, _, nota, peso in avaliacoes
    )

    soma_pesos = sum(
        peso for _, _, nota, peso in avaliacoes
    )

    media = soma_pontos / soma_pesos

    print(f"Média do aluno: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")
