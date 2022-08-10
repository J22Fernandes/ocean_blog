from flask import Flask

app = Flask ("hello")

@app.route("/")
def hello():
    return ("Hello World")

@app.route("/contactos")
def contacto():
    return """<html>         
     <head>             
     <title> Contactos </title>       
        </head>         
         <body>           
           <h1>Danilo de Souza Miguel</h1>
            <h2>danilo@email.com</h2>
            <h3> 11985748-65243 </h3>
         </body>   
        </html>"""
