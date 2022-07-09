from db import getALL, createTransaction
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
  result = getALL()
  saldo = 600
  receita = 1000
  despesa = 300

  return render_template('index.html', saldo = saldo, receita=receita, despesa = despesa)


@app.route('/cadastrar/<tipo>', methods=['GET', 'POST'])
def cadastrar(tipo):
  if request.method == 'GET':
    return render_template('cadastrar.html')
  
  dados = {
    'descricao':request.form['descricao'],
    'valor':request.form['valor'],
    'data':request.form['data'],
    'tipo':tipo
  }

  createTransaction(dados)
  return redirect('/')

app.run(debug=True)
