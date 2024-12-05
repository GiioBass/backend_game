from flask import jsonify, request, session
from text_adventure_game.models.player_model import Player
from text_adventure_game.models.player_model import Character
from text_adventure_game.utils.logger import logger
from text_adventure_game.database import Session

session_db = Session()

def create_character_player():
    try:
        player_uuid = str(session.get('player_uuid')) 
        player = session_db.query(Player).filter_by(uuid=player_uuid).first()
        data = request.get_json()
        logger.info(f"player character controller: {player.id}")
        name = data.get('name')
        level = 0
        health = 100
        energy = 100
        experience = 0
        player_id = player.id
        
        new_character = Character(name=name,level=level,health=health,energy=energy,experience=experience,player_id=player_id)
        session_db.add(new_character)
        session_db.commit()

        return jsonify({'message':'Character created successfull', 'Character name':new_character.name}), 200
    except Exception as e:
        return jsonify({'An error occurred while creating the character'}), 500
    
def get_character_stats(character_id):
    try:
        # Consultar el personaje por ID
        character = session_db.query(Character).filter_by(id=character_id).first()

        if not character:
            return jsonify({'message': 'Character not found'}), 404

        # Retornar estadísticas
        character_data = {
            'id': character.id,
            'name': character.name,
            'level': character.level,
            'health': character.health,
            'energy': character.energy,
            'experience': character.experience,
            'player_id': character.player_id,
        }
        return jsonify({'character': character_data}), 200
    except Exception as e:
        logger.error(f"Error fetching character stats: {str(e)}")
        return jsonify({'message': 'An error occurred while fetching the character stats'}), 500