#flask --app app run --debug
import requests
from flask import Flask, render_template
app = Flask (__name__)

peticion = requests.get("https://6608363ca2a5dd477b14291c.mockapi.io/allProduct")

@app.get("/")
def index():
    return render_template('index.html', data=peticion.json())

@app.route("/views/abrigos")
def abrigos(): 
    return render_template('abrigos.html', data=peticion.json())

@app.route("/views/camisetas")
def camisetas():
    return render_template('camisetas.html', data=peticion.json())

@app.route("/views/pantalones")
def pantalones():
    return render_template('pantalones.html', data=peticion.json())

@app.route("/views/carritos")
def carritos():
    return render_template('carritos.html')

@app.route("/views/abrir")
def abrir():
    return render_template('abrir.html')

@app.route("/views/vaciarcarrito")
def vaciarcarrito():
    return render_template('vaciarcarrito.html')

app.run(debug=True)

