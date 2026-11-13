# NFM – Sistema de Controle de Notas Escolares

Projeto acadêmico desenvolvido na disciplina de Programação Orientada a Objetos do curso de Ciência da Computação.

**Instituição fictícia:** NFM – Núcleo de Formação Moderna.

## 1. Objetivo

Desenvolver um sistema para auxiliar no gerenciamento acadêmico, permitindo cadastrar alunos e disciplinas, registrar avaliações e notas, calcular médias ponderadas e consultar a situação acadêmica dos alunos.

## 2. Tecnologias utilizadas

- Python 3
- Tkinter – desenvolvimento da interface gráfica.
- SQLite – armazenamento e persistência dos dados.
- Git e GitHub – controle de versão e organização do projeto.
- Unittest – execução dos testes automatizados.

## 3. Funcionalidades implementadas

1. Cadastro, consulta e exclusão de alunos.
2. Cadastro, consulta e exclusão de disciplinas.
3. Lançamento e exclusão de avaliações e notas.
4. Armazenamento dos dados em banco SQLite.
5. Consulta das avaliações por aluno e disciplina.
6. Cálculo da média ponderada conforme as notas e os pesos cadastrados.
7. Identificação da situação acadêmica: aprovado ou reprovado.
8. Validação dos campos obrigatórios nas operações do sistema.
9. Verificação da seleção de aluno e disciplina antes da consulta do boletim.
10. Prevenção de cadastros duplicados.

## 4. Regras acadêmicas

- As notas são registradas em uma escala de 0 a 10.
- As avaliações possuem pesos que influenciam o cálculo da média.
- A média mínima de aprovação utilizada atualmente é 7,0.
- A situação acadêmica é apresentada conforme a média calculada.

**Observação:** as regras poderão ser ajustadas conforme as orientações do professor.

## 5. Estrutura do projeto

```text
Sistema_Controle_Notas_Escolares/
│
├── docs/
├── src/
│   ├── controllers/
│   ├── database/
│   ├── models/
│   └── views/
│
├── tests/
├── main.py
├── notas_escolares.db
├── README.md
└── .gitignore
```

## 6. Como executar

1. Instale o Python 3.
2. Abra a pasta do projeto no VS Code.
3. Ative o ambiente virtual pelo terminal do PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Execute o sistema:

```bash
python main.py
```

## 7. Como executar os testes

Para executar todos os testes automatizados, utilize:

```bash
python -m unittest discover -s tests -v
```

Os testes verificam as classes do sistema e as operações de persistência no banco de dados.

## 8. Considerações finais

O projeto busca aplicar na prática os conceitos de Programação Orientada a Objetos, organização de código, persistência de dados e desenvolvimento de interfaces gráficas.

O sistema está em desenvolvimento contínuo, com melhorias e novas funcionalidades previstas para as próximas etapas do projeto.