# Viaje por carretera por busqueda de costo uniforme
from arbol import Nodo

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
    CONEXIONES = {
        'Jiloyork': {'CDMX': 125, 'QRO': 513},
        'Morelos': {'QRO': 524},
        'CDMX': {'Jiloyork': 125, 'QRO': 423, 'Hidalgo': 491},
        'Hidalgo': {'CDMX': 491, 'QRO': 356, 'Mexicali': 309, 'MTY': 346},
        'QRO': {'SLP': 203, 'Morelos': 514, 'Jiloyork': 513, 'CDMX': 423, 'MTY': 603, 'Sonora': 437, 'Hidalgo': 356, 'Mexicali': 313, 'AGS': 599},
        'SLP': {'AGS': 390, 'QRO': 203, },
        'AGS': {'SLP': 390, 'QRO': 599},
        'Sonora': {'QRO': 437, 'Mexicali': 394,},
        'Mexicali': {'MTY': 296, 'Hidalgo': 309, 'QRO': 313, },
        'MTY': {'Mexicali': 296, 'QRO': 603, 'Hidalgo': 346},
    }

    estado_inicial = 'Jiloyork'
    solucion = 'AGS'
    nodo_solucion = buscar_solucion_USC(CONEXIONES, estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print("Ruta encontrada:", resultado)
    print("Costo total:", nodo_solucion.get_costo())

    # JILOYORK, QRO, SLP, AGS
    # COSOTO 1,106 KM
