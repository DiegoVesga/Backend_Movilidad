from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.alerta import alerta, alerta_schema,alertas_schema


ruta_alerta = Blueprint("ruta_alerta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_alerta.route("/alerta", methods=["GET"])
def alerta():
    resultall = alerta.query.all()
    result = alerta_schema.dump(resultall)
    return jsonify(result)

@ruta_alerta.route("/savealerta", methods=["POST"])
def savealerta():
    id_alerta = request.json['id_alerta']
    tipo_alerta= request.json['tipo_alerta']
    fecha=request.json["fecha"]
    id_ciclo=request.json["id_ciclo"]
    new_alerta = alerta(id_alerta,tipo_alerta,fecha,id_ciclo)
    db.session.add(new_alerta)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_alerta.route("/updatealerta", methods=["PUT"])
def updatealerta():
    id_alerta = request.json['id_alerta']
    tipo_alerta= request.json['tipo_alerta']
    fecha=request.json["fecha"]
    id_ciclo=request.json["id_ciclo"]
    nalerta = alerta.query.get(id_alerta) #Select * from Cliente where id = id
    nalerta.tipo_alerta=tipo_alerta
    nalerta.fecha=fecha
    nalerta.id_ciclo=id_ciclo

    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_alerta.route("/deletealerta/<id>", methods=["DELETE"])
def deletealerta(id):
    id_alerta= request.json['id_alerta']
    alertax = alerta.query.get(id_alerta) 
    db.session.delete(alertax)
    db.session.commit()
    