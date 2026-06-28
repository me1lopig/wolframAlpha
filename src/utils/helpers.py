# Funciones auxiliares para la aplicación Wolfram Alpha

def format_query(query: str) -> str:
    """
    Formatea una consulta para que sea compatible con la API de Wolfram Alpha.
    
    Args:
        query (str): La consulta a formatear.
    
    Returns:
        str: La consulta formateada.
    """
    return query.strip().replace(" ", "+")


def validate_response(response: dict) -> bool:
    """
    Valida si la respuesta de la API de Wolfram Alpha es válida.
    
    Args:
        response (dict): La respuesta de la API.
    
    Returns:
        bool: True si la respuesta es válida, False en caso contrario.
    """
    if not response:
        return False
    return "queryresult" in response
