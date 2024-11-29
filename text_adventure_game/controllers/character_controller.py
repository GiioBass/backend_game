from flask import jsonify, request, session
from text_adventure_game.database import Session
from text_adventure_game.models.player_model import Player
from text_adventure_game.models.player_model import Character
from text_adventure_game.utils.logger import logger

session_db = Session()

def create_character_player():
    try:
        player_uuid = str(session.get('player_uuid')) 
        player = session_db.query(Player).filter_by(uuid=player_uuid).first()
        logger('player', player)
        data = request.get_json()
        name = data.get('name')
        level = 0
        health = 100
        energy = 100
        experience = 0
        player_id = player.id
        
        new_character = Character(name=name,level=level,health=health,energy=energy,experience=experience,player_id=player_id)
       
        return jsonify({'message':'Character created successfull', 'Character name':new_character.name}), 200
    except Exception as e:
        return jsonify({'An error occurred while creating the character'}), 500