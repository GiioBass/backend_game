from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from text_adventure_game.database import Base
from text_adventure_game.database import Session

session_db = Session()

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    level = Column(Integer, default=1)
    health = Column(Float, default=100)
    energy = Column(Float, default=100)
    experience = Column(Float, default=0)

    # Relación con el jugador propietario
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    player = relationship("Player", back_populates="characters")

    def __init__(self, name, level, health, energy, experience, player_id):
        self.name = name
        self.level = level
        self.health = health
        self.energy = energy
        self.experience = experience
        self.player_id = player_id

    def update_experience(character, exp_gained):
    # """Función para actualizar la experiencia y nivel del personaje"""
    # Aumentamos la experiencia
        character.experience += exp_gained
        
        # Verificar si el personaje debe subir de nivel
        if character.experience >= 100:  # Ejemplo, 100 de experiencia para subir de nivel
            character.level += 1
            character.experience = 0  # Restablecemos la experiencia para el siguiente nivel
            return f"{character.name} ha subido de nivel a {character.level}!"

        # Guardamos los cambios
        session_db.commit()
        return f"{character.name} ha ganado {exp_gained} de experiencia."

    def update_health(character, damage):
        """Función para actualizar la salud del personaje"""
        character.health -= damage
        if character.health <= 0:
            character.health = 0
            # Aquí podrías manejar el evento de "muerte" del personaje si es necesario
            return f"{character.name} ha muerto."

        session_db.commit()
        return f"{character.name} ha recibido {damage} de daño. Salud actual: {character.health}."

    def update_energy(character, energy_used):
        """Función para actualizar la energía del personaje"""
        character.energy -= energy_used
        if character.energy < 0:
            character.energy = 0
        session_db.commit()
        return f"{character.name} ha usado {energy_used} de energía. Energía restante: {character.energy}."

