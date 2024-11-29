from flask import Blueprint
from text_adventure_game.utils.middleware_auth import token_required
from text_adventure_game.controllers.character_controller import create_character_player, get_character_stats

character_bp = Blueprint('character', __name__)

@character_bp.route('/create', methods=['POST'])
@token_required
def create_character_route():
    return create_character_player()

@character_bp.route('/get-stats/<int:character_id>', methods=['GET'])
@token_required
def get_character_stats_route(character_id):
    return get_character_stats(character_id)