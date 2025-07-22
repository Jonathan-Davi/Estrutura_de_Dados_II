class Professor:
    def __init__(self, id_prof, nome, depto):
        self.id_professor = id_prof
        self.nome_completo = nome
        self.departamento = depto

    def __repr__(self):
        return f"Professor(ID: {self.id_professor}, Nome: {self.nome_completo})"

class Turma:
    def __init__(self, id_turma, id_prof, horarios_lista):
        self.id_turma = id_turma
        self.id_professor = id_prof
        self.horarios = horarios_lista
    
    def __repr__(self):
        return f"Turma {self.id_turma} (Prof ID: {self.id_professor}, Horários: {self.horarios})"

class Materia:
    def __init__(self, codigo, nome, ementa, creditos, pre_requisitos_lista):
        self.codigo = codigo
        self.nome = nome
        self.ementa = ementa
        self.creditos = creditos
        self.pre_requisitos = pre_requisitos_lista
        self.turmas_ofertadas = []

    def adicionar_turma(self, turma):
        self.turmas_ofertadas.append(turma)

    def __repr__(self):
        return f"\n--- Matéria ---\nCódigo: {self.codigo}\nNome: {self.nome}\nCréditos: {self.creditos}\nPré-requisitos: {self.pre_requisitos}\nTurmas: {self.turmas_ofertadas}"