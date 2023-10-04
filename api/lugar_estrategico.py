from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.lugar_estrategico import lugar_estrategico, lugar_estrategico_Schema,lugares_estrategicos_Schema


ruta_lugar_estrategico = Blueprint("ruta_lugar_estrategico",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_lugar_estrategico.route("/lugar_estrategico", methods=["GET"])
def getlugar_estrategico():
    resultall = lugar_estrategico.query.all()
    result = lugar_estrategico_Schema.dump(resultall)
    return jsonify(result)

@ruta_lugar_estrategico.route("/savelugar_estrategico", methods=["POST"])
def savelugar_estrategico():
    id_lugar = request.json['id_lugar']
    nombre=request.json['nombre']
    new_lugar_estrategico= lugar_estrategico(id_lugar,nombre)
    db.session.add(new_lugar_estrategico)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_lugar_estrategico.route("/updatelugar_estrategico", methods=["PUT"])
def updatelugar_estrategico():
    id_lugar = request.json['id_lugar']
    nombre=request.json['nombre']
    nlugar = lugar_estrategico.query.get(id_lugar) #Select * from Cliente where id = id
    nlugar.nombre=nombre 
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_lugar_estrategico.route("/deletelugar_estrategico/<id>", methods=["DELETE"])
def deletelugar_estrategico(id):
    id_lugar = request.json['id_lugar']
    lugarx = lugar_estrategico.query.get(id_lugar)
    db.session.delete(lugarx)
    db.session.commit()
    