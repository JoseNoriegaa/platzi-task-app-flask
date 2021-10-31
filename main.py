import unittest

# Flask
from flask import make_response
from flask import redirect
from flask import render_template

# App
from app import create_app

app = create_app()

@app.cli.command()
def test():
    """Runs the unit tests."""

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.errorhandler(404)
def not_found(error):
    return make_response(render_template('404.html', error=error), 404)


@app.errorhandler(500)
def internal_error(error):
    return make_response(render_template('500.html', error=error), 500)


@app.route('/')
def index():
    """Index.

    Entry point of the application.
    """

    return make_response(redirect('/tasks'))
