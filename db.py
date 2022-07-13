from tinydb import TinyDB, Query

db = TinyDB("Database.json")
Database = Query()

def createTransacao(receitaOrDespesa):
    db.insert(receitaOrDespesa)

def totalReceitas():
    receitas = db.search(Database.tipo == 'receita')

    total = 0
    for row in receitas:
        total += row['valor']
    return total

def totalDespesas():
    despesas = db.search(Database.tipo == 'despesa')

    total = 0
    for row in despesas:
        total += row['valor']
    return total

def saldo():
    receitas = totalReceitas()
    despesas = totalDespesas()
    return receitas - despesas

def extrato():
    return db.all()
    
def excluirTransacao(id):
    db.remove(Database.id == id)

def editarTransacao(dados, id):
    db.update(dados, Database.id == id)
    

