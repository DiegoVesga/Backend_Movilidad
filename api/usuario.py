from flask import Blueprint, jsonify, request,json,session,render_template,redirect
from config.db import db, app, ma
from models.usuario import usuario, usuario_schema,usuarios_schema


ruta_usuario = Blueprint("ruta_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_usuario.route("/usuario", methods=["GET"])
def getusuario():
    resultall = usuario.query.all()
    result = usuarios_schema.dump(resultall)
    return jsonify(result)

@ruta_usuario.route("/saveusuario", methods=["POST"]) #Para enviar o subir un registro
def saveusuario():
    try:
        username=request.json['username']
        password=request.json['password']
        nombre=request.json['nombre']
        new_usuario= usuario(username,password,nombre)
        db.session.add(new_usuario)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"
    

@ruta_usuario.route("/updateusuario/<id>", methods=["PUT"]) #Actualizar registro
def updateusuario(id):
    try:
        id_usuario = usuario.query.get(id)
        if not id_usuario:
            return "El usuario no esta registrado"
        username=request.json['username']
        password=request.json['password']
        nombre=request.json['nombre']
        id_usuario.username=username 
        id_usuario.password=password 
        id_usuario.nombre=nombre 
        db.session.commit()
        return "Datos Actualizado con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_usuario.route("/deleteusuario/<id>", methods=["DELETE"])
def deleteusuario(id):
    try:
        id_usuario = usuario.query.get(id)
        if id_usuario is None:
            return jsonify("El usuario no se encuentra en la base de datos")
        db.session.delete(id_usuario)
        db.session.commit()
        return "El usuario ha sido eliminado con exito"
    except Exception as e:
        return f"Hubo un error{str(e)}"
    

@app.route("/Registro", methods=["POST"]) #Para enviar o subir un registro
def saveusuario():
    try:
        
        username=request.form['usuario']
        password=request.form['contrasena']
        nombre=request.form['nombre']
        print(username,password,nombre)
        new_usuario= usuario(username,password,nombre)
        db.session.add(new_usuario)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"
    


@app.route("/iniciosesion", methods=["POST"]) #Para enviar o subir un registro
def logusuario():

    usernamex=request.form['usuario']
    passwordx=request.form['contrasena']
    usuariox= usuario.query.filter_by(username=usernamex,password=passwordx).first()
    if usuariox :
        session['usuario']=usuariox.username
        return render_template ("Home2.html",usuariox = session['usuario'])
    else:
        return "mal"
    
    
@app.route('/salir')
def cerrar():
    session.pop('usuariox',None)
    return redirect('/login')



