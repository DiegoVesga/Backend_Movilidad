from flask import Flask, redirect, jsonify, render_template, request
from config.db import app
from api.ciclovia import  ruta_ciclovia
from api.usuario import ruta_usuario
from api.ruta import ruta_ruta
from api.alerta import ruta_alerta
from api.lugar_estrategico import ruta_lugar_estrategico
from api.consejos import ruta_consejos
from api.ciclo_ruta import ruta_ciclo_ruta
from api.ruta_lugar_estrategico import ruta_ruta_lugar_estrategico
from api.usuario_ruta import ruta_usuario_ruta
app.register_blueprint(ruta_ciclovia, url_prefix="/api")
app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_ruta, url_prefix="/api")
app.register_blueprint(ruta_alerta, url_prefix="/api")
app.register_blueprint(ruta_lugar_estrategico, url_prefix="/api")
app.register_blueprint(ruta_consejos, url_prefix="/api")
app.register_blueprint(ruta_ciclo_ruta, url_prefix="/api")
app.register_blueprint(ruta_ruta_lugar_estrategico, url_prefix="/api")
app.register_blueprint(ruta_usuario_ruta, url_prefix="/api")

@app.route("/")
def index():
    return render_template("Home2.html")

@app.route("/login")
def login():
    return render_template("Loginin.html")

@app.route("/sign")
def sign():
    return render_template("Signup.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')