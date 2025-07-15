import heapq

# Algoritmos de Busca

def busca_sequencial_por_professor(nome_prof, catalogo_professores, catalogo_materias):

    nome_prof_lower = nome_prof.lower()
    resultados_materias = []
    ids_profs_encontrados = []
    
    for prof in catalogo_professores.values():
        if nome_prof_lower in prof.nome_completo.lower():
            ids_profs_encontrados.append(prof.id_professor)
            
    if not ids_profs_encontrados:
        return []

    for materia in catalogo_materias.values():
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
            return catalogo_materias.get(lista_codigos_ordenada[meio])
    return None

def busca_rabin_karp(texto, padrao):

    base_ascii = 256
    primo = 97
    tam_padrao = len(padrao)
    tam_texto = len(texto)

    if tam_padrao > tam_texto:
        return False

    fator_base = 1
    hash_padrao = 0
    hash_janela = 0

    for i in range(tam_padrao - 1):
        fator_base = (fator_base * base_ascii) % primo

    for i in range(tam_padrao):
        hash_padrao = (base_ascii * hash_padrao + ord(padrao[i])) % primo
        hash_janela = (base_ascii * hash_janela + ord(texto[i])) % primo

    for i in range(tam_texto - tam_padrao + 1):
        if hash_padrao == hash_janela:
            if texto[i:i+tam_padrao] == padrao:
                return True

        if i < tam_texto - tam_padrao:
            hash_janela = (
                base_ascii * (hash_janela - ord(texto[i]) * fator_base) + ord(texto[i + tam_padrao])
            ) % primo

            if hash_janela < 0:
                hash_janela += primo

    return False

def busca_por_palavra_chave_na_ementa(palavra_chave, catalogo_materias):

    resultados = []
    palavra_chave = palavra_chave.lower()

    for materia in catalogo_materias.values():
        ementa = materia.ementa.lower()
        if busca_rabin_karp(ementa, palavra_chave):
            resultados.append(materia)

    return resultados