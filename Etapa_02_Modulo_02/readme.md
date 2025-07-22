# 🧠 EduPlanner - Fase 2 >> Módulo 1: Algoritmos de Busca

## 📋 Visão Geral da Arquitetura

A Fase 2 do EduPlanner implementa um sistema de busca acadêmica utilizando três algoritmos fundamentais de busca e pesquisa em texto. O sistema é organizado em uma arquitetura modular com separação clara de responsabilidades.

### 🏗️ Estrutura do Projeto

```
Etapa_02_Modulo_01/
├── dados/
│   ├── materias.json      # Catálogo de disciplinas
│   ├── professores.json   # Base de dados dos professores
│   └── turmas.json        # Turmas ofertadas com horários
├── src/
│   ├── main.py           # Interface principal do sistema
│   ├── algoritmos.py     # Implementação dos algoritmos de busca
│   ├── carregador_dados.py # Módulo de carregamento de dados
│   └── entidades.py      # Classes do domínio (Professor, Materia, Turma)
└── README.md
```

### 🎯 Componentes Principais

1. **Entidades de Domínio** (`entidades.py`)
   - Classes `Professor`, `Materia` e `Turma`
   - Encapsulamento das propriedades acadêmicas
   - Relacionamentos entre entidades

2. **Carregador de Dados** (`carregador_dados.py`)
   - Parsing de arquivos JSON
   - Construção de catálogos usando dicionários nativos do Python
   - Vinculação automática entre matérias e turmas

3. **Módulo de Algoritmos** (`algoritmos.py`)
   - Implementação dos três algoritmos de busca
   - Funções utilitárias para processamento de texto

4. **Interface Principal** (`main.py`)
   - Menu interativo para o usuário
   - Orquestração das buscas
   - Formatação dos resultados

## 🔍 Algoritmos Implementados

### 1. Busca Binária por Código de Matéria

**Implementação:**
```python
def busca_binaria_por_codigo(codigo, lista_codigos_ordenada, catalogo_materias):
    esquerda, direita = 0, len(lista_codigos_ordenada) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        codigo_meio = lista_codigos_ordenada[meio]
        
        if codigo_meio == codigo:
            return catalogo_materias[codigo]
        elif codigo_meio < codigo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return None
```

**Integração:**
- Utiliza uma lista ordenada de códigos de matérias (`sorted(catalogo_materias.keys())`)
- Acesso direto ao catálogo via dicionário após encontrar o código
- Pré-processamento único na inicialização do sistema

**Complexidade:**
- **Tempo:** O(log n) - onde n é o número de matérias
- **Espaço:** O(1) - busca in-place
- **Pré-processamento:** O(n log n) para ordenação inicial

### 2. Busca Sequencial por Professor

**Implementação:**
```python
def busca_sequencial_por_professor(nome_prof, catalogo_professores, catalogo_materias):
    nome_prof_lower = nome_prof.lower()
    resultados_materias = []
    ids_profs_encontrados = []
    
    # Fase 1: Encontrar professores
    for prof in catalogo_professores.values():
        if nome_prof_lower in prof.nome_completo.lower():
            ids_profs_encontrados.append(prof.id_professor)
    
    # Fase 2: Encontrar matérias dos professores
    for materia in catalogo_materias.values():
        for turma in materia.turmas_ofertadas:
            if turma.id_professor in ids_profs_encontrados:
                if materia not in resultados_materias:
                    resultados_materias.append(materia)
    
    return resultados_materias
```

**Integração:**
- Busca flexível com substring matching (case-insensitive)
- Navegação pelos relacionamentos Professor → Turma → Matéria
- Eliminação automática de duplicatas

**Complexidade:**
- **Tempo:** O(p + m × t) - onde p = professores, m = matérias, t = turmas médias por matéria
- **Espaço:** O(k) - onde k é o número de resultados encontrados
- **Pior caso:** O(n) para varrer todas as entidades

### 3. Busca por Palavra-chave (Algoritmo Rabin-Karp)

**Implementação:**
```python
def busca_rabin_karp(texto, padrao):
    if len(padrao) > len(texto):
        return False
    
    base = 256
    primo = 101
    m, n = len(padrao), len(texto)
    
    # Cálculo dos hashes iniciais
    hash_padrao = hash_texto = 0
    h = pow(base, m-1) % primo
    
    for i in range(m):
        hash_padrao = (base * hash_padrao + ord(padrao[i])) % primo
        hash_texto = (base * hash_texto + ord(texto[i])) % primo
    
    # Rolling hash e comparação
    for i in range(n - m + 1):
        if hash_padrao == hash_texto:
            if texto[i:i+m] == padrao:
                return True
        
        if i < n - m:
            hash_texto = (base * (hash_texto - ord(texto[i]) * h) + ord(texto[i+m])) % primo
            hash_texto = hash_texto % primo
    
    return False

def busca_por_palavra_chave_na_ementa(palavra_chave, catalogo_materias):
    resultados = []
    palavra_chave = palavra_chave.lower()
    
    for materia in catalogo_materias.values():
        ementa = materia.ementa.lower()
        if busca_rabin_karp(ementa, palavra_chave):
            resultados.append(materia)
    
    return resultados
```

**Integração:**
- Processamento case-insensitive para maior usabilidade
- Aplicação em todas as ementas do catálogo
- Rolling hash para eficiência em textos longos

**Complexidade:**
- **Tempo Médio:** O(n + m) - onde n = tamanho do texto, m = tamanho do padrão
- **Tempo Pior Caso:** O(n × m) - quando há muitas colisões de hash
- **Espaço:** O(1) - algoritmo in-place
- **Busca Completa:** O(t × (n + m)) - onde t = total de matérias

## 📊 Análise de Eficiência

### Desempenho Observado nos Testes

1. **Busca Binária:**
   - ✅ **Excelente** para catálogos grandes (>1000 matérias)
   - ✅ Tempo de resposta consistente

2. **Busca Sequencial:**
   - ✅ **Boa** flexibilidade (busca por substring)
   - ✅ Não requer pré-processamento

3. **Rabin-Karp:**
   - ✅ **Eficiente** para ementas de tamanho médio (100-500 caracteres)
   - ✅ Rolling hash otimiza buscas repetitivas

### Comparativo de Complexidade

| Algoritmo | Tempo (Melhor) | Tempo (Médio) | Tempo (Pior) | Espaço | Pré-proc. |
|-----------|---------------|---------------|--------------|--------|-----------|
| Busca Binária | O(1) | O(log n) | O(log n) | O(1) | O(n log n) |
| Busca Sequencial | O(1) | O(n) | O(n) | O(k) | O(1) |
| Rabin-Karp | O(m) | O(n+m) | O(n×m) | O(1) | O(1) |

*Onde: n = tamanho da entrada, m = tamanho do padrão, k = resultados*

---

*EduPlanner 🧠*