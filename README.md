# Wolfram Alpha Visual Explorer

> **Una aplicación Streamlit para consultas visuales a la API de Wolfram Alpha**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-ff4b4b.svg)](https://streamlit.io/)

---

## 📌 **Descripción**

**Wolfram Alpha Visual Explorer** es una aplicación web construida con **Streamlit** que permite realizar consultas directas a la **Simple API de Wolfram Alpha** y visualizar los resultados en forma de imágenes renderizadas. Ideal para cálculos matemáticos, gráficos de funciones, integrales, derivadas, y cualquier consulta que Wolfram Alpha pueda procesar.

---

## 🏗️ **Estructura del Proyecto**

```
wolframAlpha/
├── src/                          # Código fuente principal
│   ├── __init__.py
│   ├── app.py                    # Lógica principal de Streamlit
│   └── config.py                 # Configuración de la API
│
├── utils/                        # Funciones auxiliares (opcional)
│   ├── __init__.py
│   ├── helpers.py                # Funciones de apoyo
│   └── logger.py                 # Gestión de logs
│
├── tests/                        # Pruebas unitarias
│   ├── __init__.py
│   └── test_app.py               # Pruebas de la aplicación
│
├── docs/                         # Documentación
│   └── usage.md                  # Guía de uso detallada
│
├── scripts/                      # Scripts de automatización
│   └── deploy.sh                 # Script para despliegue
│
├── requirements.txt              # Dependencias del proyecto
├── .gitignore                    # Archivos ignorados por Git
├── LICENSE                       # Licencia Apache 2.0
└── README.md                     # Este archivo
```

---

## ⚙️ **Requisitos Previos**

- **Python 3.8 o superior**
- **Clave de API de Wolfram Alpha** (obténla gratis en [Wolfram Alpha Developer Portal](https://developer.wolframalpha.com/))
- **Git** (opcional, para clonar el repositorio)

---

## 🚀 **Instalación**

### 1. Clonar el repositorio

```bash
git clone https://github.com/me1lopig/wolframAlpha.git
cd wolframAlpha
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar la clave de API

#### Opción A: Usando variables de entorno (recomendado)
1. Crea un archivo `.env` en la raíz del proyecto:
   ```bash
   touch .env
   ```
2. Añade tu clave de API:
   ```env
   WOLFRAM_APP_ID=tu_clave_alfanumérica_aquí
   ```
3. Asegúrate de que la ruta en `src/app.py` apunte a tu archivo `.env`:
   ```python
   ruta_env = "/ruta/a/tu/archivo/.env"
   ```

#### Opción B: Modificar `src/config.py`
Edita el archivo y reemplaza el valor por defecto:
```python
WOLFRAM_ALPHA_API_KEY = "TU_CLAVE_DE_API"
```

---

## 🎯 **Uso**

### Ejecutar la aplicación

```bash
python -m src.app
```

O, si prefieres usar Streamlit directamente:

```bash
streamlit run src/app.py
```

### Interfaz de la aplicación

1. **Barra lateral (Sidebar):**
   - Selecciona el **tema visual** (Modo Claro/Oscuro)
   - Ajusta el **ancho de la imagen** (400px - 1200px)

2. **Área principal:**
   - Introduce tu consulta en inglés (ej: `plot x^2 * sin(x)`)
   - Haz clic en **"Renderizar Resultado"**

3. **Resultado:**
   - La imagen generada por Wolfram Alpha se mostrará automáticamente

### Ejemplos de consultas

| Tipo               | Ejemplo                          | Descripción                          |
|--------------------|----------------------------------|--------------------------------------|
| **Gráficos**       | `plot x^2 * sin(x) from 0 to 10` | Gráfico de la función `x² * sin(x)` |
| **Integrales**     | `integrate 1/(1+x^2)`            | Cálculo de integral indefinida       |
| **Derivadas**      | `derivative of x^3 + 2x^2`       | Cálculo de derivada                  |
| **Ecuaciones**     | `solve x^2 + 2x - 3 = 0`         | Resolución de ecuaciones             |
| **Física**         | `speed of light`                  | Consulta de constantes físicas       |
| **Química**        | `molecular formula of water`     | Fórmulas químicas                    |

---

## 📂 **Configuración Avanzada**

### Parámetros de la API

La aplicación usa la **Simple API** de Wolfram Alpha con los siguientes parámetros:

| Parámetro   | Descripción                          | Valores posibles          |
|-------------|--------------------------------------|---------------------------|
| `appid`     | Clave de API                          | Tu clave alfanumérica     |
| `i`         | Consulta (query)                     | Texto codificado en URL   |
| `background`| Color de fondo                       | `white`, `transparent`    |
| `foreground`| Color del texto                      | `black`, `white`          |
| `width`     | Ancho de la imagen (px)              | 400 - 1200                |
| `layout`    | Estilo de los títulos                | `labelbar` (por defecto)   |

### Personalización

Puedes modificar los valores por defecto en:
- `src/config.py`: Configuración de la API
- `src/app.py`: Parámetros de Streamlit y lógica de la aplicación

---

## 🧪 **Pruebas**

Para ejecutar las pruebas unitarias:

```bash
python -m unittest discover tests
```

O, si usas `unittest2`:

```bash
python -m unittest2 discover tests
```

---

## 📄 **Documentación**

- [Guía de Uso](docs/usage.md): Instrucciones detalladas y ejemplos avanzados
- [API de Wolfram Alpha](https://products.wolframalpha.com/simple-api/documentation/): Documentación oficial

---

## 🔧 **Dependencias**

| Paquete          | Versión  | Descripción                          |
|------------------|----------|--------------------------------------|
| `streamlit`      | 1.0+     | Framework para aplicaciones web     |
| `requests`       | 2.25.1+  | Solicitudes HTTP a la API            |
| `python-dotenv`  | 0.19.0+  | Gestión de variables de entorno      |
| `urllib3`        | -        | Manejo de URLs (incluido en Python)  |

> **Nota:** Las dependencias se instalan automáticamente al ejecutar `pip install -r requirements.txt`

---

## 📜 **Licencia**

Este proyecto está licenciado bajo la **Apache License 2.0**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 🤝 **Contribuciones**

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un **fork** del repositorio
2. Crea una rama con tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz **commit** (`git commit -m 'Añade nueva funcionalidad'`)
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`)
5. Abre un **Pull Request**

---

## 📞 **Contacto**

- **Autor:** [me1lopig](https://github.com/me1lopig)
- **Repositorio:** [me1lopig/wolframAlpha](https://github.com/me1lopig/wolframAlpha)
- **Issues:** [Reportar un problema](https://github.com/me1lopig/wolframAlpha/issues)

---

> **⚠️ Importante:** Asegúrate de **no exponer tu clave de API** en el código o en repositorios públicos. Usa siempre variables de entorno o archivos `.env` para gestionar credenciales sensibles.
