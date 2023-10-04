from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.usuario_ruta import usuario_ruta, usuario_ruta_schema,usuario_rutas_schema


ruta_usuario_ruta = Blueprint("ruta_usuario_ruta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_usuario_ruta.route("/usuario_ruta", methods=["GET"])
def getusuario_ruta():
    resultall = usuario_ruta.query.all()
    result = usuario_ruta_schema.dump(resultall)
    return jsonify(result)

@ruta_usuario_ruta.route("/saveusuario_ruta/<id>", methods=["POST"])
def saveusuario_ruta(id):
    try:   
        id_usuario_ruta = request.json['id_usuario_ruta']
        id_usuario = request.json['id_usuario']
        id_ruta = request.json['id_ruta']
        favorito = request.json['favorito']
        new_usuario_ruta = usuario_ruta(id_usuario_ruta,id_usuario,id_ruta,favorito)
        db.session.add(new_usuario_ruta)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un error{str(e)}"

@ruta_usuario_ruta.route("/updateusuario_ruta", methods=["PUT"])
def updatecusuario_ruta():
    id_usuario_ruta = request.json['id_usuario_ruta']
    id_usuario = request.json['id_usuario']
    id_ruta = request.json['id_ruta']
    favorito = request.json['favorito']
    nusuario_ruta = usuario_ruta.query.get(id_usuario_ruta) #Select * from Cliente where id = id
    nusuario_ruta.id_usuario=id_usuario
    nusuario_ruta.id_ruta=id_ruta
    nusuario_ruta.favorito= favorito
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usuario_ruta.route("/deleteusuario_ruta/<id>", methods=["DELETE"])
def deleteusuario_ruta(id):
    id_usuario_ruta = request.json['id_usuario_ruta']
    usuario_rutax = usuario_ruta.query.get(id_usuario_ruta)
    db.session.delete(usuario_rutax)
    db.session.commit()