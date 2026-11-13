
from src.database.conexao import conectar


class AvaliacaoDAO:

    def cadastrar(
        self,
        matricula,
        codigo_disciplina,
        descricao,
        nota,
        peso=1
    ):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                INSERT INTO avaliacoes (
                    matricula,
                    codigo_disciplina,
                    descricao,
                    nota,
                    peso
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                matricula,
                codigo_disciplina,
                descricao,
                nota,
                peso
            ))

            conexao.commit()
            return True

        except Exception as erro:
            print(f"Erro ao cadastrar avaliação: {erro}")
            return False

        finally:
            conexao.close()

    def listar_por_aluno_disciplina(
        self,
        matricula,
        codigo_disciplina
    ):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id, descricao, nota, peso
                FROM avaliacoes
                WHERE matricula = ?
                AND codigo_disciplina = ?
                ORDER BY id
            """, (matricula, codigo_disciplina))

            return cursor.fetchall()

        finally:
            conexao.close()

    def excluir(self, id_avaliacao):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                DELETE FROM avaliacoes
                WHERE id = ?
            """, (id_avaliacao,))

            conexao.commit()

            return cursor.rowcount > 0

        finally:
            conexao.close()
