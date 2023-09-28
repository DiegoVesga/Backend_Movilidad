
from config.db import app, db, ma

class ciclovia(db.Model):
    __tablename__ = "tblciclovia"
    id_ciclo = db.Column(db.Integer, primary_key = True)
    dir_inicio = db.Column(db.String(50))
    dir_fin = db.Column(db.String(50))

    def __init__(self, id_ciclo,dir_inicio,dir_fin):
        self.id_ciclo = id_ciclo
        self.dir_inicio=dir_inicio
        self.dir_fin=dir_fin

with app.app_context():
    db.create_all()


class cicloviaSchema(ma.Schema):
    class Meta:
        fields = ('id_ciclo', 'dir_inicio','dir_fin')

ciclovia_schema = cicloviaSchema()
ciclovias_schema = cicloviaSchema(many=True)