
import tkinter as tk
from tkinter import ttk, messagebox

from src.database.aluno_dao import AlunoDAO
from src.database.disciplina_dao import DisciplinaDAO
from src.database.avaliacao_dao import AvaliacaoDAO


class ConsultaBoletim:

    def __init__(self, janela_principal):

        self.janela = tk.Toplevel(janela_principal)
        self.janela.title("Consulta de Boletim - NFM")
        self.janela.geometry("850x600")
        self.janela.minsize(750, 500)
        self.janela.configure(bg="#f2f4f8")

        # Conexão com os bancos de dados
        self.aluno_dao = AlunoDAO()
        self.disciplina_dao = DisciplinaDAO()
        self.avaliacao_dao = AvaliacaoDAO()

        self.alunos = {}
        self.disciplinas = {}

        # Configuração visual
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Treeview",
            font=("Arial", 10),
            rowheight=28
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold"),
            background="#243b64",
            foreground="white"
        )

        estilo.configure(
            "Acao.TButton",
            font=("Arial", 10, "bold"),
            padding=9
        )

        # Cabeçalho
        cabecalho = tk.Frame(
            self.janela,
            bg="#243b64",
            height=75
        )
        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)

        tk.Label(
            cabecalho,
            text="CONSULTA DE BOLETIM",
            font=("Arial", 19, "bold"),
            bg="#243b64",
            fg="white"
        ).pack(pady=20)

        # Área principal
        principal = tk.Frame(
            self.janela,
            bg="#f2f4f8"
        )
        principal.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        # Seleção do aluno
        tk.Label(
            principal,
            text="Aluno:",
            font=("Arial", 11),
            bg="#f2f4f8"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.combo_aluno = ttk.Combobox(
            principal,
            width=45,
            state="readonly"
        )
        self.combo_aluno.grid(
            row=0, column=1, padx=10, pady=10, sticky="w"
        )

        # Seleção da disciplina
        tk.Label(
            principal,
            text="Disciplina:",
            font=("Arial", 11),
            bg="#f2f4f8"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.combo_disciplina = ttk.Combobox(
            principal,
            width=45,
            state="readonly"
        )
        self.combo_disciplina.grid(
            row=1, column=1, padx=10, pady=10, sticky="w"
        )

        # Botões
        botoes = tk.Frame(
            principal,
            bg="#f2f4f8"
        )
        botoes.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=12
        )

        ttk.Button(
            botoes,
            text="Consultar Boletim",
            style="Acao.TButton",
            command=self.consultar_boletim
        ).pack(side="left", padx=8)

        ttk.Button(
            botoes,
            text="Limpar",
            style="Acao.TButton",
            command=self.limpar_consulta
        ).pack(side="left", padx=8)

        # Tabela de avaliações
        area_tabela = tk.LabelFrame(
            principal,
            text="Avaliações do Aluno",
            font=("Arial", 11, "bold"),
            bg="#f2f4f8",
            fg="#243b64",
            padx=10,
            pady=10
        )
        area_tabela.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="nsew",
            pady=15
        )

        colunas = ("id", "descricao", "nota", "peso")

        self.tabela = ttk.Treeview(
            area_tabela,
            columns=colunas,
            show="headings",
            height=8
        )

        self.tabela.heading("id", text="ID")
        self.tabela.heading("descricao", text="Avaliação")
        self.tabela.heading("nota", text="Nota")
        self.tabela.heading("peso", text="Peso")

        self.tabela.column("id", width=60, anchor="center")
        self.tabela.column("descricao", width=350)
        self.tabela.column("nota", width=100, anchor="center")
        self.tabela.column("peso", width=100, anchor="center")

        barra = ttk.Scrollbar(
            area_tabela,
            orient="vertical",
            command=self.tabela.yview
        )

        self.tabela.configure(yscrollcommand=barra.set)

        self.tabela.pack(
            side="left",
            fill="both",
            expand=True
        )

        barra.pack(side="right", fill="y")

        # Resultado do boletim
        self.resultado = tk.Label(
            principal,
            text="Média: -- | Situação: --",
            font=("Arial", 16, "bold"),
            bg="#f2f4f8",
            fg="#243b64"
        )
        self.resultado.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=15
        )

        principal.grid_columnconfigure(1, weight=1)
        principal.grid_rowconfigure(3, weight=1)

        # Rodapé
        tk.Label(
            self.janela,
            text="Sistema de Controle de Notas Escolares | "
                 "NFM - Núcleo de Formação Moderna | 2026",
            font=("Arial", 9),
            bg="#e1e6ef",
            fg="#555555",
            pady=10
        ).pack(fill="x", side="bottom")

        # Carrega os dados
        self.carregar_alunos()
        self.carregar_disciplinas()

    # Carregar alunos cadastrados
    def carregar_alunos(self):

        try:
            registros = self.aluno_dao.listar_todos()

            self.alunos = {
                f"{aluno[1]} - {aluno[0]}": aluno[0]
                for aluno in registros
            }

            self.combo_aluno["values"] = list(self.alunos.keys())

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar os alunos:\n{erro}",
                parent=self.janela
            )

    # Carregar disciplinas cadastradas
    def carregar_disciplinas(self):

        try:
            registros = self.disciplina_dao.listar_todos()

            self.disciplinas = {
                f"{disciplina[1]} - {disciplina[0]}": disciplina[0]
                for disciplina in registros
            }

            self.combo_disciplina["values"] = list(
                self.disciplinas.keys()
            )

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar as disciplinas:\n{erro}",
                parent=self.janela
            )

    # Consultar boletim
    def consultar_boletim(self):

        aluno_selecionado = self.combo_aluno.get()
        disciplina_selecionada = self.combo_disciplina.get()

        if not aluno_selecionado or not disciplina_selecionada:
            messagebox.showwarning(
                "Atenção",
                "Selecione um aluno e uma disciplina.",
                parent=self.janela
            )
            return

        matricula = self.alunos[aluno_selecionado]
        codigo_disciplina = self.disciplinas[
            disciplina_selecionada
        ]

        try:
            avaliacoes = self.avaliacao_dao.listar_por_aluno_disciplina(
                matricula,
                codigo_disciplina
            )

            # Limpa a tabela
            self.tabela.delete(*self.tabela.get_children())

            if not avaliacoes:
                self.resultado.config(
                    text="Média: -- | Situação: Sem avaliações",
                    fg="#555555"
                )

                messagebox.showinfo(
                    "Consulta",
                    "Não existem avaliações cadastradas para "
                    "este aluno nesta disciplina.",
                    parent=self.janela
                )
                return

            total_pontos = 0
            total_pesos = 0

            # Exibe as avaliações e calcula a média
            for avaliacao in avaliacoes:

                id_avaliacao = avaliacao[0]
                descricao = avaliacao[1]
                nota = float(avaliacao[2])
                peso = float(avaliacao[3])

                self.tabela.insert(
                    "",
                    "end",
                    values=(
                        id_avaliacao,
                        descricao,
                        f"{nota:.2f}",
                        f"{peso:.2f}"
                    )
                )

                total_pontos += nota * peso
                total_pesos += peso

            if total_pesos <= 0:
                self.resultado.config(
                    text="Média: -- | Situação: Pesos inválidos",
                    fg="#b00020"
                )
                return

            media = total_pontos / total_pesos

            # Critério de aprovação: média igual ou superior a 7
            if media >= 7:
                situacao = "Aprovado"
                cor = "#176b45"
            else:
                situacao = "Reprovado"
                cor = "#b00020"

            self.resultado.config(
                text=f"Média: {media:.2f} | Situação: {situacao}",
                fg=cor
            )

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível consultar o boletim:\n{erro}",
                parent=self.janela
            )

    # Limpar consulta
    def limpar_consulta(self):

        self.combo_aluno.set("")
        self.combo_disciplina.set("")

        self.tabela.delete(*self.tabela.get_children())

        self.resultado.config(
            text="Média: -- | Situação: --",
            fg="#243b64"
        )


if __name__ == "__main__":
    janela = tk.Tk()
    janela.withdraw()

    app = ConsultaBoletim(janela)

    janela.mainloop()
