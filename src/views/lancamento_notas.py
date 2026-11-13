
import tkinter as tk
from tkinter import ttk, messagebox

from src.database.conexao import conectar
from src.database.avaliacao_dao import AvaliacaoDAO
from src.models.avaliacao import Avaliacao
from src.models.boletim import Boletim
from src.models.aluno import Aluno
from src.models.disciplina import Disciplina


class LancamentoNotas:

    def __init__(self, janela):
        self.janela = tk.Toplevel(janela)
        self.janela.transient(janela)

        self.janela.title("Lançamento de Notas")
        self.janela.geometry("900x600")
        self.janela.resizable(False, False)

        self.dao = AvaliacaoDAO()

        self.alunos = {}
        self.disciplinas = {}

        self.criar_interface()
        self.carregar_alunos()
        self.carregar_disciplinas()

    def criar_interface(self):

        titulo = tk.Label(
            self.janela,
            text="Lançamento de Notas",
            font=("Arial", 18, "bold"),
            bg="#174A7E",
            fg="white",
            pady=15
        )
        titulo.pack(fill="x")

        formulario = tk.Frame(
            self.janela,
            padx=20,
            pady=15
        )
        formulario.pack(fill="x")

        tk.Label(formulario, text="Aluno:").grid(
            row=0, column=0, sticky="w", pady=7
        )

        self.combo_aluno = ttk.Combobox(
            formulario,
            width=45,
            state="readonly"
        )
        self.combo_aluno.grid(
            row=0, column=1, padx=10, pady=7
        )
        self.combo_aluno.bind(
            "<<ComboboxSelected>>",
            self.selecionar_aluno
        )

        tk.Label(formulario, text="Disciplina:").grid(
            row=1, column=0, sticky="w", pady=7
        )

        self.combo_disciplina = ttk.Combobox(
            formulario,
            width=45,
            state="readonly"
        )
        self.combo_disciplina.grid(
            row=1, column=1, padx=10, pady=7
        )
        self.combo_disciplina.bind(
            "<<ComboboxSelected>>",
            self.selecionar_disciplina
        )

        tk.Label(formulario, text="Avaliação:").grid(
            row=2, column=0, sticky="w", pady=7
        )

        self.entrada_descricao = tk.Entry(
            formulario,
            width=48
        )
        self.entrada_descricao.grid(
            row=2, column=1, padx=10, pady=7
        )

        tk.Label(formulario, text="Nota (0 a 10):").grid(
            row=3, column=0, sticky="w", pady=7
        )

        self.entrada_nota = tk.Entry(
            formulario,
            width=15
        )
        self.entrada_nota.grid(
            row=3, column=1, padx=10, pady=7, sticky="w"
        )

        tk.Label(formulario, text="Peso:").grid(
            row=4, column=0, sticky="w", pady=7
        )

        self.entrada_peso = tk.Entry(
            formulario,
            width=15
        )
        self.entrada_peso.insert(0, "1")
        self.entrada_peso.grid(
            row=4, column=1, padx=10, pady=7, sticky="w"
        )

        botoes = tk.Frame(self.janela)
        botoes.pack(pady=10)

        tk.Button(
            botoes,
            text="Lançar Nota",
            width=18,
            command=self.cadastrar_avaliacao
        ).pack(side="left", padx=5)

        tk.Button(
            botoes,
            text="Limpar",
            width=15,
            command=self.limpar_campos
        ).pack(side="left", padx=5)

        tk.Button(
            botoes,
            text="Excluir Avaliação",
            width=18,
            command=self.excluir_avaliacao
        ).pack(side="left", padx=5)

        # Tabela de avaliações
        colunas = ("id", "descricao", "nota", "peso")

        self.tabela = ttk.Treeview(
            self.janela,
            columns=colunas,
            show="headings",
            height=10
        )

        self.tabela.heading("id", text="ID")
        self.tabela.heading("descricao", text="Avaliação")
        self.tabela.heading("nota", text="Nota")
        self.tabela.heading("peso", text="Peso")

        self.tabela.column("id", width=70, anchor="center")
        self.tabela.column("descricao", width=450)
        self.tabela.column("nota", width=120, anchor="center")
        self.tabela.column("peso", width=120, anchor="center")

        self.tabela.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        # Resultado
        self.resultado = tk.Label(
            self.janela,
            text="Média: -- | Situação: --",
            font=("Arial", 14, "bold"),
            fg="#174A7E",
            pady=12
        )
        self.resultado.pack()

    def carregar_alunos(self):

        conexao = conectar()

        try:
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT matricula, nome
                FROM alunos
                ORDER BY nome
            """)

            registros = cursor.fetchall()

            opcoes = []

            for matricula, nome in registros:
                exibicao = f"{nome} - {matricula}"
                self.alunos[exibicao] = matricula
                opcoes.append(exibicao)

            self.combo_aluno["values"] = opcoes

        finally:
            conexao.close()

    def carregar_disciplinas(self):

        conexao = conectar()

        try:
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT codigo, nome
                FROM disciplinas
                ORDER BY nome
            """)

            registros = cursor.fetchall()

            opcoes = []

            for codigo, nome in registros:
                exibicao = f"{nome} - {codigo}"
                self.disciplinas[exibicao] = codigo
                opcoes.append(exibicao)

            self.combo_disciplina["values"] = opcoes

        finally:
            conexao.close()

    def selecionar_aluno(self, evento=None):
        self.carregar_avaliacoes()

    def selecionar_disciplina(self, evento=None):
        self.carregar_avaliacoes()

    def cadastrar_avaliacao(self):

        aluno = self.combo_aluno.get()
        disciplina = self.combo_disciplina.get()
        descricao = self.entrada_descricao.get().strip()
        nota_texto = self.entrada_nota.get().strip().replace(",", ".")
        peso_texto = self.entrada_peso.get().strip().replace(",", ".")

        if not aluno or not disciplina or not descricao:
            messagebox.showwarning(
                "Atenção",
                "Selecione o aluno, a disciplina e informe a avaliação.",
                parent=self.janela
            )
            return

        try:
            nota = float(nota_texto)
            peso = float(peso_texto)

            if nota < 0 or nota > 10 or peso <= 0:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Atenção",
                "Informe uma nota entre 0 e 10 e um peso maior que zero.",
                parent=self.janela
            )
            return

        resultado = self.dao.cadastrar(
            self.alunos[aluno],
            self.disciplinas[disciplina],
            descricao,
            nota,
            peso
        )

        if resultado:
            messagebox.showinfo(
                "Sucesso",
                "Avaliação cadastrada com sucesso!",
                parent=self.janela
            )

            self.limpar_campos()
            self.carregar_avaliacoes()

        else:
            messagebox.showerror(
                "Erro",
                "Não foi possível cadastrar a avaliação.",
                parent=self.janela
            )

    def carregar_avaliacoes(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        aluno = self.combo_aluno.get()
        disciplina = self.combo_disciplina.get()

        if not aluno or not disciplina:
            self.resultado.config(
                text="Média: -- | Situação: --"
            )
            return

        matricula = self.alunos[aluno]
        codigo = self.disciplinas[disciplina]

        avaliacoes = self.dao.listar_por_aluno_disciplina(
            matricula,
            codigo
        )

        boletim = Boletim(
            Aluno(matricula, self.combo_aluno.get().split(" - ")[0], ""),
            Disciplina(codigo, self.combo_disciplina.get().split(" - ")[0], 0)
        )

        for id_avaliacao, descricao, nota, peso in avaliacoes:

            self.tabela.insert(
                "",
                "end",
                values=(
                    id_avaliacao,
                    descricao,
                    nota,
                    peso
                )
            )

            boletim.adicionar_avaliacao(
                Avaliacao(descricao, nota, peso)
            )

        if avaliacoes:
            media = boletim.calcular_media()
            situacao = boletim.verificar_situacao()

            self.resultado.config(
                text=f"Média: {media:.2f} | Situação: {situacao}"
            )
        else:
            self.resultado.config(
                text="Média: -- | Situação: Sem avaliações"
            )

    def excluir_avaliacao(self):

        selecionado = self.tabela.selection()

        if not selecionado:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma avaliação na tabela.",
                parent=self.janela
            )
            return

        valores = self.tabela.item(
            selecionado[0],
            "values"
        )

        id_avaliacao = valores[0]

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            "Deseja excluir esta avaliação?",
            parent=self.janela
        )

        if confirmar:
            if self.dao.excluir(id_avaliacao):
                self.carregar_avaliacoes()

                messagebox.showinfo(
                    "Sucesso",
                    "Avaliação excluída com sucesso!",
                    parent=self.janela
                )

    def limpar_campos(self):

        self.entrada_descricao.delete(0, tk.END)
        self.entrada_nota.delete(0, tk.END)

        self.entrada_peso.delete(0, tk.END)
        self.entrada_peso.insert(0, "1")
