from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from text_adventure_game.database import Base

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    level = Column(Integer, default=1)
    health = Column(Float, default=100)
    energy = Column(Float, default=100)
    experience = Column(Float, default=0)

    # Relación con el jugador propietario
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    player = relationship('Player', back_populates='characters')
 