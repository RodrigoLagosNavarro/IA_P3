# ============================================================================
#  Rodrigo Lagos Navarro     23110148      6E
#  Simulador Árbol de Mínimo y Máximo coste con Kruskal (COMENTADO)
# ============================================================================

import math                     # Importamos la librería math para usar valores infinitos y trigonometría
import matplotlib.pyplot as plt  # Librería para graficar

INF = math.inf  # Representa ausencia de conexión entre nodos en la matriz

# ======================== CONSTRUIR LISTA DE ARISTAS ========================
def construir_aristas(G):
    aristas = []                # Lista donde guardaremos todas las aristas del grafo
    n = len(G)                  # Cantidad de nodos
    for u in range(n):          # Recorre filas
        for v in range(u+1, n): # Recorre columnas, evitando repetir aristas
            if G[u][v] != INF:  # Si existe una conexión válida
                aristas.append((G[u][v], u, v))  # Guardamos (peso, nodo u, nodo v)
    return aristas

# ============================== UNION-FIND ==================================
def find(p, x):
    # Busca el representante (raíz) del conjunto del nodo x
    if p[x] != x:               # Si no es su propio padre, seguimos buscando
        p[x] = find(p, p[x])    # Compresión de caminos
    return p[x]

def union(p, r, x, y):
    # Une los conjuntos que contienen a x y a y usando su rango
    rx, ry = find(p, x), find(p, y)  # Raíces de cada conjunto
    if rx == ry:               # Si ya están en el mismo conjunto, no hacemos nada
        return False
    if r[rx] < r[ry]:          # El de menor rango se conecta al de mayor
        p[rx] = ry
    elif r[rx] > r[ry]:
        p[ry] = rx
    else:                      # Si tienen el mismo rango, uno pasa a ser padre del otro
        p[ry] = rx
        r[rx] += 1             # Aumentamos el rango del nuevo padre
    return True

# ============================= KRUSKAL ======================================
def kruskal(G, L, minimo=True):
    n = len(G)                 # Número de nodos
    aristas = construir_aristas(G)  # Construimos la lista de aristas del grafo

    # Ordenamos las aristas dependiendo de si queremos mínimo o máximo costo
    aristas.sort(key=lambda x: x[0], reverse=not minimo)

    tipo = "MINIMO" if minimo else "MAXIMO"
    print(f"\n===== KRUSKAL {tipo} COSTE =====")
    print("Aristas ordenadas:")
    for w,u,v in aristas:
        print(f"  {L[u]} - {L[v]} : {w}")

    p = list(range(n))  # Lista de padres (cada nodo inicia siendo su propio padre)
    r = [0]*n           # Rangos de cada conjunto
    arbol = []          # Aquí guardaremos las aristas que sí entran al árbol
    total = 0           # Suma de pesos del árbol

    print("\nProceso paso a paso:")
    for w,u,v in aristas:                   # Recorremos las aristas en orden
        print(f"Considerando arista {L[u]} - {L[v]} (peso {w})...")
        if find(p, u) != find(p, v):        # Si no forman un ciclo
            union(p, r, u, v)               # Unimos sus conjuntos
            arbol.append((u, v, w))         # La aceptamos en el árbol
            total += w                      # Sumamos su peso
            print(f"  -> ACEPTADA. Coste acumulado = {total}")
        else:
            print(f"  -> RECHAZADA (formaría ciclo).")

    print(f"\nAristas elegidas para el árbol de {tipo} coste:")
    for u,v,w in arbol:
        print(f"  {L[u]} -- {w} --> {L[v]}")
    print(f"Coste total del árbol de {tipo} coste: {total}\n")

    return arbol

# ============================ DIBUJAR ÁRBOL =================================
def dibujar_kruskal(L, aristas, nombre_archivo, titulo):
    n = len(L)                                    # Cantidad de nodos
    ang = [2*math.pi*i/n for i in range(n)]       # Angulos para distribuir nodos en círculo
    pos = {i:(math.cos(ang[i]), math.sin(ang[i])) for i in range(n)}

    fig, ax = plt.subplots()                      # Creamos figura
    ax.set_aspect("equal")                       # Escala proporcional
    ax.axis("off")                               # Quitamos ejes

    # Dibujamos solo las aristas del árbol
    for u,v,w in aristas:
        x1,y1 = pos[u]; x2,y2 = pos[v]
        ax.plot([x1,x2],[y1,y2], linewidth=3)     # Línea de la arista
        xm,ym = (x1+x2)/2, (y1+y2)/2              # Punto medio para el peso
        ax.text(xm, ym, str(w), fontsize=9)

    # Dibujamos los nodos
    for i in range(n):
        x,y = pos[i]
        ax.scatter([x],[y], s=300)                # Nodo como punto grande
        ax.text(x, y, L[i], ha="center", va="center", fontsize=12)

    plt.title(titulo)
    plt.savefig(nombre_archivo)                   # Guardamos la imagen
    print(f"Grafico guardado como {nombre_archivo}")

# ========================= PROGRAMA PRINCIPAL ===============================
if __name__ == "__main__":
    L = ["A","B","C","D","E","F","G"]  # Etiquetas

    # Matriz de adyacencia del grafo (INF = sin conexión)
    G = [
        [INF,  2,   4, INF, INF, INF, INF],
        [2,  INF,   1,   7, INF, INF, INF],
        [4,    1, INF,   3,   5, INF, INF],
        [INF,  7,   3, INF,   6,   8, INF],
        [INF, INF,   5,   6, INF,   9,   4],
        [INF, INF, INF,   8,   9, INF,   2],
        [INF, INF, INF, INF,   4,   2, INF]
    ]

    arbol_min = kruskal(G, L, minimo=True)   # Árbol mínimo
    dibujar_kruskal(L, arbol_min, "kruskal_min.png", "Arbol de Minimo Coste (Kruskal)")

    arbol_max = kruskal(G, L, minimo=False)  # Árbol máximo
    dibujar_kruskal(L, arbol_max, "kruskal_max.png", "Arbol de Maximo Coste (Kruskal)")
