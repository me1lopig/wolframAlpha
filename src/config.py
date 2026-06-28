# Configuración de la aplicación Wolfram Alpha

# Clave de API de Wolfram Alpha (debe guardarse en variables de entorno en producción)
WOLFRAM_ALPHA_API_KEY = "YOUR_API_KEY_HERE"

# URL base de la API de Wolfram Alpha
WOLFRAM_ALPHA_API_URL = "https://api.wolframalpha.com/v2/query"

# Parámetros por defecto para las consultas
DEFAULT_PARAMS = {
    "format": "plaintext",
    "input": "",
    "appid": WOLFRAM_ALPHA_API_KEY,
}
