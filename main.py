from flask import Flask, render_template,request,Response
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask import redirect
from flask import g
import forms
from flask import flash

from config import DevelopmentConfig
from models import db
from models import Empleados, Ventas

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


@app.route("/eliminar",methods=["GET","POST"])
def eliminar():
    empleados_form=forms.EmpleadosForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        empleado1=db.session.query(Empleados).filter(Empleados.id==id).first()
        empleados_form.id.data=request.args.get('id')
        empleados_form.nombre.data=empleado1.nombre
        empleados_form.email.data=empleado1.email
        empleados_form.telefono.data=empleado1.telefono
        empleados_form.direccion.data=empleado1.direccion
        empleados_form.sueldo.data=empleado1.sueldo
    if request.method=='POST':
        id=empleados_form.id.data
        empl=Empleados.query.get(id)
        db.session.delete(empl)
        db.session.commit()
        return redirect('tableEmpleados')
    
    return render_template("eliminar.html",form=empleados_form)

@app.route("/modificar",methods=["GET","POST"])
def modificar():
    empleados_form=forms.EmpleadosForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        empleado1=db.session.query(Empleados).filter(Empleados.id==id).first()
        empleados_form.id.data=request.args.get('id')
        empleados_form.nombre.data=empleado1.nombre
        empleados_form.email.data=empleado1.email
        empleados_form.telefono.data=empleado1.telefono
        empleados_form.direccion.data=empleado1.direccion
        empleados_form.sueldo.data=empleado1.sueldo
    if request.method=='POST':
        id=empleados_form.id.data
        empleado1=db.session.query(Empleados).filter(Empleados.id==id).first()
        empleado1.nombre=empleados_form.nombre.data
        empleado1.email=empleados_form.email.data
        empleado1.telefono=empleados_form.email.data
        empleado1.direccion=empleados_form.direccion.data
        empleado1.sueldo=empleados_form.sueldo.data
        db.session.add(empleado1)
        db.session.commit()
        return redirect('tableEmpleados')
    
    return render_template("modificar.html",form=empleados_form)
arrPizzas=[]
@app.route('/regPizza',methods=['GET','POST'])
def regPizza():
    reg_pizza=forms.FormPizzas(request.form)
    allVentas=Ventas.query.all()
    if request.method == 'POST':
        if request.form.get('registrar'):
            tamanios=int(reg_pizza.tamanioPizza.data)
            ingredientes=int(reg_pizza.ingredientes.data)
            nombre=reg_pizza.nombre.data;
            direccion=reg_pizza.direccion.data;
            telefono=reg_pizza.telefono.data;
            numPizzas=reg_pizza.numPizzas.data;
            preciotamanio=0
            ingrediente=0
            tamanio=''
            nameIngredient=''
        
            if tamanios == 0:
                preciotamanio=40
                tamanio='Chica'
            elif tamanios == 1:
                preciotamanio=80
                tamanio='Mediana'
            elif tamanios == 2:
                preciotamanio=120
                tamanio="Grande"
        
            if ingredientes == 0 :
                ingrediente = 10
                nameIngredient='Jamon'
            elif ingredientes == 1:
                ingrediente = 10
                nameIngredient='Piña'
            elif ingredientes == 2:
                ingrediente = 10
                nameIngredient='Champiñones'

            total=(numPizzas * preciotamanio) + ingrediente;
        
            arrPizzas.append([nombre, direccion, telefono, tamanio,nameIngredient, numPizzas, total])
            
            for v in allVentas:
               print(v.nombre)
            
        elif request.form.get('eliminar'):
            if arrPizzas:
                arrPizzas.pop()
        
        elif request.form.get('registrarBD'):
            if arrPizzas:
                for pizzas in arrPizzas:
                    piza = Ventas(nombre=pizzas[0],
                                  direccion=pizzas[1],
                                  telefono=pizzas[2],
                                  tamanioPizza=pizzas[3],
                                  ingredientes=pizzas[4],
                                  numPizzas=pizzas[5],
                                  total=pizzas[6]
                                  )
                    db.session.add(piza)
                    arrPizzas.clear()
                db.session.commit()
                print('Se agrego correctamente')    
            print('Hola')
            
    
        
    return render_template("pizzas.html",form=reg_pizza,arreglos=arrPizzas,ventas=allVentas)

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