# 🧠 EduPlanner – Sistema Inteligente de Planejamento Acadêmico

## 📌 Etapa 1: Introdução e Concepção

### 🎯 Tema do Projeto e Justificativa

**Tema:**  
EduPlanner é um sistema que auxilia estudantes universitários na organização de suas matrículas semestrais, considerando requisitos como carga horária, pré-requisitos, horários e preferências pessoais.

**Justificativa:**  
Planejar um semestre acadêmico pode ser um grande desafio. O EduPlanner surge para resolver conflitos de horários, validar pré-requisitos e sugerir combinações otimizadas de disciplinas. Ao aplicar algoritmos de grafos, busca e otimização, este software visa facilitar o processo de tomada de decisão acadêmica de forma personalizada e eficiente.

---

### 🧩 Visão Geral das Funcionalidades

- 📚 Cadastro e consulta de disciplinas com informações completas.
- 🕑 Montagem automática de plano de matrícula com base em restrições.
- 🔍 Busca por nome, código, professor ou área de conhecimento.
- 🌐 Visualização em grafo das dependências entre disciplinas.
- 📊 Análise de carga horária semanal e alertas de sobrecarga.
- 🧠 Sugestão inteligente de disciplinas recomendadas.
- 💾 Compactação e exportação de plano e histórico do aluno.

---

### 🔗 Integração com a Ementa da Disciplina

| Tópico da Ementa                              | Implementação no EduPlanner                                                                                      |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Teoria da Complexidade (NP-Difíceis)**      | Montagem ideal de grade com restrições de pré-requisitos e horários é NP-difícil. Solução via heurística.       |
| **Busca Sequencial / Binária**                | Pesquisa de disciplinas por nome, código ou área.                                                               |
| **Busca em Texto**                            | Localização de disciplinas por palavras-chave na descrição ou nome do professor.                                |
| **Hashing**                                   | Acesso rápido aos dados do aluno, disciplinas e histórico via tabela hash.                                      |
| **Compressão de Dados (RLE / Huffman)**       | Compactação dos planos de matrícula e históricos salvos.                                                        |
| **Grafos (Pré-requisitos, Dependências)**     | Representação da grade como grafo direcionado. Pré-requisitos modelados como arestas.                          |
| **DFS / Ordenação Topológica**                | Validação dos pré-requisitos antes da inserção de uma disciplina no plano.                                     |
| **Algoritmos Gulosos**                        | Seleção rápida de disciplinas que maximizam aproveitamento dentro dos limites do usuário.                       |
| **Programação Dinâmica (Mochila 0/1)**        | Seleção ótima de disciplinas para preencher a carga horária semanal ou créditos disponíveis.                    |

---

### 💻 Tecnologias Escolhidas

- **Linguagem de Programação:**  
  - Python  

- **Frameworks / Bibliotecas:**  
    - A decidir

---
