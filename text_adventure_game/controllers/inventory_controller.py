from text_adventure_game.services.inventory_service import InventoryService
from flask import jsonify, session
from text_adventure_game.database import Session

session_db = Session()

def get_inventory_controller():
    """Endpoint para obtener el inventario de un jugador."""
    player_id = session.get("player_id")  # ID del jugador en la sesión
    inventory = InventoryService.get_inventory(session_db, player_id)
    return jsonify(inventory)

def add_item_controller(inventory_id, item_id, quantity):
    """Endpoint para agregar un ítem al inventario."""
    InventoryService.add_item_to_inventory(session_db, inventory_id, item_id, quantity)
    return jsonify({"message": "Item added successfully"})
