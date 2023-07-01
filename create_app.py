from flask import Flask
from config.config import *
from db_models import *
from flask_login import LoginManager
from flask_cors import CORS

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    set_config(app.config, app.jinja_env)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.app_context().push()
    SESSION_TYPE = 'sqlalchemy'
    app.config.from_object(__name__)

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    login_manager = LoginManager()
    login_manager.init_app(app)

    return app
