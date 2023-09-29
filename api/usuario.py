from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.usuario import usuario, usuario_schema,usuarios_schema


ruta_usuario = Blueprint("ruta_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_usuario.route("/usuario", methods=["GET"])
def usuario():
    resultall = usuario.query.all()
    result = usuarios_schema.dump(resultall)
    return jsonify(result)

@ruta_usuario.route("/saveusuario", methods=["POST"])
def saveusuario():
    id_usuario = request.json['id_usuario']
    nombre=request.json['nombre']
    new_usuario= usuario(id_usuario,nombre)
    db.session.add(new_usuario)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_usuario.route("/updateusuario", methods=["PUT"])
def updateusuario():
    id_usuario = request.json['id_usuario']
    nombre=request.json['nombre']
    nusuario = usuario.query.get(id_usuario) #Select * from Cliente where id = id
    nusuario.nombre=nombre 
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usuario.route("/deleteusuario/<id>", methods=["DELETE"])
def deleteusuario(id):
    id_usuario = request.json['id_usuario']
    usuariox = usuario.query.get(id_usuario)
    db.session.delete(usuariox)
    db.session.commit()
    