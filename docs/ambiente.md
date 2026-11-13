# Configuração do Ambiente de Desenvolvimento — VS Code

## 1. Ferramentas necessárias

1. Instale o Python 3 no Windows.
2. Instale o Visual Studio Code.
3. No VS Code, instale a extensão **Python**, da Microsoft.

## 2. Abrir o projeto

1. Abra o VS Code.
2. Acesse **Arquivo > Abrir Pasta**.
3. Selecione a pasta `Sistema_Controle_Notas_Escolares`.

## 3. Verificar a instalação do Python

No terminal integrado do VS Code, execute:

```powershell
py --version
```

Ou:

```powershell
python --version
```

## 4. Criar o ambiente virtual

Na pasta principal do projeto, execute:

```powershell
py -m venv .venv
```

## 5. Ativar o ambiente virtual

No terminal PowerShell, execute:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 6. Selecionar o interpretador Python

1. Pressione `Ctrl + Shift + P`.
2. Procure por **Python: Select Interpreter**.
3. Selecione o interpretador localizado na pasta `.venv`.

## 7. Executar o sistema

Com o ambiente virtual ativado, execute:

```powershell
python main.py
```

## 8. Executar os testes automatizados

Para verificar o funcionamento das classes e operações do banco de dados, execute:

```powershell
python -m unittest discover -s tests -v
```

**Observação:** o projeto utiliza bibliotecas nativas do Python, como Tkinter e SQLite, não exigindo instalação adicional dessas ferramentas.