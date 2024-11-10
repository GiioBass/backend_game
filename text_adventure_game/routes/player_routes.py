from flask import Blueprint, request, jsonify
from text_adventure_game.controllers.player_controller import create_player, login_player

player_bp = Blueprint('player', __name__)

@player_bp.route('/register', methods=['POST'])
def register_player():
    return create_player()

@player_bp.route('/login', methods=['POST'])
def login_player():
    return create_player()