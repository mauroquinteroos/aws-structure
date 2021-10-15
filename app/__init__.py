from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import SEC_DATABASE_URI, DATABASE_URI


db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config["SQLALCHEMY_BINDS"] = {
        'base': SEC_DATABASE_URI
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    from . import home
    from . import auth
    app.register_blueprint(home.bp, url_prefix='')
    app.register_blueprint(auth.bp, url_prefix='/api/auth')

    return app
