from tinydb import TinyDB, Query

db = TinyDB("Database.json")
Database = Query()

table_receitas = db.table('receitas')
table_despesas = db.table('despesas')

def createReceita(receita):
    table_receitas.insert(receita)

def createDespesa(despesa):
    table_despesas.insert(despesa)

def totalReceitas():
    total = 0
    for row in table_receitas:
        total+=row['valor']
    return total

def totalDespesas():
    total = 0
    for row in table_despesas:
        total+=row['valor']
    return total

def saldo():
    receitas = totalReceitas()
    despesas = totalDespesas()
    return receitas - despesas

def excluirReceita(id):
    table_receitas.remove(Database.id == id)

def excluirDespesa(id):
    table_despesas.remove(Database.id == id)

def excluirTransacao(tipo, id):
    excluirReceita(id) if tipo == 'receita' else excluirDespesa(id)

    

