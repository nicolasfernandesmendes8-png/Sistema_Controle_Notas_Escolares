
import sqlite3
from pathlib import Path


# Caminho da pasta principal do projeto
PASTA_PROJETO = Path(__file__).resolve().parents[2]

# Arquivo do banco de dados
CAMINHO_BANCO = PASTA_PROJETO / "notas_escolares.db"


def conectar():
    """
    Estabelece conexão com o banco de dados SQLite.
    """
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_banco():
    """
    Cria o banco de dados e suas tabelas.
    """

    conexao = conectar()

    try:
        cursor = conexao.cursor()

        # Tabela de alunos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                matricula TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                curso TEXT NOT NULL
            )
        """)

        # Tabela de disciplinas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS disciplinas (
                codigo TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                carga_horaria INTEGER NOT NULL
            )
        """)

        # Tabela de avaliações
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS avaliacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula TEXT NOT NULL,
                codigo_disciplina TEXT NOT NULL,
                descricao TEXT NOT NULL,
                nota REAL NOT NULL,
                peso REAL NOT NULL DEFAULT 1,

                FOREIGN KEY (matricula)
                    REFERENCES alunos(matricula),

                FOREIGN KEY (codigo_disciplina)
                    REFERENCES disciplinas(codigo)
            )
        """)

        conexao.commit()

    finally:
        conexao.close()


if __name__ == "__main__":
    criar_banco()

    print("Banco de dados atualizado com sucesso!")
    print(f"Localização: {CAMINHO_BANCO}")
