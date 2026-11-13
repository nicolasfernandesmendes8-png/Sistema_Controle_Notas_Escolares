
import tkinter as tk
from tkinter import ttk, messagebox

from src.views.cadastro_alunos import CadastroAlunos
from src.views.cadastro_disciplinas import CadastroDisciplinas
from src.views.lancamento_notas import LancamentoNotas
from src.views.consulta_boletim import ConsultaBoletim


class TelaPrincipal:

    def __init__(self, janela):
        self.janela = janela

        self.janela.title(
            "Sistema de Controle de Notas Escolares - NFM"
        )
        self.janela.geometry("950x600")
        self.janela.minsize(800, 500)
        self.janela.configure(bg="#f2f4f8")

        # Controle das janelas
        self.tela_alunos = None
        self.tela_disciplinas = None
        self.tela_notas = None
        self.tela_boletim = None

        # Configuração dos botões
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Menu.TButton",
            font=("Arial", 11, "bold"),
            padding=12,
            background="#243b64",
            foreground="white"
        )

        estilo.map(
            "Menu.TButton",
            background=[("active", "#34568a")]
        )

        # Cabeçalho
        cabecalho = tk.Frame(
            janela,
            bg="#243b64",
            height=90
        )
        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)

        tk.Label(
            cabecalho,
            text="NFM | CONTROLE ACADÊMICO",
            font=("Arial", 20, "bold"),
            bg="#243b64",
            fg="white"
        ).pack(side="left", padx=30, pady=25)

        # Área principal
        conteudo = tk.Frame(
            janela,
            bg="#f2f4f8"
        )
        conteudo.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=35
        )

        tk.Label(
            conteudo,
            text="Sistema de Controle de Notas Escolares",
            font=("Arial", 22, "bold"),
            bg="#f2f4f8",
            fg="#243b64"
        ).pack(pady=(15, 8))

        tk.Label(
            conteudo,
            text="Gerenciamento de alunos, disciplinas e avaliações",
            font=("Arial", 12),
            bg="#f2f4f8",
            fg="#555555"
        ).pack(pady=(0, 30))

        # Menu de funcionalidades
        menu = tk.Frame(
            conteudo,
            bg="#f2f4f8"
        )
        menu.pack()

        ttk.Button(
            menu,
            text="Cadastro de Alunos",
            style="Menu.TButton",
            command=self.abrir_cadastro_alunos
        ).pack(fill="x", pady=7)

        ttk.Button(
            menu,
            text="Cadastro de Disciplinas",
            style="Menu.TButton",
            command=self.abrir_cadastro_disciplinas
        ).pack(fill="x", pady=7)

        ttk.Button(
            menu,
            text="Lançamento de Notas",
            style="Menu.TButton",
            command=self.abrir_lancamento_notas
        ).pack(fill="x", pady=7)

        ttk.Button(
            menu,
            text="Consultar Boletim",
            style="Menu.TButton",
            command=self.abrir_consulta_boletim
        ).pack(fill="x", pady=7)

        # Rodapé
        rodape = tk.Label(
            janela,
            text=(
                "Projeto Acadêmico - Ciência da Computação | "
                "NFM - Núcleo de Formação Moderna | 2026"
            ),
            font=("Arial", 9),
            bg="#e1e6ef",
            fg="#555555",
            pady=12
        )
        rodape.pack(fill="x", side="bottom")

    # Abrir cadastro de alunos
    def abrir_cadastro_alunos(self):
        if (
            self.tela_alunos is None
            or not self.tela_alunos.janela.winfo_exists()
        ):
            self.tela_alunos = CadastroAlunos(self.janela)
        else:
            self.tela_alunos.janela.lift()

    # Abrir cadastro de disciplinas
    def abrir_cadastro_disciplinas(self):
        if (
            self.tela_disciplinas is None
            or not self.tela_disciplinas.janela.winfo_exists()
        ):
            self.tela_disciplinas = CadastroDisciplinas(
                self.janela
            )
        else:
            self.tela_disciplinas.janela.lift()

    # Abrir lançamento de notas
    def abrir_lancamento_notas(self):
        if (
            self.tela_notas is None
            or not self.tela_notas.janela.winfo_exists()
        ):
            self.tela_notas = LancamentoNotas(self.janela)
        else:
            self.tela_notas.janela.lift()

    # Abrir consulta de boletim
    def abrir_consulta_boletim(self):
        if (
            self.tela_boletim is None
            or not self.tela_boletim.janela.winfo_exists()
        ):
            self.tela_boletim = ConsultaBoletim(self.janela)
        else:
            self.tela_boletim.janela.lift()

    # Mensagem para funcionalidades ainda não implementadas
    def em_desenvolvimento(self, funcionalidade):
        messagebox.showinfo(
            "Em desenvolvimento",
            f"A funcionalidade {funcionalidade} será implementada "
            "nas próximas etapas."
        )


if __name__ == "__main__":
    janela = tk.Tk()
    app = TelaPrincipal(janela)
    janela.mainloop()
