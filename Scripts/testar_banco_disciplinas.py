
from src.database.disciplina_dao import DisciplinaDAO

dao = DisciplinaDAO()

print("CADASTRANDO DISCIPLINA...")

resultado = dao.cadastrar(
    "POO01",
    "Programação Orientada a Objetos",
    80
)

if resultado:
    print("Disciplina cadastrada com sucesso!")
else:
    print("Não foi possível cadastrar.")

print("\nDISCIPLINAS CADASTRADAS:")

disciplinas = dao.listar_todos()

for disciplina in disciplinas:
    print(disciplina)

print("\nTESTANDO EXCLUSÃO...")

if dao.excluir("POO01"):
    print("Disciplina excluída com sucesso!")
else:
    print("Disciplina não encontrada.")
