# 🧠 EduPlanner - Sistema de Planejamento Acadêmico

## 📋 Visão Geral da Arquitetura

O EduPlanner é um sistema modular de planejamento acadêmico que implementa diversos algoritmos de estruturas de dados para permitir a busca, organização e compactação de informações sobre matérias, professores e turmas. A arquitetura foi desenvolvida com foco na separação de responsabilidades e na eficiência algorítmica.

### 🏗️ Estrutura do Projeto

```
EduPlanner/
├── dados/
│   ├── materias.json      # Catálogo de disciplinas
│   ├── professores.json   # Base de dados dos professores
│   └── turmas.json        # Turmas ofertadas com horários
├── src/
│   ├── main.py            # Interface principal do sistema
│   ├── algoritmos.py      # Implementação dos algoritmos de busca e compressão
│   ├── carregador_dados.py # Módulo de carregamento de dados
│   ├── entidades.py       # Classes do domínio (Professor, Materia, Turma)
│   └── tabela_hash.py     # Implementação da tabela hash personalizada
└── README.md
```

### 🎯 Componentes Principais

1. **Entidades de Domínio** (`entidades.py`)
   - Classes `Professor`, `Materia` e `Turma`
   - Encapsulamento das propriedades acadêmicas
   - Relacionamentos entre entidades

2. **Carregador de Dados** (`carregador_dados.py`)
   - Parsing de arquivos JSON
   - Construção de catálogos usando tabelas hash
   - Vinculação automática entre matérias e turmas

3. **Tabela Hash** (`tabela_hash.py`)
   - Implementação personalizada com múltiplas funções de hash
   - Resolução de colisão por encadeamento
   - Métodos para análise de desempenho

4. **Módulo de Algoritmos** (`algoritmos.py`)
   - Implementação dos algoritmos de busca
   - Compressão e descompressão com Huffman
   - Funções utilitárias para processamento de texto

5. **Interface Principal** (`main.py`)
   - Menu interativo para o usuário
   - Orquestração das buscas e demonstrações
   - Formatação dos resultados

## 🔍 Algoritmos de Busca Implementados

### 1. Busca Binária por Código de Matéria

**Implementação:**
```python
def busca_binaria_por_codigo(codigo, lista_codigos_ordenada, catalogo_materias):
    baixo, alto = 0, len(lista_codigos_ordenada) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista_codigos_ordenada[meio] < codigo:
            baixo = meio + 1
        elif lista_codigos_ordenada[meio] > codigo:
            alto = meio - 1
        else:
            return catalogo_materias.buscar(lista_codigos_ordenada[meio])
    return None
```

**Integração:**
- Utiliza uma lista ordenada de códigos de matérias (`sorted(catalogo_materias.todas_as_chaves())`)
- Acesso via tabela hash após encontrar o código na lista ordenada
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
    
    for prof in catalogo_professores.todos_os_valores():
        if nome_prof_lower in prof.nome_completo.lower():
            ids_profs_encontrados.append(prof.id_professor)
            
    if not ids_profs_encontrados:
        return []

    for materia in catalogo_materias.todos_os_valores():
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

### 3. Busca por Palavra-chave com Rabin-Karp

**Implementação:**
```python
def rabin_karp_search(texto, padrao):
    D, Q, M, N = 256, 97, len(padrao), len(texto)
    if M > N: return False
    h, hash_padrao, hash_texto = 1, 0, 0
    
    # Calcular o valor de h = D^(M-1) mod Q
    for i in range(M - 1): h = (h * D) % Q
    
    # Calcular os hashes iniciais
    for i in range(M):
        hash_padrao = (D * hash_padrao + ord(padrao[i])) % Q
        hash_texto = (D * hash_texto + ord(texto[i])) % Q
    
    # Deslizar a janela e verificar coincidências
    for i in range(N - M + 1):
        if hash_padrao == hash_texto:
            if texto[i:i+M] == padrao: return True
        
        # Atualizar o hash da janela para a próxima posição
        if i < N - M:
            hash_texto = (D * (hash_texto - ord(texto[i]) * h) + ord(texto[i + M])) % Q
            if hash_texto < 0: hash_texto += Q
    
    return False
```

**Integração:**
- Processamento case-insensitive para maior usabilidade
- Aplicação em todas as ementas do catálogo
- Rolling hash para eficiência em textos longos

**Complexidade:**
- **Tempo Médio:** O(n + m) - onde n = tamanho do texto, m = tamanho do padrão
- **Tempo Pior Caso:** O(n × m) - quando há muitas colisões de hash
- **Espaço:** O(1) - algoritmo in-place

## 🧮 Tabela Hash Personalizada

O sistema implementa uma tabela hash customizada com duas funções de hash distintas:

### 1. Função de Hash por Enlaçamento Deslocado

```python
def _hash_por_enlacamento_deslocado(self, chave, tamanho_pedaco=2):
    chave_str = str(chave)
    hash_valor = 0
    for i in range(0, len(chave_str), tamanho_pedaco):
        pedaco = chave_str[i:i+tamanho_pedaco]
        soma_pedaco = 0
        for char in pedaco:
            soma_pedaco += ord(char)
        hash_valor += soma_pedaco
    return hash_valor
```

