
from config.db import app, db, ma

class lugar_estrategico(db.Model):
    __tablename__ = "tbllugar_estrategico"
    id_lugar= db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    

    def __init__(self, id_lugar,nombre):
        self.id_lugar=id_lugar
        self.nombre=nombre
        
with app.app_context():
    db.create_all()


class lugar_estrategicoSchema(ma.Schema):
    class Meta:
        fields = ('id_lugar', 'nombre')

lugar_estrategico_Schema = lugar_estrategicoSchema()
lugares_estrategicos_Schema = lugar_estrategicoSchema(many=True)