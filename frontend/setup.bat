@echo off
REM Script para configurar e iniciar la aplicación en Windows

echo.
echo ================================================
echo  Configurador de Algoritmos de Búsqueda
echo ================================================
echo.

REM Crear entorno virtual
echo [1/4] Creando entorno virtual...
python -m venv venv
if errorlevel 1 (
    echo Error al crear el entorno virtual
    exit /b 1
)

REM Activar entorno virtual
echo [2/4] Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo [3/4] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error al instalar dependencias
    exit /b 1
)

REM Ejecutar servidor
echo [4/4] Iniciando servidor Django...
echo.
echo Servidor disponible en: http://localhost:8000
echo Presiona Ctrl+C para detener el servidor
echo.
python manage.py runserver
