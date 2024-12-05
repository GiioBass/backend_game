from flask import Blueprint, request
from text_adventure_game.utils.middleware_auth import token_required
from text_adventure_game.controllers.item_controller import use_item_controller

item_bp = Blueprint('item', __name__)

@item_bp.route('/use', methods=['POST'])
@token_required
def use_item():
    data = request.get_json()
    return use_item_controller(data['inventory_id'], data['item_id'])
