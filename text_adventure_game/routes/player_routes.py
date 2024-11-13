from flask import Blueprint
from text_adventure_game.controllers.player_controller import create_player, login_player,  get_profile_player
from text_adventure_game.utils.middleware_auth import token_required

player_bp = Blueprint('player', __name__)

@player_bp.route('/register', methods=['POST'])
def register_player():
    return create_player()

@player_bp.route('/login', methods=['POST'])
def login():
    return login_player()

@player_bp.route('/profile/<int:id>', methods=['GET'])
@token_required  # Protección con el middleware
def profile(id):
    return get_profile_player(id)