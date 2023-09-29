
from config.db import app, db, ma

class concejos(db.Model):
    __tablename__ = "tblconcejos"
    id_concejo = db.Column(db.Integer, primary_key = True)
    id_usuario= db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    texto_concejo = db.Column(db.String(50))
    

    def __init__(self, id_concejo,id_usuario,texto_concejo):
        self.id_concejo=id_concejo
        self.id_usuario=id_usuario
        self.texto_concejo=texto_concejo
        
with app.app_context():
    db.create_all()


class concejos_Schema(ma.Schema):
    class Meta:
        fields = ('id_concejos','id_usuario', 'texto_concejo')

concejo_Schema = concejos_Schema()
concejoss_Schema = concejos_Schema(many=True)