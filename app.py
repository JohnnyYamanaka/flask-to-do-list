from flask import Flask, render_template, url_for, redirect, request
import datetime
from models import Task

app = Flask(__name__)

lista_task = []

@app.route('/')
def index():
    return render_template('index.html', lista_task=lista_task)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Nova Tarefa')


@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    desc_curta = request.form['desc_curta']
    desc_longa = request.form['desc_longa']
    status = "Não iniciado"
    prioridade = request.form['prioridade']
    data_conclusao = None
    date = datetime.datetime.now()
    data_inicio = date.strftime("%d/%m/%Y")
    task = Task(desc_curta, desc_longa, status, prioridade,
    data_inicio, data_conclusao)
    lista_task.append(task)
    return redirect(url_for('index'))


@app.route('/concluidos')
def concluidos():
    return render_template('concluidos.html', titulo="Conluídos",
     lista_task=lista_task)


@app.route('/concluir', methods=['POST',])
def concluir():
    task.status = 'Concluido'
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
