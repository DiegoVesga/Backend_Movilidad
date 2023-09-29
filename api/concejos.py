from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.concejos import concejos, concejo_Schema,concejoss_Schema


ruta_concejos = Blueprint("ruta_concejos",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_concejos.route("/concejos", methods=["GET"])
def concejos():
    resultall = concejos.query.all()
    result = concejoss_Schema.dump(resultall)
    return jsonify(result)

@ruta_concejos.route("/saveconcejos", methods=["POST"])
def saveconcejos():
    id_concejos = request.json['id_concejos']
    id_usuario = request.json['id_usuario']
    texto_concejo = request.json['texto_concejo']
    new_concejos= concejos(id_concejos,id_usuario,texto_concejo)
    db.session.add(new_concejos)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_concejos.route("/updateconcejos", methods=["PUT"])
def updateconcejos():
    id_concejos = request.json['id_concejos']
    id_usuario = request.json['id_usuario']
    texto_concejo = request.json['texto_concejo']
    nconcejos = concejos.query.get(id_concejos) #Select * from Cliente where id = id
    nconcejos.id_usuario=id_usuario
    nconcejos.texto_concejo=texto_concejo
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_concejos.route("/deleteconcejos/<id>", methods=["DELETE"])
def deleteconcejos(id):
    id_concejos = request.json['id_concejos']
    concejosx = concejos.query.get(id_concejos)
    db.session.delete(concejosx)
    db.session.commit()
    