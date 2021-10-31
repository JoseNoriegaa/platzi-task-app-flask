# Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import request

# Flask Login
from flask_login import current_user  # type: ignore
from flask_login import login_required


# Firestore Service
from app.firestore_service import get_tasks
from app.firestore_service import get_task
from app.firestore_service import create_task
from app.firestore_service import update_task_status
from app.firestore_service import update_task
from app.firestore_service import delete_task

# App
from app.task.config import task

# Forms
from app.forms.task import CreateTaskForm
from app.forms.task import DeleteTaskForm
from app.forms.task import UpdateTaskStatusForm
from app.forms.task import UpdateTaskForm


@task.route('/', methods=['GET'])
def index():
    """Tasks page.

    List all tasks.
    """

    username = current_user.id

    task_form = CreateTaskForm()
    update_status_form = UpdateTaskStatusForm()
    delete_task_form = DeleteTaskForm()

    context = {
        'username': username,
        'tasks': get_tasks(username),
        'task_form': task_form,
        'update_status_form': update_status_form,
        'delete_task_form': delete_task_form,
    }

    return render_template('task/index.html', **context)


@task.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Create page.

    Create a new task.
    """

    task_form = CreateTaskForm()

    context = {
        'task_form': task_form,
    }

    if task_form.validate_on_submit():
        title = task_form.title.data.title()
        description = task_form.description.data.capitalize()
        status = 'No comenzada'

        user_id = current_user.id

        create_task(user_id, {
            'title': title,
            'description': description,
            'status': status,
        })

        return redirect(url_for('tasks.index'))

    return render_template('task/create.html', **context)


@task.route('/<task_id>/update-status', methods=['POST'])
@login_required
def update_status(task_id: str):
    """Update status.

    Update task status.

    Args:
        task_id: Task id.
    """

    user_id = current_user.id

    # Check if task exists
    task_document = get_task(user_id, task_id)

    if task_document.exists:
        form = UpdateTaskStatusForm()

        if form.validate_on_submit():
            status = form.status.data

            update_task_status(user_id, task_id, status)

            flash('Tarea actualizada', 'success')

        else:
            flash('No se pudo actualizar la tarea.', 'danger')

    else:

        flash('La tarea no existe', 'danger')

    return redirect(url_for('tasks.index'))


@task.route('/<task_id>/update', methods=['GET', 'POST'])
@login_required
def update(task_id: str):
    """Update page.

    Update a task.

    Args:
        task_id: Task id.
    """

    task_document = get_task(current_user.id, task_id)

    # Check if task exists
    if not task_document.exists:
        return redirect(url_for('tasks.index'))

    task_form = UpdateTaskForm()

    # Fill the form with the task data
    if request.method == 'GET':
        task_dict = task_document.to_dict()

        task_form.title.data = task_dict['title']
        task_form.description.data = task_dict['description']
        task_form.status.data = task_dict['status']

    context = {
        'task': task_document,
        'task_form': task_form,
    }

    if task_form.validate_on_submit():
        title = task_form.title.data.title()
        description = task_form.description.data.capitalize()
        status = task_form.status.data

        user_id = current_user.id

        update_task(user_id, task_id, {
            'title': title,
            'description': description,
            'status': status,
        })

        flash('Tarea actualizada', 'success')

        return redirect(url_for('tasks.index'))

    return render_template('task/update.html', **context)


@task.route('/<task_id>/delete', methods=['POST'])
@login_required
def delete(task_id: str):
    """Delete task.

    Delete a task.

    Args:
        task_id: Task id.
    """

    user_id = current_user.id

    # Check if task exists
    task_document = get_task(user_id, task_id)

    if task_document.exists:
        delete_task_form = DeleteTaskForm()

        if delete_task_form.validate_on_submit():
            delete_task(user_id, task_id)

            flash('Tarea eliminada', 'success')

        else:
            flash('No se pudo eliminar la tarea.', 'danger')

    else:

        flash('La tarea no existe', 'danger')

    return redirect(url_for('tasks.index'))
