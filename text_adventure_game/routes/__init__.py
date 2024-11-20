from .player_routes import player_bp
from .character_routes import character_bp


blueprints = [
    (player_bp, '/player'),
    (character_bp, '/character')
    ]