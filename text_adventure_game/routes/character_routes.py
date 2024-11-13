from flask import Blueprint
from text_adventure_game.utils.middleware_auth import token_required

player_bp = Blueprint('character', __name__)

@player_bp.route('/register', methods=['POST'])
@token_required
def create_character():
    return create_player()
