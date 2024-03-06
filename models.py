from flask_sqlalchemy import SQLAlchemy
import datetime


db=SQLAlchemy()
class Empleados(db.Model):
    __tablename__='colaboradores'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    email=db.Column(db.String(50))
    telefono=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    sueldo=db.Column(db.String(50))

class Ventas(db.Model):
    __tablename__='ventas'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(100))
    telefono=db.Column(db.String(50))
    numPizzas=db.Column(db.String(50))
    tamanioPizza=db.Column(db.String(50))
    ingredientes=db.Column(db.String(50))
    total=db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)
    
    
