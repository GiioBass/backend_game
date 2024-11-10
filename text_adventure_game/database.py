# text_adventure_game/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from text_adventure_game.config import DATABASE_URL

# Crear la clase Base, que es la base de todos los modelos de SQLAlchemy
Base = declarative_base()

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear todas las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
