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
 try:
    id_inicio = request.json['id_inicio']
    id_fin = request.json['id_fin']
    new_ciclovia = ciclovia(id_inicio,id_fin)
    db.session.add(new_ciclovia)
    db.session.commit()
    return "Datos guardados con exitos"
 except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_ciclovia.route("/updateciclovia/<id>", methods=["PUT"])
def updatecliente(id):
 try:
    id_ciclo = ciclovia.query.get(id)
    if not id_ciclo:
            return "ciclovia no esta registrado"
    dir_inicio = request.json['dir_inicio']
    dir_fin = request.json['dir_fin']
    id_ciclo.dir_inicio=dir_inicio
    id_ciclo.dir_fin=dir_fin
    db.session.commit()
    return "Datos Actualizado con exitos"
 except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_ciclovia.route("/deleteciclovia/<id>", methods=["DELETE"])
def deleteciclovia(id):
  try:
    id_ciclo = ciclovia.query.get(id)
    if not id_ciclo:
            return "ciclovia no esta registrado"
    db.session.delete(id_ciclo)
    db.session.commit()
    return "se ha eliminado la ciclovia"
  except Exception as e:
        return f"Hubo un error{str(e)}"
    