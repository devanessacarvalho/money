from tinydb import TinyDB, Query

bd = TinyDB("Transactions.json")
transactions = Query()

def createTransaction(transaction):
    bd.insert(transaction)

def getALL():
    return bd.all()


    

