from flask import Blueprint
from text_adventure_game.utils.middleware_auth import token_required
from text_adventure_game.controllers.character_controller import create_character_player

character_bp = Blueprint('character', __name__)

@character_bp.route('/create', methods=['POST'])
@token_required
def create_character():
    return create_character_player()
