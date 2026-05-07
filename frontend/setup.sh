#!/bin/bash

# Script para configurar e iniciar la aplicación en Linux/macOS

echo ""
echo "================================================"
echo " Configurador de Algoritmos de Búsqueda"
echo "================================================"
echo ""

# Crear entorno virtual
echo "[1/4] Creando entorno virtual..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error al crear el entorno virtual"
    exit 1
fi

# Activar entorno virtual
echo "[2/4] Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "[3/4] Instalando dependencias..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error al instalar dependencias"
    exit 1
fi

# Ejecutar servidor
echo "[4/4] Iniciando servidor Django..."
echo ""
echo "Servidor disponible en: http://localhost:8000"
echo "Presiona Ctrl+C para detener el servidor"
echo ""
python manage.py runserver
