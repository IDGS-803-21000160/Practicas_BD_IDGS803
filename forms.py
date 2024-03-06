from wtforms import Form
from wtforms  import StringField,IntegerField,EmailField,RadioField
from wtforms import validators
 

class EmpleadosForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
    ])
    email=EmailField('email',[
        validators.Email(message='Ingresa edad valida')
    ])
    telefono=IntegerField('telefono',[
        validators.DataRequired(message='El campo es requerido')
    ])
    direccion=StringField('direccion',[
        validators.DataRequired(message='El campo es requerido')
    ])
    sueldo=IntegerField('sueldo',[
        validators.DataRequired(message='El campo es requerido')
    ])

class FormPizzas(Form):
    id=IntegerField('id')
    tamanioPizza= RadioField('', choices=[(0, 'Chica $40'), (1, 'Mediana $80'), (2, 'Grande $120')])
    ingredientes= RadioField('', choices=[(0, 'Jamon $10'), (1, 'Piña $10'), (2, 'Champiñones $10')])
    nombre=StringField('Nombre')
    direccion=StringField('Direccion')
    telefono=IntegerField('Telefono')
    numPizzas=IntegerField('Num. Pizzas')
