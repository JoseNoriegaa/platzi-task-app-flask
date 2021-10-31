# WTForm
from wtforms import fields  # type: ignore
from wtforms import validators

# Flask WTF
from flask_wtf import FlaskForm  # type: ignore


class CreateTaskForm(FlaskForm):
    """
    Form for creating a new task
    """

    title = fields.StringField('Título',
        [
            validators.DataRequired(message='El título es requerido.'),
            validators.Length(min=3, max=50, message='El título de ser de 3 a 50 caracteres de longitud.')
        ]
    )

    description = fields.TextAreaField(
        'Descripción',
        [
            validators.DataRequired(message='La descripción es requerida'),
            validators.Length(min=3, max=255, message='La descripción debe de ser de 3 a 255 caracteres de longitud.')
        ]
    )

    submit = fields.SubmitField('Registrar Tarea')



class DeleteTaskForm(FlaskForm):
    """
    Form for deleting a task
    """

    submit = fields.SubmitField('Eliminar Tarea')


class UpdateTaskStatusForm(FlaskForm):
    """
    Form for updating a task's status
    """

    status = fields.SelectField(
        'Estado',
        [
            validators.DataRequired(message='Status is required'),
            validators.Length(min=3, max=100, message='Status must be between 3 and 100 characters long')
        ],
        choices=[
            ('No comenzada', 'No comenzada'),
            ('En proceso', 'En proceso'),
            ('Completada', 'Completada')
        ]
    )


class UpdateTaskForm(UpdateTaskStatusForm, CreateTaskForm):
    """
    Form for updating a task
    """

    submit = fields.SubmitField('Actualizar Tarea')
