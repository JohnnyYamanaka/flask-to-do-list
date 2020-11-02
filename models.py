from app import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    desc_curta = db.Column(db.String(30), unique=True, nullable=False)
    desc_longa = db.Column(db.String(99))
    status = db.Column(db.Boolean)
    prioridade = db.Column(db.String(10), nullable=False)
    data_inicio = db.Column(db.DateTime)
    data_conclusao = db.Column(db.DateTime)


    def __init__(self, desc_curta, desc_longa, status, prioridade,
    data_inicio, data_conclusao, id=None):
        self.id = id
        self.desc_curta = desc_curta
        self.desc_longa = desc_longa
        self.status = status
        self.prioridade = prioridade
        self.data_inicio = data_inicio
        self.data_conclusao = data_conclusao

        def __repr__(self):
            return '<desc_curta %r>' % self.desc_curta
