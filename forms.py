from wtforms import Form
from wtforms  import StringField,IntegerField,EmailField,RadioField
from wtforms import validators
 

class EmpleadosForm(Form):
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
    