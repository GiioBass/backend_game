from flask import Blueprint, request
from text_adventure_game.utils.middleware_auth import token_required
from text_adventure_game.controllers.inventory_controller import get_inventory_controller, add_item_controller

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/get', methods=['GET'])
@token_required
def get_inventory():
    return get_inventory_controller()

@inventory_bp.route('/add', methods=['POST'])
@token_required
def add_item():
    data = request.get_json()
    return add_item_controller(data['inventory_id'], data['item_id'], data['quantity'])
