from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.ciclovia import ciclovia, ciclovia_schema,ciclovias_schema


ruta_ciclovia = Blueprint("ruta_ciclovia",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_ciclovia.route("/ciclovia", methods=["GET"])
def getciclovia():
    resultall = ciclovia.query.all()
    result = ciclovia_schema.dump(resultall)
    return jsonify(result)

@ruta_ciclovia.route("/saveciclovia", methods=["POST"])
def saveciclovia():
    id_inicio = request.json['id_inicio']
    id_fin = request.json['id_fin']
    new_ciclovia = ciclovia(id_inicio,id_fin)
    db.session.add(new_ciclovia)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_ciclovia.route("/updateciclovia", methods=["PUT"])
def updatecliente():
    id_ciclo = request.json['id_ciclo']
    dir_inicio = request.json['dir_inicio']
    dir_fin = request.json['dir_fin']
    nciclovia = ciclovia.query.get(id_ciclo) #Select * from Cliente where id = id
    nciclovia.dir_inicio=dir_inicio
    nciclovia.dir_fin=dir_fin
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_ciclovia.route("/deleteciclovia/<id>", methods=["DELETE"])
def deleteciclovia(id):
    id_ciclo = request.json['id_ciclo']
    cicloviax = ciclovia.query.get(id_ciclo)
    db.session.delete(cicloviax)
    db.session.commit()
    