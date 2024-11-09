# text_adventure_game/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from text_adventure_game.config import DATABASE_URL

from text_adventure_game.models.player_model import Base

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear todas las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
