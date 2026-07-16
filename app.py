from flask import Flask, render_template, request, redirect
import csv
import os
app = Flask(__name__)
LEADS_FILE = "leads.csv"
# Crea el archivo leads.csv con encabezados si no existe
if not os.path.exists(LEADS_FILE):
     with open(LEADS_FILE, "w", newline="", encoding="utf-8") as f:
         writer = csv.writer(f)
         writer.writerow("nombre", "correo", "interes")

@app.route("/")
def index():
    # Parámetro para el A/B testing (Paso 3). No lo modifiques.
    version = request.args.get("version", "a")
    return render_template("index.html", version=version)


@app.route("/enviar", 
methods=["POST"])
def enviar():


   # TODO Paso 2: recibe los campos del formulario
   # Pista: request.form.get("nombre")
   nombre = request.form.get("nombre")
   correo=  request.form.get("correo")
   interes= request.form.get("interes")
   # TODO Paso 2: guarda la fila en leads.csv
   with open(LEADS_FILE, "a", newline="", encoding="itf-8") as f:
       writer = csv.writer(f)
       writer.writerow(nombre, correo, interes )

   return redirect("/gracias")

@app.route("/gracias")
def gracias():
    return render_template("gracias.html")

if __name__ == "__main__":
    app.run(debug=True)