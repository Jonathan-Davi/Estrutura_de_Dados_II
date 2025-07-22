import heapq

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

def rabin_karp_search(texto, padrao):
    D, Q, M, N = 256, 97, len(padrao), len(texto)
    if M > N: return False
    h, hash_padrao, hash_texto = 1, 0, 0
    for i in range(M - 1): h = (h * D) % Q
    for i in range(M):
        hash_padrao = (D * hash_padrao + ord(padrao[i])) % Q
        hash_texto = (D * hash_texto + ord(texto[i])) % Q
    for i in range(N - M + 1):
        if hash_padrao == hash_texto:
            if texto[i:i+M] == padrao: return True
        if i < N - M:
            hash_texto = (D * (hash_texto - ord(texto[i]) * h) + ord(texto[i + M])) % Q
            if hash_texto < 0: hash_texto += Q
    return False

def busca_por_palavra_chave_na_ementa(palavra_chave, catalogo_materias):
    resultados = []
    palavra_lower = palavra_chave.lower()
    for materia in catalogo_materias.todos_os_valores():
        ementa_lower = materia.ementa.lower()
        if rabin_karp_search(ementa_lower, palavra_lower):
            resultados.append(materia)
    return resultados

## HUFFMAN

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def criar_arvore_huffman(texto):

    frequencia = {char: texto.count(char) for char in set(texto)}
    
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencia.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(priority_queue, merged)
        
    return priority_queue[0] if priority_queue else None

def gerar_codigos_huffman(node, current_code, codes):
    if node is None: return
    if node.char is not None:
        codes[node.char] = current_code
        return
    gerar_codigos_huffman(node.left, current_code + "0", codes)
    gerar_codigos_huffman(node.right, current_code + "1", codes)

def comprimir_huffman(texto):

    if not texto: return "", None
    
    root = criar_arvore_huffman(texto)
    codes = {}
    gerar_codigos_huffman(root, "", codes)
    
    texto_comprimido = "".join([codes[char] for char in texto])
    return texto_comprimido, root

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