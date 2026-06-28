import streamlit as st
import urllib.parse
import os
from dotenv import load_dotenv

# 1. Configuración y carga de variables de entorno
# Aquí está la ruta inventada. Cámbiala por la ruta real de tu sistema.
ruta_env = "/home/imac/Documentos/env/.env"
load_dotenv(dotenv_path=ruta_env)

# Extraemos la clave de la variable que hemos definido en el archivo .env
APP_ID = os.getenv("WOLFRAM_APP_ID")

# 2. Configuración de la página de Streamlit
st.set_page_config(
    page_title="Wolfram Explorer", 
    page_icon="🐺", 
    layout="centered"
)

st.title("Motor de Cálculo Visual")
st.markdown("Consultas directas a la **Simple API** de Wolfram|Alpha")

# 3. Barra lateral para la parametrización de la imagen
st.sidebar.header("Parámetros de la API")
st.sidebar.markdown("Ajusta cómo renderizará Wolfram la imagen final:")

tema_visual = st.sidebar.radio("Tema del resultado:", ["Modo Claro", "Modo Oscuro"])
ancho_imagen = st.sidebar.slider("Ancho de renderizado (px)", min_value=400, max_value=1200, value=750, step=50)

# Lógica para adaptar los parámetros 'background' y 'foreground' a la API
if tema_visual == "Modo Oscuro":
    bg_color = "transparent" # Queda genial sobre el fondo oscuro por defecto de Streamlit
    fg_color = "white"
else:
    bg_color = "white"
    fg_color = "black"

# 4. Interfaz principal
query = st.text_input(
    "Introduce tu consulta, cálculo o función (en inglés):", 
    placeholder="Ej: plot x^2 * sin(x), integrate 1/(1+x^2)"
)

# 5. Ejecución de la consulta
if st.button("Renderizar Resultado", type="primary"):
    
    # Comprobación de seguridad inicial
    if not APP_ID or APP_ID == "TU_CLAVE_ALFANUMERICA_AQUI":
        st.error(f"⚠️ **Error de Autenticación:** No se ha encontrado una API Key válida. Verifica que el archivo existe en `{ruta_env}` y contiene la variable `WOLFRAM_APP_ID`.")
    
    elif not query.strip():
        st.warning("Por favor, introduce una consulta antes de procesar.")
    
    else:
        with st.spinner("Conectando con el motor de Wolfram..."):
            # Codificamos la ecuación para que los caracteres +, = o / no rompan la URL
            query_url = urllib.parse.quote_plus(query)
            
            # Construimos la petición a la Simple API con todos los parámetros
            url = (
                f"https://api.wolframalpha.com/v1/simple"
                f"?appid={APP_ID}"
                f"&i={query_url}"
                f"&background={bg_color}"
                f"&foreground={fg_color}"
                f"&width={ancho_imagen}"
                f"&layout=labelbar" # Añade unas cajas sombreadas a los títulos de la imagen
            )
            
            try:
                # Streamlit maneja automáticamente la descarga e incrustación de la imagen desde la URL
                st.image(url, caption=f"Resultado generado para: {query}")
                
            except Exception as e:
                st.error(f"Ocurrió un error al cargar la imagen: {e}")