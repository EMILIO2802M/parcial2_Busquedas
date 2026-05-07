# Vuelos con busqueda en amplitud
from arbol import Nodo


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


def obtener_ciudades(conexiones):
    ciudades = set(conexiones.keys())
    for destinos in conexiones.values():
        ciudades.update(destinos)
    return sorted(ciudades)

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []

    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera[0]

        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))

        if nodo.get_datos() == solucion:
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones.get(dato_nodo, []):
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None


def reconstruir_ruta(nodo_solucion, estado_inicial):
    ruta = []
    nodo = nodo_solucion

    while nodo.get_padre() is not None:
        ruta.append(nodo.get_datos())
        nodo = nodo.get_padre()

    ruta.append(estado_inicial)
    ruta.reverse()
    return ruta


def pedir_ciudad(mensaje, ciudades_validas):
    while True:
        ciudad = input(mensaje).strip()
        if ciudad in ciudades_validas:
            return ciudad
        print("Ciudad no valida. Opciones:", ", ".join(ciudades_validas))


if __name__ == "__main__":
    conexiones_base = CONEXIONES
    lista_ciudades = obtener_ciudades(conexiones_base)
    print("Ciudades disponibles:", ", ".join(lista_ciudades))

    ciudad_origen = pedir_ciudad("Ingresa estado inicial: ", lista_ciudades)
    ciudad_destino = pedir_ciudad("Ingresa estado destino: ", lista_ciudades)

    nodo_resultado = buscar_solucion_BFS(conexiones_base, ciudad_origen, ciudad_destino)

    if nodo_resultado is not None:
        resultado = reconstruir_ruta(nodo_resultado, ciudad_origen)
        print("Ruta encontrada:", " -> ".join(resultado))
    else:
        print("No se encontró solución")