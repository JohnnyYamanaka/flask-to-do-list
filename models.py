

class Task:
    def __init__(self, desc_curta, desc_longa, status, prioridade,
    data_inicio, data_conclusao, id=None):
        self.id = id
        self.desc_curta = desc_curta
        self.desc_longa = desc_longa
        self.status = status
        self.prioridade = prioridade
        self.data_inicio = data_inicio
        self.data_conclusao = data_conclusao
