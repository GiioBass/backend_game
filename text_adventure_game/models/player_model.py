from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from text_adventure_game.database import Base  # Importamos Base de db.py
import bcrypt
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=False, nullable=False)
    email = Column(String(50), unique=True, nullable=False, index=True)
    user_code = Column(String(50), unique=False, nullable=False)
    password = Column(
        String(255), unique=False, nullable=False, info={"protected": True}
    )
    uuid = Column(String(255), unique=True, nullable=False)

    def __init__(self, user_name, email, user_code, password, uuid):
        self.user_name = user_name
        self.email = email
        self.user_code = user_code
        self.password = self.hash_password(password) 
        self.uuid = uuid
        
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
