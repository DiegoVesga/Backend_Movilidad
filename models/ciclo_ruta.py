from config.db import app, db, ma

class ciclo_ruta(db.Model):
    __tablename__ = "tblciclo_ruta"
    id_ciclo = db.Column(db.Integer, db.ForeignKey('tblciclovia.id_ciclo'), primary_key=True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('tblruta.id_ruta'),primary_key=True)

    def __init__(self,  id_ciclo, id_ruta):
        self.id_ciclo = id_ciclo
        self.id_ruta = id_ruta
 

        
with app.app_context():
    db.create_all()


class ciclo_rutaSchema(ma.Schema):
    class Meta:
        fields = ('id_ciclo', 'id_ruta')

ciclo_ruta_schema = ciclo_rutaSchema()
ciclo_rutas_schema = ciclo_rutaSchema(many=True)