import sys
import A1_1 as G_bib

arquivo = sys.argv[1]
origem = int(sys.argv[2])

grafo = G_bib.Grafo(arquivo=arquivo)


def algoritmoBellmanFord(grafo: G_bib.Grafo, origem):
    num_vertices = grafo.qtdVertices()

    D = [float('inf')] * (num_vertices + 1)
    A = [None] * (num_vertices + 1)

    D[origem] = 0

    for i in range(1, num_vertices):
        mudou = False # aplica a melhoria vista em prova

        for u in range(1, num_vertices + 1):
            for v in grafo.vizinhos(u):
                peso = grafo.peso(u, v)

                if D[u] != float('inf') and D[v] > D[u] + peso:
                    D[v] = D[u] + peso
                    A[v] = u
                    mudou = True
        
        if not mudou:
            break

    for u in range(1, num_vertices + 1):
        for v in grafo.vizinhos(u):
            peso = grafo.peso(u, v)

            if D[u] != float('inf') and D[v] > D[u] + peso:
                return False, None, None

    return True, D, A

# reconstroi o caminho
def caminho(A, origem, destino):
    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)

        if atual == origem:
            break

        atual = A[atual]

    caminho.reverse()

    if caminho[0] != origem:
        return []

    return caminho


resultado, D, A = bellmanFord(grafo, origem)

# estrutura o resultado no formato espeado pelo VPL
if resultado:
    for v in range(1, grafo.qtdVertices() + 1):
        if D[v] == float('inf'):
            print(f"{v}: d=inf")
        else:
            caminho_v = caminho(A, origem, v)
            caminho_str = ",".join(str(x) for x in caminho_v)
            print(f"{v}: {caminho_str}; d={D[v]:g}")
