
import unittest

from src.models.aluno import Aluno
from src.models.disciplina import Disciplina
from src.models.avaliacao import Avaliacao
from src.models.boletim import Boletim


class TestSistemaNotas(unittest.TestCase):

    def setUp(self):
        self.aluno = Aluno(
            "2026001",
            "João Silva",
            "Ciência da Computação"
        )

        self.disciplina = Disciplina(
            "POO01",
            "Programação Orientada a Objetos",
            80
        )

        self.boletim = Boletim(
            self.aluno,
            self.disciplina
        )

    def test_criar_aluno(self):
        self.assertEqual(self.aluno.nome, "João Silva")
        self.assertEqual(self.aluno.matricula, "2026001")

    def test_criar_disciplina(self):
        self.assertEqual(
            self.disciplina.nome,
            "Programação Orientada a Objetos"
        )

    def test_calcular_pontuacao(self):
        avaliacao = Avaliacao("Prova 1", 8.0, 2)
        self.assertEqual(avaliacao.calcular_pontuacao(), 16.0)

    def test_calcular_media_ponderada(self):
        self.boletim.adicionar_avaliacao(
            Avaliacao("Prova 1", 8.0, 2)
        )
        self.boletim.adicionar_avaliacao(
            Avaliacao("Trabalho", 9.0, 1)
        )

        self.assertAlmostEqual(
            self.boletim.calcular_media(),
            8.33,
            places=2
        )

    def test_situacao_aprovado(self):
        self.boletim.adicionar_avaliacao(
            Avaliacao("Prova", 8.0, 1)
        )

        self.assertEqual(
            self.boletim.verificar_situacao(),
            "Aprovado"
        )

    def test_situacao_reprovado(self):
        self.boletim.adicionar_avaliacao(
            Avaliacao("Prova", 5.0, 1)
        )

        self.assertEqual(
            self.boletim.verificar_situacao(),
            "Reprovado"
        )

    def test_boletim_sem_avaliacoes(self):
        self.assertEqual(
            self.boletim.calcular_media(),
            0
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
