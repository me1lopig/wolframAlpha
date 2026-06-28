# Configuración de logging para la aplicación Wolfram Alpha

import logging

# Configurar el logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("wolfram_alpha.log"),
    ],
)

logger = logging.getLogger(__name__)
