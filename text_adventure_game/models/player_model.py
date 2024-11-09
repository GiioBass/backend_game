from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from text_adventure_game import db

# Crear la clase Base, que es la base de todos los modelos de SQLAlchemy
Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)

    def __init__(self, username, level, experience):
        self.username = username
        self.level = level
        self.experience = experience