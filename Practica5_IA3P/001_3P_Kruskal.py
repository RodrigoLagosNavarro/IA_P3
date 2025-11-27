# ============================================================================
#  Rodrigo Lagos Navarro     23110148      6E
#  Simulador Árbol de Mínimo y Máximo coste con Kruskal
# ============================================================================

import math
import matplotlib.pyplot as plt

INF = math.inf  # valor para indicar que no hay arista en la matriz


# ======================== CONSTRUIR LISTA DE ARISTAS ========================
def construir_aristas(G):
    aristas = []
    n = len(G)
    for u in range(n):
        for v in range(u+1, n):     # u < v para no repetir aristas
            if G[u][v] != INF:
                aristas.append((G[u][v], u, v))  # (peso, u, v)
    return aristas


# ============================== UNION-FIND ==================================
def find(p, x):
    # Busca la raíz del conjunto de x (con compresión de caminos)
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, r, x, y):
    # Une los conjuntos de x e y usando rangos
    rx, ry = find(p, x), find(p, y)
    if rx == ry:
        return False
    if r[rx] < r[ry]:
        p[rx] = ry
    elif r[rx] > r[ry]:
        p[ry] = rx
    else:
        p[ry] = rx
        r[rx] += 1
    return True


# ============================= KRUSKAL ======================================
def kruskal(G, L, minimo=True):
    n = len(G)
    aristas = construir_aristas(G)

    # Ordenamos por peso: ascendente para mínimo, descendente para máximo
    aristas.sort(key=lambda x: x[0], reverse=not minimo)

    tipo = "MINIMO" if minimo else "MAXIMO"
    print(f"\n===== KRUSKAL {tipo} COSTE =====")
    print("Aristas ordenadas:")
    for w,u,v in aristas:
        print(f"  {L[u]} - {L[v]} : {w}")

    p = list(range(n))  # padre para Union-Find
    r = [0]*n           # rango
    arbol = []          # aristas escogidas
    total = 0

    print("\nProceso paso a paso:")
    for w,u,v in aristas:
        print(f"Considerando arista {L[u]} - {L[v]} (peso {w})...")
        if find(p, u) != find(p, v):
            union(p, r, u, v)
            arbol.append((u, v, w))
            total += w
            print(f"  -> ACEPTADA. Coste acumulado = {total}")
        else:
            print(f"  -> RECHAZADA (formaría ciclo).")
    print(f"\nAristas elegidas para el árbol de {tipo} coste:")
    for u,v,w in arbol:
        print(f"  {L[u]} -- {w} --> {L[v]}")
    print(f"Coste total del árbol de {tipo} coste: {total}\n")

    return arbol  # lista de (u, v, w)


# ============================ DIBUJAR ÁRBOL =================================
def dibujar_kruskal(L, aristas, nombre_archivo, titulo):
    n = len(L)
    ang = [2*math.pi*i/n for i in range(n)]
    pos = {i:(math.cos(ang[i]), math.sin(ang[i])) for i in range(n)}

    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    # Dibujar solo las aristas del árbol resultante
    for u,v,w in aristas:
        x1,y1 = pos[u]; x2,y2 = pos[v]
        ax.plot([x1,x2],[y1,y2], linewidth=3)
        xm,ym = (x1+x2)/2, (y1+y2)/2
        ax.text(xm, ym, str(w), fontsize=9)  # peso

    # Dibujar nodos
    for i in range(n):
        x,y = pos[i]
        ax.scatter([x],[y], s=300)
        ax.text(x,y, L[i], ha="center", va="center", fontsize=12)

    plt.title(titulo)
    plt.savefig(nombre_archivo)
    print(f"Grafico guardado como {nombre_archivo}")


# ========================= PROGRAMA PRINCIPAL ===============================
if __name__ == "__main__":
    # Etiquetas de los nodos
    L = ["A","B","C","D","E","F","G"]

    # Matriz de adyacencia del grafo (simétrica, no dirigido)
    G = [
        #A    B    C    D    E    F    G
        [INF,  2,   4, INF, INF, INF, INF], # A
        [2,  INF,   1,   7, INF, INF, INF], # B
        [4,    1, INF,   3,   5, INF, INF], # C
        [INF,  7,   3, INF,   6,   8, INF], # D
        [INF, INF,   5,   6, INF,   9,   4], # E
        [INF, INF, INF,   8,   9, INF,   2], # F
        [INF, INF, INF, INF,   4,   2, INF]  # G
    ]

    # Árbol de mínimo coste
    arbol_min = kruskal(G, L, minimo=True)
    dibujar_kruskal(L, arbol_min, "kruskal_min.png",
                    "Arbol de Minimo Coste (Kruskal)")

    # Árbol de máximo coste
    arbol_max = kruskal(G, L, minimo=False)
    dibujar_kruskal(L, arbol_max, "kruskal_max.png",
                    "Arbol de Maximo Coste (Kruskal)")
