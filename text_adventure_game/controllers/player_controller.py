
from flask import jsonify, request
from text_adventure_game.database import Session
from text_adventure_game.models.player_model import Player
from email_validator import validate_email, EmailNotValidError
from sqlalchemy.exc import IntegrityError
import uuid
from text_adventure_game.utils.logger import logger


session = Session()

def create_player():
    try:
        data = request.get_json()
        user_name = data.get("user_name")
        
        email = data.get("email")
        user_code = data.get("user_code")
        password = data.get("password")
        user_uuid = uuid.uuid4()
        
        
         # Verifica si el email ya existe
        existing_player = session.query(Player).filter_by(email=email).first()
        if existing_player:
            return jsonify({"message": "Email already exists"}), 400
        
        if not is_valid_email(email):
            return jsonify({"message": "The email is invalid"}), 402
        
        if " " in user_name:
            return jsonify({"message": "The user name can't have spaces"}), 402
            
        new_player = Player(user_name=user_name,email=email,user_code=user_code,password=password,uuid=user_uuid,)

        session.add(new_player)
        session.commit()

        return jsonify({"message": "Player created", "player_id": new_player.user_name}),201
    
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    except IntegrityError as e:
        session.rollback()  # Rollback the transaction
        return jsonify({"message": "Email already exists"}), 400

def is_valid_email(email):
    try:
        # Valida el email utilizando la librería email-validator
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False
    
    
def login_player():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # Buscar al jugador por su email
        player = session.query(Player).filter_by(email=email).first()

        if not player:
            return jsonify({"message": "Email not found"}), 404

        # Verificar si la contraseña es correcta
        if not player.check_password(password):
            return jsonify({"message": "Incorrect password"}), 401

        return jsonify({"message": "Login successful", "player_id": player.id, "player_name": player.user_name}), 200
    except Exception as e:
        session.rollback()  
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500