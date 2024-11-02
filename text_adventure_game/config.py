# config.py

import os

# Configuración de la base de datos
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+pymysql://username:password@localhost/db_name')

