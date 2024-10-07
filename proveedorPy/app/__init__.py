from flask import Flask
from logging.config import dictConfig
import os
from dotenv import load_dotenv
load_dotenv()

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    logger = app
    app.config.from_pyfile(config_filename)
    register_blueprints(app)
    return app

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def register_blueprints(app):
    from app.modulos.orden_de_compra import orden_de_compra_blueprint
    from app.models import db
    app.register_blueprint(orden_de_compra_blueprint)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+DB_USER+':'+DB_PASSWORD+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME+'?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()



    