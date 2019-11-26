from flask import Blueprint

from App.model import Person

blue = Blueprint("first_blue", __name__)


def init_first_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return "HelloFlask"


@blue.route('/create')
def create_person():
    person = Person()
    return 'Create success'
