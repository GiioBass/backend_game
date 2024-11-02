from sqlalchemy import Column, Integer, String
from text_adventure_game import db

class Player(db.Model):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)

    def __repr__(self):
        return f"<Player(id={self.id}, username={self.username}, level={self.level})>"
