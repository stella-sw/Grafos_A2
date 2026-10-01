import sys
import A1_1 as G_bib

arquivo = sys.argv[1]

grafo = G_bib.Grafo(arquivo=arquivo)

def floyd_warshall(grafo: G_bib.Grafo):
    num_vertices = grafo.qtdVertices()
    D = [[float('inf') for x in range (num_vertices+1)] for x in range(num_vertices+1)]
    PI = [[None for x in range (num_vertices+1)] for x in range(num_vertices+1)]
    for u in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            if (u == v):
                D[u][v] = 0
            else:
                D[u][v] = grafo.peso(u, v)
                PI[u][v] = u
    for k in range(1, num_vertices + 1):
        for u in range(1, num_vertices + 1):
            for v in range(1, num_vertices + 1):
                if (D[u][v] > D[u][k] + D[k][v]):
                    D[u][v] = D[u][k] + D[k][v]
                    PI[u][v] = PI[k][v]
    return (D, PI)

distancias, ancestrais = floyd_warshall(grafo=grafo)

for u in range(1, grafo.qtdVertices() + 1):
    valores = []

    for v in range(1, grafo.qtdVertices() + 1):
        distancia = distancias[u][v]

        if distancia == float('inf'):
            valores.append("inf")
        elif distancia == int(distancia):
            valores.append(str(int(distancia)))
        else:
            valores.append(str(distancia))

    print(f'{u}:{",".join(valores)}')