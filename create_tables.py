from text_adventure_game.database import Base, engine
from text_adventure_game.models.player_model import Player  # Importación explícita
from text_adventure_game.models.character_model import Character  # Importación explícita

# Crear las tablas
Base.metadata.create_all(engine)
