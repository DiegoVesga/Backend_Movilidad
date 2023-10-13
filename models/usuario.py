
from config.db import app, db, ma

class usuario(db.Model):
    __tablename__ = "tblusuario"
    id_usuario= db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    nombre = db.Column(db.String(50))

    

    def __init__(self,username,password,nombre):
        self.username=username
        self.password=password
        self.nombre=nombre
        
        
with app.app_context():
    db.create_all()


class usuario_Schema(ma.Schema):
    class Meta:
        fields = ('id_usuario','username','password','nombre')

usuario_schema = usuario_Schema()
usuarios_schema = usuario_Schema(many=True)