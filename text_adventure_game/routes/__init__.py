from .player_routes import player_bp
from .character_routes import character_bp
from .inventory_routes import inventory_bp
from .item_routes import item_bp


blueprints = [
    (player_bp, '/player'),
    (character_bp, '/character'),
    (inventory_bp, '/inventory'),
    (item_bp, '/item'),
    ]