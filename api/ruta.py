from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.ruta import ruta, ruta_schema, rutas_schema


ruta_ruta = Blueprint("ruta_alerta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_ruta.route("/ruta", methods=["GET"])
def ruta():
    resultall = ruta.query.all()
    result = ruta_schema.dump(resultall)
    return jsonify(result)

@ruta_ruta.route("/ruta", methods=["POST"])
def saveruta():
    id_ruta = request.json['id_ruta']
    punto_inicio= request.json['punto_inicio']
    punto_final= request.json['punto_final']
    new_ruta= ruta(id_ruta,punto_inicio,punto_final)
    db.session.add(new_ruta)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_ruta.route("/updateruta", methods=["PUT"])
def updateruta():
    id_ruta = request.json['id_ruta']
    punto_inicio= request.json['punto_inicio']
    punto_final= request.json['punto_final']
    nruta = ruta.query.get(id_ruta) #Select * from Cliente where id = id
    nruta.punto_inicio=punto_inicio
    nruta.punto_final=punto_final  
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_ruta.route("/deleteruta/<id>", methods=["DELETE"])
def deleteruta(id):
    id_ruta = request.json['id_ruta']
    rutax = ruta.query.get(id_ruta)
    db.session.delete(rutax)
    db.session.commit()
    