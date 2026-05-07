# Vuelos con búsqueda en profundidad iterativa
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

def DFS_profundidad_iterativa(nodo, solucion):
    for limite in range(0, 100):
        visitados = []
        sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
        if sol is not None:
            return sol
    return None


def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite):
    if limite >= 0:
        visitados.append(nodo)

        # Verificar si es la solución
        if nodo.get_datos() == solucion:
            return nodo
        else:
            # Expandir nodos hijos
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in CONEXIONES[dato_nodo]:
                hijo = Nodo(un_hijo)
                hijo.set_padre(nodo)  # Para reconstruir el camino

                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)

            nodo.set_hijos(lista_hijos)

            # Recorrer hijos
            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.en_lista(visitados):
                    # IMPORTANTE: copiar lista de visitados
                    sol = buscar_solucion_DFS_Rec(
                        nodo_hijo, solucion, visitados.copy(), limite - 1
                    )
                    if sol is not None:
                        return sol
    return None


if __name__ == "__main__":
    estado_inicial = 'Jiloyork'
    ciudad_objetivo = 'Oaxaca'

    nodo_inicial = Nodo(estado_inicial)
    nodo_resultado = DFS_profundidad_iterativa(nodo_inicial, ciudad_objetivo)

    # Mostrar resultado
    if nodo_resultado is not None:
        resultado = []
        while nodo_resultado is not None:
            resultado.append(nodo_resultado.get_datos())
            nodo_resultado = nodo_resultado.get_padre()

        resultado.reverse()
        print("Ruta encontrada:", resultado)
    else:
        print("Solución no encontrada.")
