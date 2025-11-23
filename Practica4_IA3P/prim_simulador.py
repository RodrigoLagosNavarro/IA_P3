# ============================================================================
#  Alumno: Rodrigo Lagos Navarro     
#  Reg: 23110148      
#  Grupo: 6E
#  Simulador del Arbol Parcial PRIM
# ============================================================================

import math
import matplotlib.pyplot as plt

INF = math.inf  # Representa ausencia de conexión


# ALGORITMO DE PRIM
def prim(G, L, s=0):
    n = len(G)               # número de nodos
    key = [INF]*n            # valores mínimos para conectar cada nodo
    pad = [None]*n           # padre de cada nodo en el MST
    mst = [False]*n          # si el nodo ya está dentro del MST
    key[s] = 0               # iniciamos desde el nodo s (A)

    print(f"Iniciando Prim en {L[s]}:\n")
    for it in range(n):      # se repite n veces (una por cada nodo)
        u = None
        mk = INF

        # Elegir el nodo con la key más pequeña que no esté en el MST
        for v in range(n):
            if not mst[v] and key[v] < mk:
                mk, u = key[v], v

        if u is None: break
        mst[u] = True        # metemos ese nodo al MST

        # Mostrar estado de la iteración
        print(f"Iteración {it+1}: elijo {L[u]} (key={mk})")
        print("  key   :", [f"{k:.1f}" if k!=INF else 'INF' for k in key])
        print("  padre :", [L[p] if p!=None else '-' for p in pad])

        # Revisar los vecinos de u y actualizar sus keys
        for v in range(n):
            w = G[u][v]
            if w != INF and not mst[v] and w < key[v]:
                print(f"    actualizo {L[v]}: {key[v]} -> {w}, padre -> {L[u]}")
                key[v], pad[v] = w, u
        print()

    # Mostrar el MST final
    print("Árbol Parcial Mínimo:")
    tot = 0
    for v in range(n):
        if pad[v] is not None:
            w = G[v][pad[v]]
            print(f"  {L[pad[v]]} -- {w} --> {L[v]}")
            tot += w
    print("Peso total:", tot)

    return pad



#DIBUJAR EL MST
def dibujar_mst(G, L, pad):
    n = len(G)
    
    # Posición circular para que los nodos se vean bonitos
    ang = [2*math.pi*i/n for i in range(n)]
    pos = {i:(math.cos(ang[i]), math.sin(ang[i])) for i in range(n)}

    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    # Dibujar todas las aristas del grafo
    for u in range(n):
        for v in range(u+1, n):
            if G[u][v] != INF:
                x1,y1 = pos[u]; x2,y2 = pos[v]
                ax.plot([x1,x2],[y1,y2])   # línea del grafo base

    # Dibujar las aristas que forman el MST en grueso
    for v in range(n):
        p = pad[v]
        if p is not None:
            x1,y1 = pos[p]; x2,y2 = pos[v]
            ax.plot([x1,x2],[y1,y2], linewidth=3)   # arista fuerte del MST
            xm,ym = (x1+x2)/2, (y1+y2)/2
            ax.text(xm, ym, str(G[p][v]), fontsize=9)   # peso de la arista

    # Dibujar nodos
    for i in range(n):
        x,y = pos[i]
        ax.scatter([x],[y], s=300)           # círculo
        ax.text(x,y, L[i], ha="center", va="center", fontsize=12)  # nombre del nodo

    plt.title("Árbol Parcial Mínimo (Prim)")
    plt.savefig("resultadoprim.png")  # guardamos la imagen
    print("\nGráfico guardado como resultadoprim.png")



#PROGRAMA PRINCIPAL
if __name__ == "__main__":

    # Nombres de los nodos
    L = ["A","B","C","D","E","F","G"]

    # Matriz de adyacencia con los pesos
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

    padres = prim(G, L)         # Ejecutar Prim
    dibujar_mst(G, L, padres)   # Dibujar y guardar imagen

