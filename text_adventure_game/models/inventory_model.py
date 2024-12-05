from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from text_adventure_game.database import Base
from text_adventure_game.database import Session

class Inventory(Base):
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    
    character = relationship('Character', back_populates='inventory')
    items = relationship('InventoryItem', back_populates='inventory')

    def __init__(self, player_id, character_id):
        self.player_id = player_id
        self.character_id = character_id