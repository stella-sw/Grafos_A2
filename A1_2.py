import sys
from collections import deque
import A1_1 as G_bib

arquivo = sys.argv[1]
indice_s = int(sys.argv[2])

grafo = G_bib.Grafo(arquivo=arquivo)

def buscaLargura(grafo: G_bib.Grafo, origem):
    C = [False]*(grafo.qtdVertices() + 1)
    D = [float('inf')]*(grafo.qtdVertices() + 1)
    A = [None]*(grafo.qtdVertices() + 1)
    C[origem] = True
    D[origem] = 0
    Q = deque()
    Q.append(origem)
    print(f'0: {origem}')
    while (len(Q) > 0):
        nivel_atual = D[Q[0]]
        vertices_nivel = []

        while ((len(Q) > 0) and (D[Q[0]] == nivel_atual)):
            u = Q.popleft()
            for v in grafo.vizinhos(u):
                if (C[v] == False):
                    C[v] = True
                    D[v] = D[u] + 1
                    A[v] = u
                    Q.append(v)
                    vertices_nivel.append(v)
        if (len(vertices_nivel) > 0):
            print(f'{D[u] + 1}: {",".join(map(str, vertices_nivel))}')
    return (D, A)

D, A = buscaLargura(grafo, indice_s)