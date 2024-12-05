from sqlalchemy.orm import Session
from text_adventure_game.models.inventory_model import Inventory
from text_adventure_game.models.inventory_item_model import InventoryItem


class InventoryService:

    def get_inventory(session, player_id):
        """Obtener el inventario de un jugador."""
        inventory = session.query(Inventory).filter_by(player_id=player_id).first()
        if not inventory:
            raise ValueError("Inventory not found")
        return inventory

    def add_item_to_inventory(
        session: Session, inventory_id: int, item_id: int, quantity: int = 1
    ):
        """Añadir un objeto al inventario"""
        inventory = session.query(Inventory).filter_by(id=inventory_id).first()
        if not inventory:
            raise ValueError("Inventory not found")

        # Verificar si el objeto ya está en el inventario
        inventory_item = next(
            (i for i in inventory.items if i.item_id == item_id), None
        )
        if inventory_item:
            inventory_item.quantity += quantity
        else:
            new_item = InventoryItem(
                inventory_id=inventory_id, item_id=item_id, quantity=quantity
            )
            session.add(new_item)

        session.commit()
        return f"Added {quantity} of item {item_id} to inventory {inventory_id}"

    def use_item_from_inventory(session: Session, inventory_id: int, item_id: int):
        """Usar un objeto del inventario"""
        inventory = session.query(Inventory).filter_by(id=inventory_id).first()
        if not inventory:
            raise ValueError("Inventory not found")

        inventory_item = next(
            (i for i in inventory.items if i.item_id == item_id), None
        )
        if not inventory_item or inventory_item.quantity <= 0:
            raise ValueError("Item not available in inventory")

        inventory_item.quantity -= 1
        if inventory_item.quantity == 0:
            session.delete(inventory_item)

        session.commit()
        return f"Used item {item_id} from inventory {inventory_id}"
