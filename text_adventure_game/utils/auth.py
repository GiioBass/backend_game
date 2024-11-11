import jwt
from datetime import datetime, timedelta
from text_adventure_game.config import SECRET_KEY  # Asegúrate de tener una clave secreta en tu configuración
from text_adventure_game.models.player_model import Player

def generate_token(user_id):
    """Generar un token JWT para el usuario con su ID"""
    payload = {
        "sub": user_id,  # ID del usuario (puede ser 'user_id' o 'uuid', según tu preferencia)
        "exp": datetime.utcnow() + timedelta(hours=1)  # Expiración en 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    """Decodificar un token y extraer el payload"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload  # Contiene los datos del usuario
    except jwt.ExpiredSignatureError:
        return None  # El token ha expirado
    except jwt.InvalidTokenError:
        return None  # El token es inválido
