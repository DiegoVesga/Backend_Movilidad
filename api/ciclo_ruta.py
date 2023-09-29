from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.ciclo_ruta import ciclo_ruta, ciclo_ruta_schema,ciclo_rutas_schema


ruta_ciclo_ruta = Blueprint("ruta_ciclo_ruta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_ciclo_ruta.route("/ciclo_ruta", methods=["GET"])
def ciclo_ruta():
    resultall = ciclo_ruta.query.all()
    result = ciclo_ruta_schema.dump(resultall)
    return jsonify(result)

@ruta_ciclo_ruta.route("/saveciclo_ruta", methods=["POST"])
def saveciclo_ruta():
    id_ciclo_ruta = request.json['id_ciclo_ruta']
    id_ciclo = request.json['id_ciclo']
    id_ruta = request.json['id_ruta']
    new_ciclo_ruta = ciclo_ruta(id_ciclo_ruta,id_ciclo,id_ruta )
    db.session.add(new_ciclo_ruta)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_ciclo_ruta.route("/updateciclo_ruta", methods=["PUT"])
def updateciclo_ruta():
    id_ciclo_ruta = request.json['id_ciclo_ruta']
    id_ciclo = request.json['id_ciclo']
    id_ruta = request.json['id_ruta']
    nciclo_ruta = ciclo_ruta.query.get(id_ciclo_ruta,id_ciclo, id_ruta) #Select * from Cliente where id = id
    nciclo_ruta.id_ciclo_ruta= id_ciclo_ruta
    nciclo_ruta.id_ciclo=id_ciclo
    nciclo_ruta.id_ruta=id_ruta
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_ciclo_ruta.route("/deleteciclo_ruta/<id>", methods=["DELETE"])
def deleteciclo_ruta(id):
    id_ciclo_ruta = request.json['id_ciclo_ruta']
    ciclo_rutax = ciclo_ruta.query.get(id_ciclo_ruta)
    db.session.delete(ciclo_rutax)
    db.session.commit()
    
    