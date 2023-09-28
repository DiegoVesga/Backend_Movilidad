
from config.db import app, db, ma

class alerta(db.Model):
    __tablename__ = "tblalerta"
    id_alerta = db.Column(db.Integer, primary_key = True)
    tipo_alerta = db.Column(db.String(50))
    fecha=db.Column(db.Date)
    id_ciclo = db.Column(db.Integer, db.ForeignKey('ciclovia.id_ciclo'))

    def __init__(self, id_alerta,tipo_alerta,fecha,id_ciclo):
        self.id_ciclo = id_ciclo
        self.id_alerta= id_alerta
        self.tipo_alerta=tipo_alerta
        self.fecha=fecha

        
with app.app_context():
    db.create_all()


class alertaSchema(ma.Schema):
    class Meta:
        fields = ('id_alerta', 'tipo_alerta','fecha','id_ciclo')

alerta_schema = alertaSchema()
alertas_schema = alertaSchema(many=True)