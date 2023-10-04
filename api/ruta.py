from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.ruta import ruta, ruta_schema, rutas_schema


ruta_ruta = Blueprint("ruta_ruta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_ruta.route("/ruta", methods=["GET"])
def getruta():
    resultall = ruta.query.all()
    result = ruta_schema.dump(resultall)
    return jsonify(result)

@ruta_ruta.route("/saveruta", methods=["POST"])
def saveruta():
    try:
        id_ruta = request.json['id_ruta']
        punto_inicio= request.json['punto_inicio']
        punto_final= request.json['punto_final']
        new_ruta= ruta(id_ruta,punto_inicio,punto_final)
        db.session.add(new_ruta)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un problema{str(e)}"

@ruta_ruta.route("/updateruta/<id>", methods=["PUT"])
def updateruta(id):
    try:
        id_ruta = ruta.query.get(id)
        if not id_ruta:
            return "El usuario no esta registrado"
        punto_inicio= request.json['punto_inicio']
        punto_final= request.json['punto_final']
        id_ruta.punto_inicio=punto_inicio
        id_ruta.punto_final=punto_final  
        db.session.commit()
        return "Datos Actualizado con exitos"
    except Exception as e:
        return f"Hubo un error{str(e)}"

@ruta_ruta.route("/deleteruta/<id>", methods=["DELETE"])
def deleteruta(id):
    try:
        id_ruta = ruta.query.get(id)
        if not id_ruta:
            return "El usuario no esta registrado"
        db.session.delete(id_ruta)
        db.session.commit()
    except Exception as e:
        return f"Hubo un error {str(e)}"
    