from config.db import app, db, ma

class ruta_lugar_estrategico(db.Model):
    __tablename__ = "tblruta_lugar_estrategico"
    id_lugar = db.Column(db.Integer, db.ForeignKey('tbllugar_estrategico.id_lugar'), primary_key=True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('tblruta.id_ruta'),primary_key=True)

    def __init__(self,  id_lugar, id_ruta):
        self.id_lugar = id_lugar
        self.id_ruta = id_ruta
 

        
with app.app_context():
    db.create_all()


class ruta_lugar_estrategicoSchema(ma.Schema):
    class Meta:
        fields = ('id_lugar', 'id_ruta')

ruta_lugar_estrategico_Schema = ruta_lugar_estrategicoSchema()
ruta_lugar_estrategicos_Schema = ruta_lugar_estrategicoSchema(many=True)
