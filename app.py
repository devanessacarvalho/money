from uuid import uuid4
from flask import Flask, render_template, redirect, request

from db import createTransacao
from db import totalReceitas, totalDespesas, saldo, extrato, obterTransacao
from db import excluirTransacao
from db import editarTransacao

app = Flask(__name__)

@app.route('/')
def index():
  return render_template(
    'index.html',
    saldo = saldo(), 
    receita=totalReceitas(), 
    despesa = totalDespesas(),
    extrato = extrato(),
  )

@app.route('/cadastrar/<tipo>', methods=['GET', 'POST'])
def cadastrar(tipo):
  if request.method == 'GET':
    return render_template('cadastrar.html', tipo=tipo)
    
  dados = {
    'id': str(uuid4()),
    'descricao':request.form['descricao'],
    'valor':float(request.form['valor']),
    'data':request.form['data'],
    'tipo': tipo,
  }

  createTransacao(dados)
 
  return redirect('/')

@app.route('/deletar/<id>')
def deletar(id):
  excluirTransacao(id)
  
  return redirect("/")

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
  if request.method == 'GET':
    transacao = obterTransacao(id)
    return render_template('editar.html', transacao=transacao)

  newDados = {
    'descricao':request.form['descricao'],
    'valor':float(request.form['valor']),
    'data':request.form['data'],
  }

  editarTransacao(newDados, id)
 
  return redirect('/')

app.run(debug=True)
