from flask import Flask, render_template,request,Response
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask import redirect
from flask import g
import forms
from flask import flash

from config import DevelopmentConfig
from models import db
from models import Empleados

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()
app.secret_key='esta es la clave secreta'

@app.route("/index",methods=["GET","POST"])
def index():
    empleados_form=forms.EmpleadosForm(request.form)
    if request.method=='POST':
        empl=Empleados(nombre=empleados_form.nombre.data,
                       email=empleados_form.email.data,
                      telefono=empleados_form.telefono.data,
                      direccion=empleados_form.direccion.data,
                      sueldo=empleados_form.sueldo.data)
        db.session.add(empl)
        db.session.commit()
    return render_template("index.html",form=empleados_form)

@app.route("/tableEmpleados",methods=["GET","POST"])
def TablaEmpleados():
    empleados_form=forms.EmpleadosForm(request.form)
    emplead=Empleados.query.all()
    return render_template("tableEmpleados.html",empleadoss=emplead)

#Funcion que nos permite manejar el error 404 y mandar lo que queramos con el html
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
    

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()