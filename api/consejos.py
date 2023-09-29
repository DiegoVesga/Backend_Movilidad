from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.consejos import consejos, consejo_Schema,consejoss_Schema


ruta_consejos = Blueprint("ruta_consejos",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_consejos.route("/consejos", methods=["GET"])
def consejos():
    resultall = consejos.query.all()
    result = consejoss_Schema.dump(resultall)
    return jsonify(result)

@ruta_consejos.route("/saveconsejos", methods=["POST"])
def saveconsejos():
    id_consejos = request.json['id_consejos']
    id_usuario = request.json['id_usuario']
    texto_consejo = request.json['texto_consejo']
    new_consejos= consejos(id_consejos,id_usuario,texto_consejo)
    db.session.add(new_consejos)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_consejos.route("/updateconsejos", methods=["PUT"])
def updateconsejos():
    id_consejos = request.json['id_consejos']
    id_usuario = request.json['id_usuario']
    texto_consejo = request.json['texto_consejo']
    nconsejos = consejos.query.get(id_consejos) #Select * from Cliente where id = id
    nconsejos.id_usuario=id_usuario
    nconsejos.texto_consejo=texto_consejo
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_consejos.route("/deleteconsejos/<id>", methods=["DELETE"])
def deleteconsejos(id):
    id_consejos = request.json['id_consejos']
    consejosx = consejos.query.get(id_consejos)
    db.session.delete(consejosx)
    db.session.commit()
    