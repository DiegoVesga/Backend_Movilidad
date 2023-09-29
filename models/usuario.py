
from config.db import app, db, ma

class usuario(db.Model):
    __tablename__ = "tblusuario"
    id_usuario= db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    

    def __init__(self, id_usuario,nombre):
        self.id_lugar=id_usuario
        self.nombre=nombre
        
with app.app_context():
    db.create_all()


class usuario_Schema(ma.Schema):
    class Meta:
        fields = ('id_usuario', 'nombre')

usuario_schema = usuario_Schema()
usuarios_schema = usuario_Schema(many=True)