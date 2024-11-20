from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from text_adventure_game.config import SECRET_KEY, DATABASE_URL
from os import getenv
from text_adventure_game.utils.logger import logger
from dotenv import load_dotenv 

load_dotenv()

db = SQLAlchemy()  # Creamos la instancia de SQLAlchemy

def create_app():
  
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Vinculamos SQLAlchemy con la app
    return app
