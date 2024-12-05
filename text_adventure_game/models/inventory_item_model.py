from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from text_adventure_game.database import Base
from text_adventure_game.database import Session

class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True)
    inventory_id = Column(Integer, ForeignKey('inventories.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    quantity = Column(Integer, default=1)

    inventory = relationship('Inventory', back_populates='items')
    item = relationship('Item')

    def __init__(self, inventory_id, item_id, quantity):
        self.inventory_id = inventory_id
        self.item_id = item_id
        self.quantity = quantity