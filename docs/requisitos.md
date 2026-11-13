# Levantamento de Requisitos – Sistema de Controle de Notas Escolares

## 1. Objetivo

Desenvolver uma aplicação desktop para organizar alunos, disciplinas, avaliações e notas, permitindo acompanhar o desempenho acadêmico por meio do cálculo de médias e da consulta de boletins.

## 2. Ator

**Usuário:** responsável por cadastrar, consultar e gerenciar os dados acadêmicos no sistema.

## 3. Requisitos funcionais

- **RF01:** cadastrar, consultar e excluir alunos.
- **RF02:** cadastrar, consultar e excluir disciplinas.
- **RF03:** registrar, consultar e excluir avaliações e notas.
- **RF04:** calcular a média ponderada por aluno e disciplina.
- **RF05:** apresentar a situação acadêmica do aluno, conforme a média calculada.
- **RF06:** consultar o boletim mediante seleção de aluno e disciplina.
- **RF07:** validar os campos obrigatórios antes de executar as operações.

## 4. Requisitos não funcionais

- **RNF01:** possuir interface gráfica simples e intuitiva.
- **RNF02:** armazenar os dados de forma persistente em banco SQLite.
- **RNF03:** validar as informações inseridas pelo usuário.
- **RNF04:** manter o código organizado em módulos e classes.
- **RNF05:** apresentar mensagens claras de sucesso, erro e validação.

## 5. Regras de negócio

- As notas são registradas em uma escala de 0 a 10.
- Cada avaliação possui um peso utilizado no cálculo da média.
- A média é calculada de forma ponderada.
- A média mínima de aprovação utilizada atualmente é 7,0.
- A consulta do boletim exige a seleção de um aluno e uma disciplina.
- A existência de recuperação ou exame final ainda depende de orientação do professor.

**Observação:** as regras acadêmicas poderão ser ajustadas conforme as orientações oficiais da disciplina.

## 6. Situação do projeto

Os requisitos apresentados refletem as funcionalidades implementadas até esta etapa do desenvolvimento. Novas funcionalidades e ajustes poderão ser incorporados conforme a evolução do projeto e as orientações do professor.