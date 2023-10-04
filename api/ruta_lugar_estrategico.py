from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.ruta_lugar_estrategico import ruta_lugar_estrategico, ruta_lugar_estrategico_Schema, ruta_lugar_estrategicos_Schema


ruta_ruta_lugar_estrategico = Blueprint("ruta_ruta_lugar_estrategico",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_ruta_lugar_estrategico.route("/ruta_lugar_estrategico", methods=["GET"])
def getruta_lugar_estrategico():
    resultall = ruta_lugar_estrategico.query.all()
    result = ruta_lugar_estrategico_Schema.dump(resultall)
    return jsonify(result)

@ruta_ruta_lugar_estrategico.route("/saveruta_lugar_estrategico", methods=["POST"])
def saveruta_lugar_estrategico():
    try:
        id_lugar_ruta = request,json['id_lugar_ruta']
        id_lugar = request.json['id_lugar']
        id_ruta = request.json['id_ruta']
        new_ruta_lugar_estrategico = ruta_lugar_estrategico(id_lugar_ruta,id_lugar,id_ruta)
        db.session.add(new_ruta_lugar_estrategico)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_ruta_lugar_estrategico.route("/updateruta_lugar_estrategico/<id>", methods=["PUT"])
def updateruta_lugar_estrategico(id):
    try:
        id_lugar_ruta= ruta_lugar_estrategico.query.get(id)
        if not id_lugar_ruta:
            return "NO existe el Lugar_Ruta"
        id_lugar = request.json['id_lugar']
        id_ruta = request.json['id_ruta']
        id_lugar_ruta.id_lugar=id_lugar
        id_lugar_ruta.id_ruta=id_ruta
        db.session.commit()
        return "Datos Actualizado con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_ruta_lugar_estrategico.route("/deleteruta_lugar_estrategico/<id>", methods=["DELETE"])
def deleteruta_lugar_estrategico(id):
    try:
        id_lugar_ruta= ruta_lugar_estrategico.query.get(id)
        if not id_lugar_ruta:
            return "NO existe el Lugar_Ruta"
        db.session.delete(id_lugar_ruta)
        db.session.commit()
    except Exception as e:
        return f"Hubo un error {str(e)}"