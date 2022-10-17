from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField


from wtforms import validators

class CommentForm(Form):
    username = StringField('username'[validators.length(min=4, max=8, message='Ingrese un usuario alido')])
    email = EmailField('Correo electronico')
    comment = TextField('Comentario')
