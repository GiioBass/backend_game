from flask import request, jsonify, session
from text_adventure_game.utils.auth import decode_token
from text_adventure_game.utils.logger import logger

def token_required(f):
    """Middleware para proteger rutas que requieren autenticación"""
    def decorator(*args, **kwargs):
        # Obtener el token de las cabeceras Authorization
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing"}), 403  # Token no proporcionado

        token = token.split(" ")[1]  # El formato es "Bearer <token>"
        
        # Decodificar el token
        payload = decode_token(token)
     
        if not payload:
            return jsonify({"message": "Token is invalid or expired"}), 403  # Token inválido o expirado
        
        # Puedes acceder a la información del usuario con payload['sub']
        # Aquí puedes agregar el ID del usuario a la solicitud
        # request.player_id = payload["sub"]
        session['player_uuid'] = payload.get('sub') 
        return f(*args, **kwargs)  # Continuar con la ejecución de la función

    return decorator
