import sys
import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Agregar la carpeta padre al path para importar los scripts
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from arbol import Nodo


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
        estado_inicial = data.get('estado_inicial', 'Jiloyork')
        solucion = data.get('solucion', 'Monterrey')
        
        resultado = None
        ruta = None
        
        if algoritmo == 'usc':
            resultado = ejecutar_usc(estado_inicial, solucion)
        elif algoritmo == 'bfs':
            resultado = ejecutar_bfs(estado_inicial, solucion)
        elif algoritmo == 'dfs':
            resultado = ejecutar_dfs(estado_inicial, solucion)
        
        return JsonResponse({
            'success': True,
            'resultado': resultado,
            'mensaje': f'Búsqueda completada exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


def ejecutar_usc(estado_inicial, solucion):
    """Ejecuta la búsqueda USC desde Carretera_USC.py"""
    from Carretera_USC import buscar_solucion_USC
    
    # Definir conexiones (costos de carreteras) - diccionario de diccionarios
    conexiones = {
        'Jiloyork': {'CDMX': 125, 'QRO': 513},
        'Morelos': {'QRO': 524},
        'CDMX': {'Jiloyork': 125, 'QRO': 423, 'Hidalgo': 491},
        'Hidalgo': {'CDMX': 491, 'QRO': 356, 'Mexicali': 309, 'MTY': 346},
        'QRO': {'SLP': 203, 'Morelos': 514, 'Jiloyork': 513, 'CDMX': 423, 'MTY': 603, 'Sonora': 437, 'Hidalgo': 356, 'Mexicali': 313, 'AGS': 599},
        'SLP': {'AGS': 390, 'QRO': 203},
        'AGS': {'SLP': 390, 'QRO': 599},
        'Sonora': {'QRO': 437, 'Mexicali': 394},
        'Mexicali': {'MTY': 296, 'Hidalgo': 309, 'QRO': 313},
        'MTY': {'Mexicali': 296, 'QRO': 603, 'Hidalgo': 346},
    }
    
    resultado = buscar_solucion_USC(conexiones, estado_inicial, solucion)
    
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
