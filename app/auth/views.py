# Werkzeug
from werkzeug.security import generate_password_hash

# Flask
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for

# Flask-Login
from flask_login import login_user  # type: ignore
from flask_login import login_required
from flask_login import logout_user

# Firestore service
from app.firestore_service import get_user
from app.firestore_service import create_user

# Forms
from app.forms.auth import LoginForm
from app.forms.auth import SignupForm

# Models
from app.models import UserModel
from app.models import UserData

# App
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Login view.

    This view is responsible for handling the login process.
    """
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        # Get user from database
        user_document = get_user(username)

        if user_document is not None:
            user_dict = user_document.to_dict()
        else:
            user_dict = None

        # Check if user exists
        if user_dict is not None:
            password_from_db = user_dict['password']

            # Verify password
            if password_from_db == password:
                user = UserModel.from_document(user_document)
                login_user(user)

                flash('Bienvenido de nuevo!')

                return redirect(url_for('tasks.index'))

            else:
                flash('La información no coincide.')

        else:
            flash('El usuario no existe.')

    return render_template('login.html', **context)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """signup view.

    This view is responsible for handling the signup process.
    """

    signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        # Get user from database
        user_document = get_user(username)

        if user_document:
            user_dict = user_document.to_dict()
        else:
            user_dict = None

        # Check if user exists
        if user_dict is None:
            password_hash = generate_password_hash(password)

            user_data = UserData(username, password_hash)
            create_user(user_data)

            user = UserModel(user_data)

            login_user(user)

            flash('Bienvenido!')

            return redirect(url_for('tasks.index'))

        else:
            flash('El usuario ya existe.')

    return render_template('signup.html', **context)


@auth.route('/logout')
@login_required
def logout():
    """Logout view.

    This view is responsible for handling the logout process.
    """

    logout_user()

    flash('Regresa pronto!')

    return redirect(url_for('auth.login'))
