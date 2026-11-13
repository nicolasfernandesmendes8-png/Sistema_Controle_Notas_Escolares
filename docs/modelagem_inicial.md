# Modelagem do Sistema de Controle de Notas Escolares

## 1. Classes principais

- **Aluno:** representa o aluno, contendo matrícula, nome e curso.
- **Disciplina:** representa a disciplina, com código, nome e carga horária.
- **Avaliacao:** armazena a descrição da avaliação, a nota e o peso.
- **Boletim:** relaciona um aluno a uma disciplina, reúne suas avaliações, calcula a média ponderada e identifica a situação acadêmica.

## 2. Classes de acesso ao banco de dados (DAO)

- **AlunoDAO:** realiza cadastro, consulta e exclusão de alunos.
- **DisciplinaDAO:** realiza cadastro, consulta e exclusão de disciplinas.
- **AvaliacaoDAO:** realiza cadastro, consulta e exclusão de avaliações.

As classes DAO utilizam a função `conectar()`, definida no módulo `conexao.py`, para acessar o banco de dados SQLite.

## 3. Relacionamentos

- Um aluno pode possuir boletins referentes a diferentes disciplinas.
- Uma disciplina pode estar presente nos boletins de vários alunos.
- Cada boletim está associado a um aluno e a uma disciplina.
- O boletim reúne as avaliações correspondentes à combinação de aluno e disciplina.
- Cada avaliação está vinculada a um aluno e a uma disciplina no banco de dados.
- As classes DAO fazem a comunicação entre o sistema e o banco de dados SQLite.

## 4. Regras de negócio

- As notas são registradas em uma escala de 0 a 10.
- Cada avaliação possui um peso.
- A média é calculada de forma ponderada.
- A média mínima de aprovação utilizada atualmente é 7,0.
- Para consultar o boletim, é necessário selecionar um aluno e uma disciplina.
- A situação acadêmica é apresentada conforme a média calculada.

## 5. Organização da arquitetura

O sistema está organizado em três áreas principais:

- **Models:** representam as entidades e regras de negócio.
- **Database:** concentra a conexão com o SQLite e as operações de persistência por meio das classes DAO.
- **Views:** apresentam as telas e permitem a interação do usuário com o sistema.

## 6. Observações

Esta modelagem representa a estrutura implementada até o momento e poderá receber ajustes conforme a evolução do projeto e as orientações do professor.