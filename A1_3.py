import sys
from collections import deque
import A1_1 as G_bib

arquivo = sys.argv[1]

grafo = G_bib.Grafo(arquivo=arquivo)


def hierholzer(grafo: G_bib.Grafo):
    if grafo.qtdArestas() == 0:
        return True, []

    num_vertices = grafo.qtdVertices()

    C = [[0 for x in range(num_vertices + 1)] for x in range(num_vertices + 1)]

    for u in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            C[u][v] = len(grafo.Adj[u][v])

    for u in range(1, num_vertices + 1):
        if grafo.grau(u) % 2 != 0:
            return False, None

    inicio = None

    for k in range(1, num_vertices + 1):
        if grafo.grau(k) > 0:
            inicio = k
            break

    visitados = [False] * (num_vertices + 1)
    fila = [inicio]
    visitados[inicio] = True

    while len(fila) > 0:
        u = fila.pop()

        for v in grafo.vizinhos(u):
            if not visitados[v]:
                visitados[v] = True
                fila.append(v)

    for u in range(1, num_vertices + 1):
        if grafo.grau(u) > 0 and not visitados[u]:
            return False, None

    r, Ciclo = buscarSubciclo(grafo, inicio, C)

    if r == False:
        return False, None

    for u in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            if C[u][v] > 0:
                return False, None

    return True, Ciclo


def buscarSubciclo(grafo: G_bib.Grafo, v, C):
    Ciclo = [v]
    t = v

    while True:
        u = None

        for w in grafo.vizinhos(v):
            if C[v][w] > 0:
                u = w
                break

        if u is None:
            return False, None

        C[v][u] -= 1
        C[u][v] -= 1

        v = u
        Ciclo.append(v)

        if v == t:
            break

    Ciclo_original = Ciclo.copy()

    for u in Ciclo_original:
        for w in grafo.vizinhos(u):
            if C[u][w] > 0:
                r, Ciclo_interno = buscarSubciclo(grafo, u, C)

                if r == False:
                    return False, None

                posicao = Ciclo.index(u)

                for x in Ciclo_interno[1:]:
                    Ciclo.insert(posicao + 1, x)
                    posicao += 1

    return True, Ciclo


resultado, ciclo = hierholzer(grafo)

if resultado:
    print(1)
    print(",".join(map(str, ciclo)))
else:
    print(0)
