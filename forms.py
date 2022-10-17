from xml.etree.ElementTree import Comment
from wtforms import Form
from wtforms import StringField, TextAreaField
from wtforms import EmailField, SubmitField



from wtforms.validators import DataRequired, Email, Length

from wtforms import validators

class CommentForm(Form):
    username = StringField('username',[validators.length(min=4, max=8, message='Ingrese un usuario alido')])
    email = EmailField('Correo electronico')
    comment = TextAreaField('Comentario')
    submit = SubmitField('Send')
