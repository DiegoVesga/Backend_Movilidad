from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.ruta_lugar_estrategico import ruta_lugar_estrategico, ruta_lugar_estrategico_Schema, ruta_lugar_estrategicos_Schema


ruta_ruta_lugar_estrategico = Blueprint("ruta_ruta_lugar_estrategico",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_ruta_lugar_estrategico.route("/ruta_lugar_estrategico", methods=["GET"])
def ruta_lugar_estrategico():
    resultall = ruta_lugar_estrategico.query.all()
    result = ruta_lugar_estrategico_Schema.dump(resultall)
    return jsonify(result)

@ruta_ruta_lugar_estrategico.route("/saveruta_lugar_estrategico", methods=["POST"])
def saveruta_lugar_estrategico():
    id_lugar_ruta = request,json['id_lugar_ruta']
    id_lugar = request.json['id_lugar']
    id_ruta = request.json['id_ruta']
    new_ruta_lugar_estrategico = ruta_lugar_estrategico(id_lugar_ruta,id_lugar,id_ruta)
    db.session.add(new_ruta_lugar_estrategico)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_ruta_lugar_estrategico.route("/updateruta_lugar_estrategico", methods=["PUT"])
def updateruta_lugar_estrategico():
    id_lugar_ruta = request.json['id_lugar_ruta']
    id_lugar = request.json['id_lugar']
    id_ruta = request.json['id_ruta']
    nruta_lugar_estrategico = ruta_lugar_estrategico.query.get(id_lugar_ruta,id_lugar, id_ruta) #Select * from Cliente where id = id
    nruta_lugar_estrategico. id_lugar_ruta = id_lugar_ruta 
    nruta_lugar_estrategico.id_lugar=id_lugar
    nruta_lugar_estrategico.id_ruta=id_ruta
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_ruta_lugar_estrategico.route("/deleteruta_lugar_estrategico/<id>", methods=["DELETE"])
def deleteruta_lugar_estrategico(id):
    id_lugar_ruta = request.json['id_lugar_ruta']
    ruta_lugar_estrategicox = ruta_lugar_estrategico.query.get(id_lugar_ruta)
    db.session.delete(ruta_lugar_estrategicox)
    db.session.commit()