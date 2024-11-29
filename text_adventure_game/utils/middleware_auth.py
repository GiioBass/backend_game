from flask import request, jsonify, session
from text_adventure_game.utils.auth import decode_token
from text_adventure_game.utils.logger import logger
from functools import wraps

def token_required(f):
    """Middleware para proteger rutas que requieren autenticación"""
    @wraps(f)
    def decorator_route(*args, **kwargs):
        # Obtener el token de las cabeceras Authorization
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing"}), 403  # Token no proporcionado

        try:
            token = token.split(" ")[1]  # El formato es "Bearer <token>"
        except IndexError:
            return jsonify({"message": "Token format is invalid"}), 403  # Formato inválido

        # Decodificar el token
        payload = decode_token(token)
        if not payload:
            return jsonify({"message": "Token is invalid or expired"}), 403  # Token inválido o expirado

        # Guardar el UUID del jugador en la sesión
        session['player_uuid'] = payload.get('sub') 

        # Continuar con la ejecución de la función
        return f(*args, **kwargs)

    return decorator_route
