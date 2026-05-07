# Viaje por carretera por busqueda de costo uniforme
from arbol import Nodo


CONEXIONES = {
    'Jiloyork': {'CDMX': 125, 'Queretaro': 513, 'Sinaloa': 420},
    'CDMX': {'Jiloyork': 125, 'Queretaro': 423, 'Oaxaca': 491, 'Tamaulipas': 356},
    'Queretaro': {'Jiloyork': 513, 'CDMX': 423, 'Monterrey': 203, 'Celaya': 314},
    'Monterrey': {'Queretaro': 203, 'Sinaloa': 299, 'Zacatecas': 346},
    'Sinaloa': {'Jiloyork': 420, 'Celaya': 280, 'Sonora': 394, 'Monterrey': 299},
    'Celaya': {'Jiloyork': 280, 'Sinaloa': 280, 'Guanajuato': 135},
    'Zacatecas': {'Sonora': 250, 'Monterrey': 346, 'Queretaro': 370},
    'Sonora': {'Zacatecas': 250, 'Sinaloa': 394},
    'Oaxaca': {'Queretaro': 491, 'CDMX': 491},
    'Tamaulipas': {'Queretaro': 356, 'CDMX': 356},
    'Guanajuato': {'Aguascalientes': 160, 'Celaya': 135},
}

def buscar_solucion_USC(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)
    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar la lista de nodos frontera por costo acumulado.
        nodos_frontera = sorted(nodos_frontera, key=lambda nodo: nodo.get_costo())
        nodo = nodos_frontera[0]
        # Extraer el nodo y añadirlo a visitados.
        nodos_visitados.append(nodos_frontera.pop(0))

        if nodo.get_datos() == solucion:
            # Solucion encontrada.
            solucionado = True
            return nodo
        else:

            # Expandir los nodos hijos (ciudades con conexion).
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                costo = conexiones[dato_nodo][un_hijo]
                hijo.set_costo(nodo.get_costo() + costo)
                hijo.set_padre(nodo)  # ← necesario para reconstruir ruta
                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados):
                    # Si esta en la lista se sustituye con
                    # el nuevo valos del costo si es menor.
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    estado_inicial_demo = 'Jiloyork'
    solucion_demo = 'Monterrey'
    nodo_solucion = buscar_solucion_USC(CONEXIONES, estado_inicial_demo, solucion_demo)
    # Mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() != None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial_demo)
    resultado.reverse()
    print("Ruta encontrada:", resultado)
    print("Costo total:", nodo_solucion.get_costo())

    # JILOYORK, CDMX, QUERETARO, MONTERREY
