# text_adventure_game/controllers/player_controller.py

from flask import jsonify, request
from text_adventure_game.database import Session
from text_adventure_game.models.player_model import Player

session = Session()

def create_player():
    data = request.json
    new_player = Player(username=data['username'], email=data['email'], password=data['password'])
    
    session.add(new_player)
    session.commit()
    
    return jsonify({"message": "Player created", "player_id": new_player.id}), 201
