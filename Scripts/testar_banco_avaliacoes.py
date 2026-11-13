from src.database.avaliacao_dao import AvaliacaoDAO

dao = AvaliacaoDAO()

print("\n===== EXCLUINDO AVALIAÇÃO DE TESTE =====")

if dao.excluir(3):
    print("Avaliação excluída com sucesso!")
else:
    print("Avaliação não encontrada.")

print("\n===== CONFERINDO REGISTROS =====")

avaliacoes = dao.listar_por_aluno_disciplina(
    "2026006",
    "003"
)

print("Avaliações restantes:", avaliacoes)