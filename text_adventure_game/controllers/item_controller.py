from flask import jsonify
from text_adventure_game.services.inventory_service import InventoryService
from text_adventure_game.database import Session

session_db = Session()

def use_item_controller(inventory_id, item_id):
    """Endpoint para usar un ítem del inventario."""
    item = InventoryService.use_item_from_inventory(session_db, inventory_id, item_id)
    return jsonify({"message": "Item used successfully", "item": item})