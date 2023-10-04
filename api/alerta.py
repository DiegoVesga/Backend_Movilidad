from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.alerta import alerta, alerta_schema,alertas_schema


ruta_alerta = Blueprint("ruta_alerta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_alerta.route("/alerta", methods=["GET"])
def getalerta():
    resultall = alerta.query.all()
    result = alerta_schema.dump(resultall)
    return jsonify(result)

@ruta_alerta.route("/savealerta", methods=["POST"])
def savealerta():
    try:
        id_alerta = request.json['id_alerta']
        tipo_alerta= request.json['tipo_alerta']
        fecha=request.json["fecha"]
        id_ciclo=request.json["id_ciclo"]
        new_alerta = alerta(id_alerta,tipo_alerta,fecha,id_ciclo)
        db.session.add(new_alerta)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"
        

@ruta_alerta.route("/updatealerta/<id>", methods=["PUT"])
def updatealerta(id):
 try:
    id_alerta = alerta.query.get(id)
    if not id_alerta:
        return "Id de alerta no exite/no se encuentra registada"
    tipo_alerta= request.json['tipo_alerta']
    fecha=request.json["fecha"]
    id_ciclo=request.json["id_ciclo"]
    id_alerta.tipo_alerta=tipo_alerta
    id_alerta.fecha=fecha
    id_alerta.id_ciclo=id_ciclo

    db.session.commit()
    return "Datos Actualizado con exitos"
 except Exception as e:
     return f"Hubo un error:  {str(e)}"


@ruta_alerta.route("/deletealerta/<id>", methods=["DELETE"])
def deletealerta(id):
  try:
    id_alerta = alerta.query.get(id)
    if not id_alerta:
        return "Id de alerta no exite/no se encuentra registada"
    db.session.delete(id_alerta)
    db.session.commit()
    return "alerta eliminada con exito"
  except Exception as e:
     return f"Hubo un error{str(e)}"
    