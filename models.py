from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
class Empleados(db.Model):
    __tablename__='colaboradores'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    email=db.Column(db.String(50))
    telefono=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    sueldo=db.Column(db.String(50))
