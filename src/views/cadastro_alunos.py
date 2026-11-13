
import tkinter as tk
from tkinter import ttk, messagebox

from src.database.aluno_dao import AlunoDAO


class CadastroAlunos:

    def __init__(self, janela_principal):

        self.janela = tk.Toplevel(janela_principal)
        self.janela.title("Cadastro de Alunos - NFM")
        self.janela.geometry("900x600")
        self.janela.minsize(800, 550)
        self.janela.configure(bg="#f2f4f8")

        # Conexão com o banco de dados
        self.dao = AlunoDAO()

        # Configuração dos estilos
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Treeview",
            font=("Arial", 10),
            rowheight=30
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
            padding=10
        )

        # Cabeçalho
        cabecalho = tk.Frame(
            self.janela,
            bg="#243b64",
            height=85
        )
        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)

        tk.Label(
            cabecalho,
            text="NFM | CADASTRO DE ALUNOS",
            font=("Arial", 21, "bold"),
            bg="#243b64",
            fg="white"
        ).pack(pady=23)

        # Área principal
        principal = tk.Frame(
            self.janela,
            bg="#f2f4f8"
        )
        principal.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        # Formulário
        formulario = tk.LabelFrame(
            principal,
            text="Dados do Aluno",
            font=("Arial", 11, "bold"),
            bg="#f2f4f8",
            fg="#243b64",
            padx=20,
            pady=15
        )
        formulario.pack(fill="x", pady=10)

        # Matrícula
        tk.Label(
            formulario,
            text="Matrícula:",
            font=("Arial", 11),
            bg="#f2f4f8"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.campo_matricula = ttk.Entry(
            formulario,
            width=45
        )
        self.campo_matricula.grid(
            row=0, column=1, padx=10, pady=10
        )

        # Nome
        tk.Label(
            formulario,
            text="Nome completo:",
            font=("Arial", 11),
            bg="#f2f4f8"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.campo_nome = ttk.Entry(
            formulario,
            width=45
        )
        self.campo_nome.grid(
            row=1, column=1, padx=10, pady=10
        )

        # Curso
        tk.Label(
            formulario,
            text="Curso:",
            font=("Arial", 11),
            bg="#f2f4f8"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.campo_curso = ttk.Entry(
            formulario,
            width=45
        )
        self.campo_curso.grid(
            row=2, column=1, padx=10, pady=10
        )

        # Botões
        botoes = tk.Frame(
            principal,
            bg="#f2f4f8"
        )
        botoes.pack(pady=15)

        ttk.Button(
            botoes,
            text="Cadastrar Aluno",
            style="Acao.TButton",
            command=self.cadastrar_aluno
        ).grid(row=0, column=0, padx=8)

        ttk.Button(
            botoes,
            text="Limpar Campos",
            style="Acao.TButton",
            command=self.limpar_campos
        ).grid(row=0, column=1, padx=8)

        ttk.Button(
            botoes,
            text="Excluir Selecionado",
            style="Acao.TButton",
            command=self.excluir_aluno
        ).grid(row=0, column=2, padx=8)

        # Tabela de alunos
        area_tabela = tk.LabelFrame(
            principal,
            text="Alunos Cadastrados",
            font=("Arial", 11, "bold"),
            bg="#f2f4f8",
            fg="#243b64",
            padx=10,
            pady=10
        )
        area_tabela.pack(
            fill="both",
            expand=True,
            pady=10
        )

        colunas = ("matricula", "nome", "curso")

        self.tabela = ttk.Treeview(
            area_tabela,
            columns=colunas,
            show="headings",
            height=8
        )

        self.tabela.heading("matricula", text="Matrícula")
        self.tabela.heading("nome", text="Nome do Aluno")
        self.tabela.heading("curso", text="Curso")

        self.tabela.column(
            "matricula",
            width=150,
            anchor="center"
        )

        self.tabela.column("nome", width=300)
        self.tabela.column("curso", width=300)

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

        # Carrega os alunos salvos no banco
        self.carregar_alunos()

        self.campo_matricula.focus()

    # Carregar alunos do banco de dados
    def carregar_alunos(self):

        self.tabela.delete(*self.tabela.get_children())

        try:
            alunos = self.dao.listar_todos()

            for aluno in alunos:
                self.tabela.insert(
                    "",
                    "end",
                    values=(
                        aluno[0],
                        aluno[1],
                        aluno[2]
                    )
                )

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar os alunos:\n{erro}",
                parent=self.janela
            )

    # Cadastrar aluno
    def cadastrar_aluno(self):

        matricula = self.campo_matricula.get().strip()
        nome = self.campo_nome.get().strip()
        curso = self.campo_curso.get().strip()

        if not matricula or not nome or not curso:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos.",
                parent=self.janela
            )
            return

        # Verifica matrícula duplicada no banco
        alunos = self.dao.listar_todos()

        if any(aluno[0] == matricula for aluno in alunos):
            messagebox.showwarning(
                "Atenção",
                "Esta matrícula já está cadastrada.",
                parent=self.janela
            )
            return

        try:
            resultado = self.dao.cadastrar(
                matricula,
                nome,
                curso
            )

            if resultado:
                self.carregar_alunos()
                self.limpar_campos()

                messagebox.showinfo(
                    "Sucesso",
                    "Aluno cadastrado com sucesso!",
                    parent=self.janela
                )

                self.campo_matricula.focus()

            else:
                messagebox.showerror(
                    "Erro",
                    "Não foi possível cadastrar o aluno.",
                    parent=self.janela
                )

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Falha ao cadastrar aluno:\n{erro}",
                parent=self.janela
            )

    # Limpar campos
    def limpar_campos(self):

        self.campo_matricula.delete(0, tk.END)
        self.campo_nome.delete(0, tk.END)
        self.campo_curso.delete(0, tk.END)

        self.campo_matricula.focus()

    # Excluir aluno
    def excluir_aluno(self):

        selecionado = self.tabela.selection()

        if not selecionado:
            messagebox.showwarning(
                "Atenção",
                "Selecione um aluno para excluir.",
                parent=self.janela
            )
            return

        item = selecionado[0]

        valores = self.tabela.item(item, "values")

        matricula = valores[0]

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Deseja excluir o aluno {valores[1]}?",
            parent=self.janela
        )

        if not confirmar:
            return

        try:
            resultado = self.dao.excluir(matricula)

            if resultado:
                self.carregar_alunos()

                messagebox.showinfo(
                    "Sucesso",
                    "Aluno excluído com sucesso!",
                    parent=self.janela
                )

            else:
                messagebox.showwarning(
                    "Atenção",
                    "Aluno não encontrado no banco de dados.",
                    parent=self.janela
                )

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível excluir o aluno:\n{erro}",
                parent=self.janela
            )
