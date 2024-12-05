from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from text_adventure_game.database import Base
from text_adventure_game.database import Session


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)  
    description = Column(String(200))
    effect = Column(String(100))  
    
    def __init__(self, name, type, description, effect):
        self.name = name
        self.type = type
        self.description = description
        self.effect = effect