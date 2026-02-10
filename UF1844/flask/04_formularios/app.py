from flask import Flask, redirect, url_for,render_template,request
from datetime import datetime
import json
import os

app = Flask(__name__)

DATOS = "datos.json"

PAISES = ['Argentina','México','España']
GENEROS = ['Hombre','Mujer','No definido']
HOBBIES = ['Leer','Deporte','Música','Video juegos', 'Viajar']

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('home.html',paises=PAISES,generos=GENEROS,hobbies=HOBBIES)