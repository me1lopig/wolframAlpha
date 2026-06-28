# Wolfram Alpha API Client

Una aplicación en Python para interactuar con la API de Wolfram Alpha.

## Estructura del Proyecto
```
wolframAlpha/
├── src/                  # Código fuente
│   ├── __init__.py
│   ├── app.py            # Lógica principal
│   ├── config.py         # Configuraciones
│   └── utils/            # Funciones auxiliares
│       ├── __init__.py
│       ├── helpers.py
│       └── logger.py
│
├── tests/                # Pruebas unitarias
│   ├── __init__.py
│   └── test_app.py
│
├── docs/                 # Documentación
│   └── usage.md
│
├── scripts/              # Scripts de automatización
│   └── deploy.sh
│
├── requirements.txt      # Dependencias
├── .gitignore            # Archivos ignorados
└── README.md
```

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

3. Configura tu clave de API en `src/config.py`.

## Uso
Ejecuta la aplicación:
```bash
python -m src.app
```

## Documentación
Consulta [docs/usage.md](docs/usage.md) para más detalles.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
