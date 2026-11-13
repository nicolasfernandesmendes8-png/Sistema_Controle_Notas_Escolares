
import unittest
import uuid

from src.database.aluno_dao import AlunoDAO
from src.database.disciplina_dao import DisciplinaDAO
from src.database.avaliacao_dao import AvaliacaoDAO


class TestBancoDeDados(unittest.TestCase):

    def setUp(self):
        self.aluno_dao = AlunoDAO()
        self.disciplina_dao = DisciplinaDAO()
        self.avaliacao_dao = AvaliacaoDAO()

        # Identificadores exclusivos para cada teste
        identificador = uuid.uuid4().hex[:8].upper()

        self.matricula = f"TESTE{identificador}"
        self.codigo = f"TESTE{identificador}"

        # Cadastra o aluno de teste
        resultado_aluno = self.aluno_dao.cadastrar(
            self.matricula,
            "Aluno de Teste",
            "Ciência da Computação"
        )

        self.assertTrue(resultado_aluno)

        # Cadastra a disciplina de teste
        resultado_disciplina = self.disciplina_dao.cadastrar(
            self.codigo,
            "Disciplina de Teste",
            60
        )

        self.assertTrue(resultado_disciplina)

    def tearDown(self):
        # Exclui primeiro as avaliações
        avaliacoes = (
            self.avaliacao_dao.listar_por_aluno_disciplina(
                self.matricula,
                self.codigo
            )
        )

        for avaliacao in avaliacoes:
            self.avaliacao_dao.excluir(avaliacao[0])

        # Depois exclui aluno e disciplina
        self.aluno_dao.excluir(self.matricula)
        self.disciplina_dao.excluir(self.codigo)

    def test_cadastrar_e_listar_aluno(self):
        alunos = self.aluno_dao.listar_todos()

        self.assertTrue(
            any(aluno[0] == self.matricula for aluno in alunos)
        )

    def test_cadastrar_e_listar_disciplina(self):
        disciplinas = self.disciplina_dao.listar_todos()

        self.assertTrue(
            any(
                disciplina[0] == self.codigo
                for disciplina in disciplinas
            )
        )

    def test_cadastrar_e_listar_avaliacao(self):
        resultado = self.avaliacao_dao.cadastrar(
            self.matricula,
            self.codigo,
            "Prova de Teste",
            8.0,
            2
        )

        self.assertTrue(resultado)

        avaliacoes = (
            self.avaliacao_dao.listar_por_aluno_disciplina(
                self.matricula,
                self.codigo
            )
        )

        self.assertTrue(
            any(
                avaliacao[1] == "Prova de Teste"
                for avaliacao in avaliacoes
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
