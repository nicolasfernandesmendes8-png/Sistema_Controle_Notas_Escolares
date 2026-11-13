
import tkinter as tk

from src.database.conexao import criar_banco
from src.views.tela_principal import TelaPrincipal


def main():
    # Cria o banco e as tabelas, caso ainda não existam
    criar_banco()

    # Inicializa a interface principal
    janela = tk.Tk()
    app = TelaPrincipal(janela)

    # Mantém a janela aberta
    janela.mainloop()


if __name__ == "__main__":
    main()
