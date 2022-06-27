from db import getALL, createTransaction
from flask import Flask, render_template, redirect
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def index():
    result = getALL()

    return render_template("index.html", result = result)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    description = request.form["description"]
    value = request.form["value"]
    type = request.form["type"]
    date = request.form["date"]

    transaction = {
      'description':description,
      'value':value,
      'type':type,
      'date':date
    }

    createTransaction(transaction)
    return redirect("/")

app.run(debug=True)
