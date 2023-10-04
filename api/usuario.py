from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.usuario import usuario, usuario_schema,usuarios_schema


ruta_usuario = Blueprint("ruta_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_usuario.route("/usuario", methods=["GET"])
def getusuario():
    resultall = usuario.query.all()
    result = usuarios_schema.dump(resultall)
    return jsonify(result)

@ruta_usuario.route("/saveusuario", methods=["POST"])
def saveusuario():
    try:
        id_usuario = request.json['id_usuario']
        nombre=request.json['nombre']
        new_usuario= usuario(id_usuario,nombre)
        db.session.add(new_usuario)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"
    

@ruta_usuario.route("/updateusuario/<id>", methods=["PUT"])
def updateusuario(id):
    try:
        id_usuario = usuario.query.get(id)
        if not id_usuario:
            return "El usuario no esta registrado"
        nombre=request.json['nombre']
        nusuario = usuario.query.get(id_usuario) #Select * from Cliente where id = id
        nusuario.nombre=nombre 
        db.session.commit()
        return "Datos Actualizado con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_usuario.route("/deleteusuario/<id>", methods=["DELETE"])
def deleteusuario(id):
    try:
        id_usuario = usuario.query.get(id)
        if not id_usuario:
            return "El usuario no se encuentra en la base de datos"
        usuariox = usuario.query.get(id_usuario)
        db.session.delete(usuariox)
        db.session.commit()
        return "El usuario ha sido eliminado con exito"
    except Exception as e:
        return f"Hubo un error{str(e)}"
    