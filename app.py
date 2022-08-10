from flask import Flask, render_template

app = Flask ("hello")

@app.route("/")
def hello():
    return ("Hello World")

@app.route("/contactos")
def contacto():
    nomeAula ="Aula python para Web"
    return render_template ("index.html", nome=nomeAula)