# WTForms
from wtforms import fields  # type: ignore
from wtforms import validators

# Flask-WTF
from flask_wtf import FlaskForm  # type: ignore


class LoginForm(FlaskForm):

    username = fields.StringField('Nombre de usuario',
                                  validators=[validators.DataRequired()])

    password = fields.PasswordField('Password',
                                    validators=[validators.DataRequired()])

    submit = fields.SubmitField('Enviar')


class SignupForm(FlaskForm):

    username = fields.StringField('Nombre de usuario',
                                  validators=[validators.DataRequired()])

    password = fields.PasswordField('Password',
                                    validators=[validators.DataRequired()])

    password_confirm = fields.PasswordField('Confirmar password',
                                            validators=[validators.DataRequired(),
                                                        validators.EqualTo('password',
                                                                            message='Las contraseñas no coinciden')])

    submit = fields.SubmitField('Enviar')
