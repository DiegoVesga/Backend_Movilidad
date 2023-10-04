from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.consejos import consejos, consejo_schema,consejoss_Schema


ruta_consejos = Blueprint("ruta_consejos",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)



@ruta_consejos.route("/consejos", methods=["GET"])
def getconsejos():
    resultall = consejos.query.all()
    result = consejoss_Schema.dump(resultall)
    return jsonify(result)

@ruta_consejos.route("/saveconsejos", methods=["POST"])
def saveconsejos():
    try:
        id_consejos = request.json['id_consejos']
        id_usuario = request.json['id_usuario']
        texto_consejo = request.json['texto_consejo']
        new_consejos= consejos(id_consejos,id_usuario,texto_consejo)
        db.session.add(new_consejos)
        db.session.commit()
        return "Datos guardados con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_consejos.route("/updateconsejos/<id>", methods=["PUT"])
def updateconsejos(id):
    try:
        id_consejo = consejos.query.get(id) #Obtiene el dato el cual se va a buscar (.GET)
        if not id_consejo: #Si no lo encuentra...
            return "El consejo no se encuentra"#... muestra el mensaje
        texto_consejo = request.json['texto_consejo']
        id_consejo.texto_consejo=texto_consejo
        db.session.commit()
        return "Datos Actualizado con exitos"
    except Exception as e:
        return f"Hubo un error {str(e)}"

@ruta_consejos.route("/deleteconsejos/<id>", methods=["DELETE"])
def deleteconsejos(id):
    try:
        id_consejo= consejos.query.get(id)
        if not id_consejo: #Si no lo encuentra...
            return "El consejo no esta registrado"#... muestra el mensaje  
        db.session.delete(id_consejo)
        db.session.commit()
    except Exception as e:
        return f"Hubo un error {str(e)}"
    