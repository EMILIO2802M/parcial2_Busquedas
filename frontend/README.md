# Algoritmos de Búsqueda - Frontend Django

Aplicación web interactiva para ejecutar algoritmos de búsqueda (USC, BFS, DFS) en grafos de ciudades y carreteras.

## 🚀 Características

- **Interfaz moderna y responsiva** con diseño de gradientes y animaciones
- **3 algoritmos de búsqueda**: USC, BFS, DFS
- **Menú interactivo** para seleccionar el algoritmo
- **Modal para configurar parámetros** de búsqueda
- **Resultados en tiempo real**

## 📋 Requisitos Previos

- Python 3.8+
- pip (gestor de paquetes de Python)
- git (opcional)

## 🛠️ Instalación Local

### 1. Clonar el repositorio (o descargar el archivo)

```bash
git clone <url-del-repositorio>
cd frontend
```

### 2. Crear entorno virtual

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Copiar scripts de algoritmos

Asegúrate de que los scripts `arbol.py`, `Carretera_USC.py`, `Vuelos_BFS.py` y `Vuelos_bpi.py` 
estén en la carpeta padre (parcial2):

```
parcial2/
├── arbol.py
├── Carretera_USC.py
├── Vuelos_BFS.py
├── Vuelos_bpi.py
└── frontend/
    ├── manage.py
    ├── config/
    └── menu_app/
```

### 5. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://localhost:8000`

## 🌐 Desplegar en Render

### 1. Preparar el repositorio

```bash
# Crear archivo .env (opcional para desarrollo local)
echo "SECRET_KEY=tu-clave-secreta-muy-larga" > .env
echo "DEBUG=False" >> .env
```

### 2. Crear repositorio en GitHub

```bash
git init
git add .
git commit -m "Inicial: Django app con algoritmos de búsqueda"
git branch -M main
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

### 3. Conectar con Render

1. Ir a [render.com](https://render.com)
2. Crear una nueva cuenta o iniciar sesión
3. Hacer clic en **"New +"** → **"Web Service"**
4. Seleccionar el repositorio de GitHub
5. Llenar la configuración:
   - **Name**: `algoritmos-busqueda` (o el nombre que prefieras)
   - **Environment**: `Python 3.11`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn config.wsgi`
   - **Plan**: Free (o el que prefieras)

6. Agregar variables de entorno:
   - `SECRET_KEY`: Una clave secreta larga y aleatoria
   - `DEBUG`: `False`

7. Hacer clic en **"Create Web Service"**

⏳ Render comenzará a desplegar la aplicación. Esto puede tomar 2-5 minutos.

## 📝 Estructura del Proyecto

```
frontend/
├── config/                    # Configuración de Django
│   ├── settings.py           # Configuración principal
│   ├── urls.py               # URLs principales
│   ├── wsgi.py               # WSGI para producción
│   └── __init__.py
├── menu_app/                 # Aplicación principal
│   ├── static/               # Archivos estáticos
│   │   ├── css/
│   │   │   └── style.css    # Estilos personalizados
│   │   └── js/
│   │       └── script.js    # JavaScript del cliente
│   ├── templates/            # Templates HTML
│   │   └── index.html        # Página principal
│   ├── views.py              # Vistas de Django
│   ├── urls.py               # URLs de la app
│   ├── models.py             # Modelos (no usados)
│   ├── apps.py               # Configuración de la app
│   └── __init__.py
├── manage.py                 # Script de gestión de Django
├── requirements.txt          # Dependencias Python
├── Procfile                  # Configuración para Render
├── runtime.txt               # Versión de Python
└── README.md                 # Este archivo
```

## 🎨 Personalización

### Agregar más algoritmos

1. Editar `menu_app/views.py` y agregar una nueva función
2. Actualizar `menu_app/templates/index.html` con una nueva tarjeta
3. Actualizar `menu_app/static/js/script.js` con el nuevo algoritmo

### Cambiar colores

En `menu_app/static/css/style.css`, modificar las variables CSS en `:root`:

```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    /* ... más colores */
}
```

## 🐛 Solución de Problemas

### Error: "No module named 'arbol'"

Asegúrate de que los scripts estén en la carpeta padre de `frontend/`

### Error: "ModuleNotFoundError" al desplegar en Render

Verifica que `requirements.txt` incluya todas las dependencias necesarias

### La página se ve diferente en móvil

La app es totalmente responsiva. Si hay problemas, limpia el cache del navegador (Ctrl+Shift+Delete)

## 📧 Contacto

Para problemas o sugerencias, contacta al administrador del proyecto.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
