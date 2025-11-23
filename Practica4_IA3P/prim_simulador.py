import math
import matplotlib.pyplot as plt

INF = math.inf

def prim(G, L, s=0):
    n = len(G)
    key = [INF]*n
    pad = [None]*n
    mst = [False]*n
    key[s] = 0

    print(f"Iniciando Prim en {L[s]}:\n")
    for it in range(n):
        u = None
        mk = INF
        for v in range(n):
            if not mst[v] and key[v] < mk:
                mk, u = key[v], v

        if u is None: break
        mst[u] = True

        print(f"Iteración {it+1}: elijo {L[u]} (key={mk})")
        print("  key   :", [f"{k:.1f}" if k!=INF else 'INF' for k in key])
        print("  padre :", [L[p] if p!=None else '-' for p in pad])

        for v in range(n):
            w = G[u][v]
            if w != INF and not mst[v] and w < key[v]:
                print(f"    actualizo {L[v]}: {key[v]} -> {w}, padre -> {L[u]}")
                key[v], pad[v] = w, u
        print()

    print("Árbol Parcial Mínimo:")
    tot = 0
    for v in range(n):
        if pad[v] is not None:
            w = G[v][pad[v]]
            print(f"  {L[pad[v]]} -- {w} --> {L[v]}")
            tot += w
    print("Peso total:", tot)
    return pad

def dibujar_mst(G, L, pad):
    n = len(G)
    ang = [2*math.pi*i/n for i in range(n)]
    pos = {i:(math.cos(ang[i]), math.sin(ang[i])) for i in range(n)}

    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    # aristas del grafo
    for u in range(n):
        for v in range(u+1, n):
            if G[u][v] != INF:
                x1,y1 = pos[u]; x2,y2 = pos[v]
                ax.plot([x1,x2],[y1,y2])

    # aristas del MST
    for v in range(n):
        p = pad[v]
        if p is not None:
            x1,y1 = pos[p]; x2,y2 = pos[v]
            ax.plot([x1,x2],[y1,y2], linewidth=3)
            xm,ym = (x1+x2)/2, (y1+y2)/2
            ax.text(xm, ym, str(G[p][v]), fontsize=9)

    # nodos
    for i in range(n):
        x,y = pos[i]
        ax.scatter([x],[y], s=300)
        ax.text(x,y, L[i], ha="center", va="center", fontsize=12)

    plt.title("Árbol Parcial Mínimo (Prim)")
    plt.savefig("resultadoprim.png")     # <--- nuevo nombre
    print("\nGráfico guardado como resultadoprim.png")


if __name__ == "__main__":
    L = ["A","B","C","D","E","F","G"]

    # Puedes ajustar pesos como quieras:
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

    padres = prim(G, L)
    dibujar_mst(G, L, padres)
