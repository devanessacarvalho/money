from db import createReceita, createDespesa, totalReceitas, totalDespesas, saldo

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template(
    'index.html',
    saldo = saldo(), 
    receita=totalReceitas(), 
    despesa = totalDespesas()
  )

@app.route('/cadastrar/<tipo>', methods=['GET', 'POST'])
def cadastrar(tipo):
  if request.method == 'GET':
    return render_template('cadastrar.html', tipo=tipo)
  
  dados = {
    'descricao':request.form['descricao'],
    'valor':float(request.form['valor']),
    'data':request.form['data'],
    'tipo':tipo
  }

  createReceita(dados) if tipo == 'receita' else createDespesa(dados)
 
  return redirect('/')

app.run(debug=True)
