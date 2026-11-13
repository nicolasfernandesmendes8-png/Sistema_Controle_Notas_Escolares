
from src.database.conexao import conectar


class AlunoDAO:

    def cadastrar(self, matricula, nome, curso):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                INSERT INTO alunos (matricula, nome, curso)
                VALUES (?, ?, ?)
            """, (matricula, nome, curso))

            conexao.commit()
            return True

        except Exception as erro:
            print(f"Erro ao cadastrar aluno: {erro}")
            return False

        finally:
            conexao.close()

    def listar_todos(self):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT matricula, nome, curso
                FROM alunos
                ORDER BY nome
            """)

            return cursor.fetchall()

        finally:
            conexao.close()

    def excluir(self, matricula):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                DELETE FROM alunos
                WHERE matricula = ?
            """, (matricula,))

            conexao.commit()

            return cursor.rowcount > 0

        finally:
            conexao.close()
