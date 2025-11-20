# ==========================================================
# Alumno: Rodrigo Lagos Navarro
# Registro: 23110148
# Grupo: 6E
# Practica 3 Algoritmo de Dijkstra
# ==========================================================

import heapq                 # Para usar una cola de prioridad (mínimo primero)
import networkx as nx        # Para graficar el grafo
import matplotlib.pyplot as plt

# Definición del grafo como diccionario: cada nodo tiene sus vecinos y pesos
grafo = {
    'A': {'B': 2, 'D': 5},
    'B': {'C': 7, 'E': 1},
    'C': {},
    'D': {'E': 1},
    'E': {'C': 3}
}

NODO_INICIAL = 'A'          # Nodo desde donde empieza Dijkstra

def dijkstra_con_pasos(grafo, inicio):
    dist = {n: float('inf') for n in grafo}   # Distancias iniciales infinitas
    prev = {n: None for n in grafo}           # Para guardar el camino
    dist[inicio] = 0                          # Distancia al inicio es 0
    visitados = set()                         # Conjunto de nodos ya visitados
    heap = [(0, inicio)]                      # Cola de prioridad con tupla (dist, nodo)
    paso = 0

    print("=== DIJKSTRA ===")
    print(f"Inicio: {inicio}\n")

    while heap:                                # Mientras haya nodos por procesar
        d_act, u = heapq.heappop(heap)         # Saca el nodo con menor distancia
        if u in visitados:                     # Si ya fue visitado, lo ignora
            continue
        visitados.add(u)                       # Marca como visitado

        print(f"Actual: {u} (dist = {d_act})")
        print(f"Visitados: {sorted(visitados)}")
        print("Distancias:")
        for n in sorted(grafo.keys()):
            d = dist[n]
            print(f"  {n}: {d if d != float('inf') else 'INF'}")
        print()

        # Explora los vecinos del nodo actual
        for v, w in grafo[u].items():
            if v in visitados:
                continue
            nd = d_act + w                     # Nueva distancia tentativa
            if nd < dist[v]:                   # Si encontramos una mejor ruta
                print(f"  Mejora {v}: {dist[v]} -> {nd}")
                dist[v] = nd                   # Actualiza distancia
                prev[v] = u                    # Guarda el nodo anterior
                heapq.heappush(heap, (nd, v))  # SE meto en la cola de prioridad
        print()

    return dist, prev

def graficar(grafo, prev):
    G = nx.DiGraph()                            # Crea un grafo dirigido
    for u in grafo:
        for v, w in grafo[u].items():           # Agrega aristas con sus pesos
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)          # Layout para dibujarlo
    plt.figure(figsize=(10, 7))
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)  # Muestra los pesos

    # Dibuja en color rojo las aristas del árbol de caminos más cortos
    aristas_arbol = [(p, n) for n, p in prev.items() if p is not None]
    nx.draw_networkx_edges(
        G, pos,
        edgelist=aristas_arbol,
        width=3,
        edge_color="red",
        arrowstyle="->",
        arrowsize=25
    )

    plt.title("Dijkstra - Árbol de caminos más cortos")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    dist, prev = dijkstra_con_pasos(grafo, NODO_INICIAL)  # Ejecuto Dijkstra

    print("Distancias finales:")
    for n, d in dist.items():                             # Imprime resultados
        print(f"  {n}: {d if d != float('inf') else 'INF'}")

    graficar(grafo, prev)                                 # Dibuja el grafo final
