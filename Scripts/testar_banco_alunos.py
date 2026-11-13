
from src.database.aluno_dao import AlunoDAO

dao = AlunoDAO()

# Testando cadastro
print("CADASTRANDO ALUNO...")

resultado = dao.cadastrar(
    "2026005",
    "Carlos Henrique",
    "Ciência da Computação"
)

if resultado:
    print("Aluno cadastrado com sucesso!")
else:
    print("Não foi possível cadastrar.")

# Consultando alunos
print("\nLISTA DE ALUNOS CADASTRADOS:")

alunos = dao.listar_todos()

for aluno in alunos:
    print(aluno)

# Testando exclusão
print("\nTESTANDO EXCLUSÃO...")

if dao.excluir("2026005"):
    print("Aluno excluído com sucesso!")
else:
    print("Aluno não encontrado.")