- **Funcionamento**: Divide a chave em pedaços de tamanho fixo e soma os valores ASCII
- **Característica**: Boa distribuição para chaves alfanuméricas
- **Complexidade**: O(n), onde n é o tamanho da chave

### 2. Função de Hash por Extração

```python
def _hash_por_extracao(self, chave):
    numeros = re.findall(r'\d', str(chave))
    if not numeros: return 0
    valor_extraido = int("".join(numeros))
    return valor_extraido
```

- **Funcionamento**: Extrai apenas os dígitos numéricos da chave
- **Característica**: Eficaz para chaves como códigos de matéria (ex: "BSI0101")
- **Complexidade**: O(n), onde n é o tamanho da chave

### Resolução de Colisões

A tabela hash utiliza o método de encadeamento (chaining) para resolver colisões:

```python
def inserir(self, chave, valor):
    indice = self._funcao_hash(chave)
    bucket = self.tabela[indice]
    for i, par in enumerate(bucket):
        if par[0] == chave:
            bucket[i] = (chave, valor)
            return
    bucket.append((chave, valor))
```

- **Vantagem**: Simplicidade de implementação
- **Desvantagem**: Performance degrada com muitas colisões
- **Complexidade**:
  - **Busca (Média)**: O(1 + α), onde α é o fator de carga
  - **Busca (Pior)**: O(n) quando todas as chaves colidem

## 🗜️ Compressão de Dados com Huffman

### Estrutura de Dados

```python
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
```

### Processo de Compressão

1. **Construção da Árvore Huffman**

```python
def criar_arvore_huffman(texto):
    # Calcular frequência de cada caractere
    frequencia = {char: texto.count(char) for char in set(texto)}
    
    # Criar fila de prioridade com nós iniciais
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencia.items()]
    heapq.heapify(priority_queue)
    
    # Construir árvore combinando nós de menor frequência
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(priority_queue, merged)
        
    return priority_queue[0] if priority_queue else None
```

2. **Geração de Códigos**

```python
def gerar_codigos_huffman(node, current_code, codes):
    if node is None: return
    if node.char is not None:
        codes[node.char] = current_code
        return
    gerar_codigos_huffman(node.left, current_code + "0", codes)
    gerar_codigos_huffman(node.right, current_code + "1", codes)
```

3. **Compressão**

```python
def comprimir_huffman(texto):
    if not texto: return "", None
    
    root = criar_arvore_huffman(texto)
    codes = {}
    gerar_codigos_huffman(root, "", codes)
    
    texto_comprimido = "".join([codes[char] for char in texto])
    return texto_comprimido, root
```

### Processo de Descompressão

```python
def descomprimir_huffman(texto_comprimido, arvore_huffman):
    if not texto_comprimido or not arvore_huffman:
        return ""

    texto_descomprimido = ""
    node_atual = arvore_huffman
    for bit in texto_comprimido:
        if bit == '0':
            node_atual = node_atual.left
        else:
            node_atual = node_atual.right
        
        if node_atual.char is not None:
            texto_descomprimido += node_atual.char
            node_atual = arvore_huffman 

    return texto_descomprimido
```

### Análise de Complexidade

- **Construção da árvore**: O(n log n), onde n é o número de caracteres únicos
- **Geração de códigos**: O(n), onde n é o número de caracteres únicos
- **Compressão**: O(m), onde m é o tamanho do texto original
- **Descompressão**: O(m'), onde m' é o tamanho do texto comprimido

### Eficiência de Compressão

A eficiência depende da distribuição de frequência dos caracteres:
- Textos com padrões repetitivos: Alta taxa de compressão
- Textos uniformes/aleatórios: Baixa taxa de compressão
- Taxa média observada: 30-50% de redução para textos típicos

## 📊 Análise Comparativa dos Algoritmos

### 1. Algoritmos de Busca

| Algoritmo | Caso Médio | Pior Caso | Espaço | Características |
|-----------|------------|-----------|--------|-----------------|
| Busca Binária | O(log n) | O(log n) | O(1) | Requer ordenação prévia |
| Busca Sequencial | O(n) | O(n) | O(1) | Flexível, suporta substring |
| Rabin-Karp | O(n+m) | O(n×m) | O(1) | Eficiente para padrões pequenos |

### 2. Funções de Hash

| Função | Distribuição | Colisões | Adequada para |
|--------|-------------|----------|---------------|
| Enlaçamento Deslocado | Média-Alta | Baixa | Chaves alfanuméricas |
| Extração | Média | Média-Alta | Chaves com padrão numérico fixo |

### 3. Comparação das Implementações de Tabela Hash

| Característica | Tabela Hash Nativa | Tabela Hash Personalizada |
|----------------|-------------------|--------------------------|
| Velocidade de Acesso | O(1) médio | O(1) médio |
| Flexibilidade | Limitada | Alta (múltiplas funções de hash) |
| Resolução de Colisões | Interna | Encadeamento visível |
| Análise de Performance | Não disponível | Disponível |

### 4. Compressão Huffman

| Métrica | Valor |
|---------|-------|
| Taxa de Compressão | 30-50% em média |
| Tempo de Compressão | O(n log n) |
| Fidelidade | Sem perdas |
| Aplicações | Planos de matrícula, históricos |

---

*EduPlanner 🧠*