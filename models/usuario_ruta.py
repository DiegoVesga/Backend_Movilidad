from config.db import app, db, ma

class usuario_ruta(db.Model):
    __tablename__ = "tblusuario_ruta"
    id_usuario_ruta= db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id_usuario'))
    id_ruta = db.Column(db.Integer, db.ForeignKey('tblruta.id_ruta'))

    def __init__(self, id_usuario_ruta, id_usuario, id_ruta):
        self.id_usuario_ruta= id_usuario_ruta
        self.id_usuario = id_usuario
        self.id_ruta = id_ruta
 

        
with app.app_context():
    db.create_all()


class usuario_rutaSchema(ma.Schema):
    class Meta:
        fields = ('id_usuario_ruta','id_usuario', 'id_ruta')

usuario_ruta_schema = usuario_rutaSchema()
usuario_rutas_schema = usuario_rutaSchema(many=True)