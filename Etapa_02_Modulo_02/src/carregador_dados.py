import json
from entidades import Professor, Materia, Turma

def carregar_dados():

    catalogo_professores = {}
    catalogo_materias = {}

    path_professores = 'Etapa_02_Modulo_01/dados/professores.json'
    path_materias = 'Etapa_02_Modulo_01/dados/materias.json'
    path_turmas = 'Etapa_02_Modulo_01/dados/turmas.json'

    with open(path_professores, mode='r', encoding='utf-8') as infile:
        dados_professores = json.load(infile)
        for row in dados_professores:
            prof = Professor(row['id_professor'], row['nome_completo'], row['departamento'])
            catalogo_professores[prof.id_professor] = prof

    with open(path_materias, mode='r', encoding='utf-8') as infile:
        dados_materias = json.load(infile)
        for row in dados_materias:
            mat = Materia(row['codigo'], row['nome'], row['ementa'], int(row['creditos']), row['pre_requisitos'])
            catalogo_materias[mat.codigo] = mat

    with open(path_turmas, mode='r', encoding='utf-8') as infile:
        dados_turmas = json.load(infile)
        for row in dados_turmas:
            turma = Turma(row['id_turma'], row['id_professor'], row['horarios'])
            codigo_materia = row['codigo_materia']
            
            materia_correspondente = catalogo_materias.get(codigo_materia)
            if materia_correspondente:
                materia_correspondente.adicionar_turma(turma)

    return catalogo_materias, catalogo_professores