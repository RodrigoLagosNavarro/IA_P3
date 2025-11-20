import heapq
import networkx as nx
import matplotlib.pyplot as plt

grafo = {
    'A': {'B': 2, 'D': 5},
    'B': {'C': 7, 'E': 1},
    'C': {},
    'D': {'E': 1},
    'E': {'C': 3}
}

NODO_INICIAL = 'A'

def dijkstra_con_pasos(grafo, inicio):
    dist = {n: float('inf') for n in grafo}
    prev = {n: None for n in grafo}
    dist[inicio] = 0
    visitados = set()
    heap = [(0, inicio)]
    paso = 0

    print("=== DIJKSTRA ===")
    print(f"Inicio: {inicio}\n")

    while heap:
        d_act, u = heapq.heappop(heap)
        if u in visitados:
            continue
        visitados.add(u)
        paso += 1

        print(f"--- Paso {paso} ---")
        print(f"Actual: {u} (dist = {d_act})")
        print(f"Visitados: {sorted(visitados)}")
        print("Distancias:")
        for n in sorted(grafo.keys()):
            d = dist[n]
            print(f"  {n}: {d if d != float('inf') else 'INF'}")
        print()

        for v, w in grafo[u].items():
            if v in visitados:
                continue
            nd = d_act + w
            if nd < dist[v]:
                print(f"  Mejora {v}: {dist[v]} -> {nd}")
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
        print()

    return dist, prev

def graficar(grafo, prev):
    G = nx.DiGraph()
    for u in grafo:
        for v, w in grafo[u].items():
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))  
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

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
    dist, prev = dijkstra_con_pasos(grafo, NODO_INICIAL)

    print("Distancias finales:")
    for n, d in dist.items():
        print(f"  {n}: {d if d != float('inf') else 'INF'}")

    graficar(grafo, prev)
