# text_adventure_game/controllers/player_controller.py

from flask import jsonify, request
from text_adventure_game.database import Session
from text_adventure_game.models.player_model import Player

session = Session()

def create_player():
    data = request.get_json()
    username = data.get('username')
    level = 0
    experience = 0
    new_player = Player(username=username, level=level, experience=experience)
    
    session.add(new_player)
    session.commit()
    
    return jsonify({"message": "Player created", "player_id": new_player.username}), 201
