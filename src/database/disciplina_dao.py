
from src.database.conexao import conectar


class DisciplinaDAO:

    def cadastrar(self, codigo, nome, carga_horaria):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                INSERT INTO disciplinas
                (codigo, nome, carga_horaria)
                VALUES (?, ?, ?)
            """, (codigo, nome, carga_horaria))

            conexao.commit()
            return True

        except Exception as erro:
            print(f"Erro ao cadastrar disciplina: {erro}")
            return False

        finally:
            conexao.close()

    def listar_todos(self):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT codigo, nome, carga_horaria
                FROM disciplinas
                ORDER BY nome
            """)

            return cursor.fetchall()

        finally:
            conexao.close()

    def excluir(self, codigo):
        conexao = conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                DELETE FROM disciplinas
                WHERE codigo = ?
            """, (codigo,))

            conexao.commit()
            return cursor.rowcount > 0

        finally:
            conexao.close()
