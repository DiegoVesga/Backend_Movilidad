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
    try:
        id_lugar = request.json['id_lugar']
        nombre=request.json['nombre']
        new_lugar_estrategico= lugar_estrategico(id_lugar,nombre)
        db.session.add(new_lugar_estrategico)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_lugar_estrategico.route("/updatelugar_estrategico/<id>", methods=["PUT"])
def updatelugar_estrategico(id):
    try:
        id_lugar=lugar_estrategico.query.get(id)
        if not id_lugar:
            return "El lugar estrategico no se encuentra"
        nombre=request.json['nombre']
        id_lugar.nombre=nombre 
        db.session.commit()
        return "Datos Actualizado con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_lugar_estrategico.route("/deletelugar_estrategico/<id>", methods=["DELETE"])
def deletelugar_estrategico(id):
    try:
        id_lugar=lugar_estrategico.query.get(id)
        if not id_lugar:
            return "El lugar estrategico no se encuentra"
        db.session.delete(id_lugar)
        db.session.commit()
    except Exception as e:
        return f"Hubo un error {str(e)}"
    