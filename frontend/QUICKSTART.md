# Quick Start Guide - Guía de Inicio Rápido

## 🚀 Inicio Rápido

### En Windows:
```bash
cd frontend
setup.bat
```

### En macOS/Linux:
```bash
cd frontend
chmod +x setup.sh
./setup.sh
```

## 📱 Cómo usar la aplicación

1. **Abre el navegador** en `http://localhost:8000`
2. **Haz clic en una de las 3 opciones:**
   - 🛣️ **Carretera USC** - Búsqueda de Costo Uniforme
   - ✈️ **Vuelos BFS** - Búsqueda en Amplitud
   - 🚁 **Vuelos DFS** - Búsqueda en Profundidad Iterativa
3. **Completa el formulario:**
   - Estado Inicial: Punto de partida (ej: Jiloyork)
   - Destino/Solución: Punto de llegada (ej: Monterrey)
4. **Haz clic en "Ejecutar Búsqueda"**
5. **Observa el resultado**

## 🔧 Pasos de Instalación Detallados

### Paso 1: Preparar la carpeta
```bash
# Asegúrate de estar en la carpeta frontend
cd frontend
```

### Paso 2: Crear entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar
```bash
python manage.py runserver
```

## ✅ Verificación

Abre tu navegador y ve a `http://localhost:8000`. Deberías ver:
- ✓ Título: "🔍 Algoritmos de Búsqueda"
- ✓ Tres tarjetas de colores diferentes
- ✓ Cada tarjeta con icono, nombre y descripción

## 🐛 Si algo no funciona

### Error: "No module named 'arbol'"
```bash
# Verifica que los archivos estén en la carpeta padre
# parcial2/
#   ├── arbol.py          ← Debe estar aquí
#   ├── Carretera_USC.py
#   ├── Vuelos_BFS.py
#   ├── Vuelos_bpi.py
#   └── frontend/
```

### Error: "Port 8000 already in use"
```bash
# Usa otro puerto
python manage.py runserver 8001
```

### Error en la página estática (CSS/JS no carga)
```bash
# Recolectar archivos estáticos
python manage.py collectstatic
```

## 📤 Desplegar en Render

Ver instrucciones completas en [README.md](README.md#-desplegar-en-render)

## 💡 Tips

- **Reinicia el servidor** después de cambiar vistas o templates (Ctrl+C, luego `python manage.py runserver`)
- **Usa F12** en el navegador para ver errores en consola
- **Limpia el cache** (Ctrl+Shift+Delete) si ves CSS/JS antiguos
- **Cambia los parámetros** para probar diferentes búsquedas

## 📞 Soporte

Para problemas específicos, revisa los logs del servidor en la terminal donde ejecutaste `runserver`.
