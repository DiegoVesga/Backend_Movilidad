
from config.db import app, db, ma

class ruta(db.Model):
    __tablename__ = "tblruta"
    id_ruta= db.Column(db.Integer, primary_key = True)
    punto_inicio = db.Column(db.String(50))
    punto_final=db.Column(db.String(50))
    

    def __init__(self, id_ruta,punto_inicio,punto_final):
        self.id_ruta = id_ruta
        self.punto_inicio=punto_inicio
        self.punto_final=punto_final
        
with app.app_context():
    db.create_all()


class rutaSchema(ma.Schema):
    class Meta:
        fields = ('id_ruta', 'punto_inicio','punto_final')

ruta_schema = rutaSchema()
rutas_schema = rutaSchema(many=True)