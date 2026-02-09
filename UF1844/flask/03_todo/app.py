from flask import Flask, redirect, url_for,render_template,request
from datetime import datetime
import json
import os

app = Flask(__name__)

MIS_TAREAS = "tareas.json"

def carga_tareas():
    if not os.path.exists(MIS_TAREAS):
        return []
    with open(MIS_TAREAS,'r',encoding='utf-8') as f:
        return json.load(f)
    
def guardar_tareas(tareas):
    with open(MIS_TAREAS, 'w',encoding='utf-8') as f:
        json.dump(tareas,f, indent=4,ensure_ascii=False)

@app.route('/', methods=["POST","GET"])
def index():
    tasks = carga_tareas()
    if request.method == "POST":
        desc = request.form["descripcion"]
        nueva = {
            "id" : len(tasks) + 1,
            "descripcion": desc,
            "fecha_alta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fecha_completada": None
        }
        tasks.append(nueva)
        guardar_tareas(tasks)
        return redirect(url_for("index"))

    return  render_template("index.html", tareas=tasks)


