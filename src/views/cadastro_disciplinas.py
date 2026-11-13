import tkinter as tk
from tkinter import ttk, messagebox

from src.database.disciplina_dao import DisciplinaDAO


class CadastroDisciplinas:

    def __init__(self, janela):
        # Abre uma janela secundária vinculada à tela principal
        self.janela = tk.Toplevel(janela)
        self.janela.transient(janela)

        self.dao = DisciplinaDAO()

        self.janela.title("Cadastro de Disciplinas")
        self.janela.geometry("800x550")
        self.janela.resizable(False, False)

        # Cabeçalho
        titulo = tk.Label(
            self.janela,
            text="Cadastro de Disciplinas",
            font=("Arial", 18, "bold"),
            bg="#174A7E",
            fg="white",
            pady=15
        )
        titulo.pack(fill="x")

        # Formulário
        formulario = tk.Frame(
            self.janela,
            padx=20,
            pady=20
        )
        formulario.pack(fill="x")

        tk.Label(
            formulario,
            text="Código:"
        ).grid(row=0, column=0, sticky="w", pady=5)

        self.entrada_codigo = tk.Entry(
            formulario,
            width=30
        )
        self.entrada_codigo.grid(
            row=0,
            column=1,
            padx=10,
            pady=5
        )

        tk.Label(
            formulario,
            text="Nome da disciplina:"
        ).grid(row=1, column=0, sticky="w", pady=5)

        self.entrada_nome = tk.Entry(
            formulario,
            width=40
        )
        self.entrada_nome.grid(
            row=1,
            column=1,
            padx=10,
            pady=5
        )

        tk.Label(
            formulario,
            text="Carga horária:"
        ).grid(row=2, column=0, sticky="w", pady=5)

        self.entrada_carga = tk.Entry(
            formulario,
            width=15
        )
        self.entrada_carga.grid(
            row=2,
            column=1,
            padx=10,
            pady=5,
            sticky="w"
        )

        # Botões
        botoes = tk.Frame(self.janela)
        botoes.pack(pady=10)

        tk.Button(
            botoes,
            text="Cadastrar",
            width=15,
            command=self.cadastrar_disciplina
        ).pack(side="left", padx=5)

        tk.Button(
            botoes,
            text="Limpar",
            width=15,
            command=self.limpar_campos
        ).pack(side="left", padx=5)

        tk.Button(
            botoes,
            text="Excluir selecionada",
            width=20,
            command=self.excluir_disciplina
        ).pack(side="left", padx=5)

        # Tabela de disciplinas
        colunas = ("codigo", "nome", "carga")

        self.tabela = ttk.Treeview(
            self.janela,
            columns=colunas,
            show="headings",
            height=12
        )

        self.tabela.heading(
            "codigo",
            text="Código"
        )

        self.tabela.heading(
            "nome",
            text="Disciplina"
        )

        self.tabela.heading(
            "carga",
            text="Carga Horária"
        )

        self.tabela.column(
            "codigo",
            width=120,
            anchor="center"
        )

        self.tabela.column(
            "nome",
            width=420
        )

        self.tabela.column(
            "carga",
            width=150,
            anchor="center"
        )

        self.tabela.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        # Carrega os registros existentes no banco
        self.carregar_disciplinas()

    def carregar_disciplinas(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        disciplinas = self.dao.listar_todos()

        for disciplina in disciplinas:
            self.tabela.insert(
                "",
                "end",
                values=disciplina
            )

    def cadastrar_disciplina(self):
        codigo = self.entrada_codigo.get().strip()
        nome = self.entrada_nome.get().strip()
        carga = self.entrada_carga.get().strip()

        if not codigo or not nome or not carga:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos.",
                parent=self.janela
            )
            return

        try:
            carga = int(carga)

            if carga <= 0:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Atenção",
                "Informe uma carga horária válida, em horas.",
                parent=self.janela
            )
            return

        resultado = self.dao.cadastrar(
            codigo,
            nome,
            carga
        )

        if resultado:
            messagebox.showinfo(
                "Sucesso",
                "Disciplina cadastrada com sucesso!",
                parent=self.janela
            )

            self.limpar_campos()
            self.carregar_disciplinas()

        else:
            messagebox.showerror(
                "Erro",
                "Não foi possível cadastrar. Verifique se o código já existe.",
                parent=self.janela
            )

    def excluir_disciplina(self):
        selecionado = self.tabela.selection()

        if not selecionado:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma disciplina na tabela.",
                parent=self.janela
            )
            return

        valores = self.tabela.item(
            selecionado[0],
            "values"
        )

        codigo = valores[0]

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Deseja excluir a disciplina {valores[1]}?",
            parent=self.janela
        )

        if confirmar:
            if self.dao.excluir(codigo):
                self.carregar_disciplinas()

                messagebox.showinfo(
                    "Sucesso",
                    "Disciplina excluída com sucesso!",
                    parent=self.janela
                )

    def limpar_campos(self):
        self.entrada_codigo.delete(0, tk.END)
        self.entrada_nome.delete(0, tk.END)
        self.entrada_carga.delete(0, tk.END)

        self.entrada_codigo.focus()
