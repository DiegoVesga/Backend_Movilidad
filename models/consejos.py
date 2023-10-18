
from config.db import app, db, ma

class consejos(db.Model):
    __tablename__ = "tblconsejos"
    id_consejo = db.Column(db.Integer, primary_key = True)
    id_usuario= db.Column(db.Integer, db.ForeignKey('tblusuario.id_usuario'))
    texto_consejo = db.Column(db.String(50))
    

    def __init__(self,id_usuario,texto_consejo):
        self.id_usuario=id_usuario
        self.texto_consejo=texto_consejo
        
with app.app_context():
    db.create_all()


class consejos_Schema(ma.Schema):
    class Meta:
        fields = ('id_consejos','id_usuario', 'texto_consejo')

consejo_schema = consejos_Schema()
consejoss_Schema = consejos_Schema(many=True)