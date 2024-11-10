# logger.py

import logging

# Configuración global de logging
logging.basicConfig(
    filename='text_adventure_game/logs/app.log',  # Archivo donde se guardarán los logs
    level=logging.DEBUG,  # Nivel de log: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato del log
)

# Crear un logger específico si quieres utilizar diferentes "loggers" en el futuro
logger = logging.getLogger(__name__)  # Esto crea un logger con el nombre del módulo

# Si solo usarás logging básico, el siguiente código es suficiente:
# logging.debug("Esto es un mensaje de debug")

# Usando el logger
# logger.debug("Este es un mensaje de debug")
# logger.info("Este es un mensaje de información")
# logger.warning("Este es un mensaje de advertencia")
# logger.error("Este es un mensaje de error")
# logger.critical("Este es un mensaje crítico")