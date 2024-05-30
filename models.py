from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    usuario = db.Column(db.String(50))
    correo = db.Column(db.String(100), unique=True, primary_key=True)
    telefono = db.Column(db.String(10))
    contrasenia = db.Column(db.String(100))
