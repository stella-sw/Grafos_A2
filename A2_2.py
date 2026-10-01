import sys
from collections import deque
import grafo_dir_npond as G_bib

arquivo = sys.argv[1]

grafo = G_bib.Grafo(arquivo=arquivo)


def dfs_OT(grafo: G_bib.Grafo):
    C = [False] * (grafo.qtdVertices() + 1)
    T = [float('inf')] * (grafo.qtdVertices() + 1)
    F = [float('inf')] * (grafo.qtdVertices() + 1)

    tempo = [0]

    O = []

    for u in range(1, grafo.qtdVertices() + 1):
        if not C[u]:
            dfs_visit_OT(grafo, u, C, T, F, tempo, O)

    return O


def dfs_visit_OT(grafo: G_bib.Grafo, v, C, T, F, tempo, O):
    C[v] = True

    tempo[0] += 1
    T[v] = tempo[0]

    for u in grafo.vizinhos(v):
        if not C[u]:
            dfs_visit_OT(grafo, u, C, T, F, tempo, O)

    tempo[0] += 1
    F[v] = tempo[0]
    O.insert(0, grafo.V[v])


ordenacao = dfs_OT(grafo=grafo)

print(" , ".join(map(str, ordenacao)))