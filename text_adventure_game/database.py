# text_adventure_game/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from text_adventure_game.config import DATABASE_URL
from text_adventure_game.utils.logger import logger

# Crear la clase Base, que es la base de todos los modelos de SQLAlchemy
Base = declarative_base()
# Crear el motor de la base de datos
# logger.info(Base)
engine = create_engine(DATABASE_URL, echo=True)
# logger.info(engine)
# logger.info("Modelos detectados para la creación de tablas: %s", Base.metadata.tables.keys())

# Crear todas las tablas
try:
    Base.metadata.create_all(engine)
    # logger.info("Tablas creadas exitosamente.")
except Exception as e:
    logger.error("Error al crear las tablas: %s", e)

# Crear una sesión
Session = sessionmaker(bind=engine)
