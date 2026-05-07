import sys
import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Agregar la carpeta padre al path para importar los scripts
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

CIUDADES_CANONICAS = {
    'jiloyork': 'Jiloyork',
    'sonora': 'Sonora',
    'guanajuato': 'Guanajuato',
    'oaxaca': 'Oaxaca',
    'sinaloa': 'Sinaloa',
    'queretaro': 'Queretaro',
    'celaya': 'Celaya',
    'zacatecas': 'Zacatecas',
    'monterrey': 'Monterrey',
    'tamaulipas': 'Tamaulipas',
    'cdmx': 'CDMX',
    'guadalajara': 'Guadalajara',
    'puerto_vallarta': 'Puerto_Vallarta',
    'aguascalientes': 'Aguascalientes',
    'morelos': 'Morelos',
    'hidalgo': 'Hidalgo',
    'mexicali': 'Mexicali',
    'mty': 'MTY',
    'qro': 'QRO',
    'ags': 'AGS',
    'slp': 'SLP',
}


def normalizar_ciudad(valor):
    """Convierte la entrada del usuario al nombre canónico del grafo."""
    if valor is None:
        return ''
    texto = str(valor).strip()
    if not texto:
        return ''
    llave = texto.replace(' ', '_').lower()
    return CIUDADES_CANONICAS.get(llave, texto)


def index(request):
    """Página principal con el menú"""
    opciones = [
        {
            'id': 1,
            'nombre': 'Carretera USC',
            'descripcion': 'Búsqueda de Costo Uniforme',
            'color': '#FF6B6B',
            'icon': '🛣️'
        },
        {
            'id': 2,
            'nombre': 'Vuelos BFS',
            'descripcion': 'Búsqueda en Amplitud',
            'color': '#4ECDC4',
            'icon': '✈️'
        },
        {
            'id': 3,
            'nombre': 'Vuelos DFS',
            'descripcion': 'Búsqueda en Profundidad Iterativa',
            'color': '#45B7D1',
            'icon': '🚁'
        }
    ]
    return render(request, 'index.html', {'opciones': opciones})


@require_http_methods(["POST"])
def ejecutar_algoritmo(request):
    """Ejecuta el algoritmo seleccionado"""
    try:
        data = json.loads(request.body)
        algoritmo = data.get('algoritmo')
        estado_inicial = normalizar_ciudad(data.get('estado_inicial', 'Jiloyork'))
        solucion = normalizar_ciudad(data.get('solucion', 'Monterrey'))
        resultado = None
        
        if algoritmo == 'usc':
            resultado = ejecutar_usc(estado_inicial, solucion)
        elif algoritmo == 'bfs':
            resultado = ejecutar_bfs(estado_inicial, solucion)
        elif algoritmo == 'dfs':
            resultado = ejecutar_dfs(estado_inicial, solucion)
        
        return JsonResponse({
            'success': True,
            'resultado': resultado,
            'mensaje': 'Búsqueda completada exitosamente'
        })
    except json.JSONDecodeError as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


def ejecutar_usc(estado_inicial, solucion):
    """Ejecuta la búsqueda USC desde Carretera_USC.py"""
    from Carretera_USC import CONEXIONES, buscar_solucion_USC

    resultado = buscar_solucion_USC(CONEXIONES, estado_inicial, solucion)
    
    if resultado:
        # Reconstruir la ruta desde el nodo final hacia atrás
        ruta = []
        nodo = resultado
        while nodo.get_padre() is not None:
            ruta.append(nodo.get_datos())
            nodo = nodo.get_padre()
        ruta.append(estado_inicial)
        ruta.reverse()
        
        return {
            'tipo': 'USC',
            'encontrado': True,
            'ruta': ruta,
            'destino': resultado.get_datos(),
            'costo': resultado.get_costo()
        }
    return {'tipo': 'USC', 'encontrado': False}


def ejecutar_bfs(estado_inicial, solucion):
    """Ejecuta la búsqueda BFS desde Vuelos_BFS.py"""
    from Vuelos_BFS import buscar_solucion_BFS
    
    CONEXIONES = {
        'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Guanajuato': {'Aguascalientes'},
        'Oaxaca': {'Queretaro'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Queretaro': {'Monterrey'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Tamaulipas': {'Queretaro'},
        'CDMX': {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'}
    }
    
    resultado = buscar_solucion_BFS(CONEXIONES, estado_inicial, solucion)
    
    if resultado:
        # Reconstruir la ruta
        ruta = []
        nodo = resultado
        while nodo.get_padre() is not None:
            ruta.append(nodo.get_datos())
            nodo = nodo.get_padre()
        ruta.append(estado_inicial)
        ruta.reverse()
        
        return {
            'tipo': 'BFS',
            'encontrado': True,
            'ruta': ruta,
            'destino': resultado.get_datos()
        }
    return {'tipo': 'BFS', 'encontrado': False}


def ejecutar_dfs(estado_inicial, solucion):
    """Ejecuta la búsqueda DFS desde Vuelos_bpi.py"""
    from Vuelos_bpi import DFS_profundidad_iterativa
    from arbol import Nodo
    
    nodo_inicial = Nodo(estado_inicial)
    resultado = DFS_profundidad_iterativa(nodo_inicial, solucion)
    
    if resultado:
        # Reconstruir la ruta
        ruta = []
        nodo = resultado
        while nodo.get_padre() is not None:
            ruta.append(nodo.get_datos())
            nodo = nodo.get_padre()
        ruta.append(estado_inicial)
        ruta.reverse()
        
        return {
            'tipo': 'DFS',
            'encontrado': True,
            'ruta': ruta,
            'destino': resultado.get_datos()
        }
    return {'tipo': 'DFS', 'encontrado': False}
