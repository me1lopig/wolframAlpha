#!/bin/bash

# Script de despliegue para la aplicación Wolfram Alpha

echo "Iniciando despliegue..."

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pruebas (opcional)
echo "Ejecutando pruebas..."
python -m unittest discover tests

# Verificar si las pruebas pasaron
if [ $? -eq 0 ]; then
    echo "Pruebas pasadas. Despliegue exitoso."
else
    echo "Pruebas fallidas. Deteniendo despliegue."
    exit 1
fi
