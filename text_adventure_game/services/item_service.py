from sqlalchemy.orm import Session
from text_adventure_game.models.item_model import Item


class ItemService:
    @staticmethod
    def create_item(session: Session, name: str, description: str):
        """Crear un nuevo objeto"""
        new_item = Item(name=name, description=description)
        session.add(new_item)
        session.commit()
        return f"Item {name} created successfully"

    @staticmethod
    def get_item_details(session: Session, item_id: int):
        """Obtener detalles de un objeto"""
        item = session.query(Item).filter_by(id=item_id).first()
        if not item:
            raise ValueError("Item not found")
        return {
            "id": item.id,
            "name": item.name,
            "description": item.description,
        }
