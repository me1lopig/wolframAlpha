# Guía de Uso de Wolfram Alpha API

## Introducción
Este documento describe cómo utilizar la aplicación para interactuar con la API de Wolfram Alpha.

## Requisitos Previos
1. Una clave de API de Wolfram Alpha. Puedes obtenerla en [Wolfram Alpha Developer Portal](https://developer.wolframalpha.com/).
2. Python 3.6 o superior.

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/me1lopig/wolframAlpha.git
   cd wolframAlpha
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura tu clave de API en el archivo `src/config.py`:
   ```python
   WOLFRAM_ALPHA_API_KEY = "TU_CLAVE_DE_API"
   ```

## Ejecución
Ejecuta el archivo principal:
```bash
python -m src.app
```

## Ejemplos
- Consulta: "What is the speed of light?"
- Consulta: "Integrate x^2"

## Configuración Adicional
Puedes modificar los parámetros por defecto en `src/config.py`.
