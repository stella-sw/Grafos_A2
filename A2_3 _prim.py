import sys
import grafo_ndir_pond as G_bib
import heapq

arquivo = sys.argv[1]
origem = int(sys.argv[2])

grafo = G_bib.Grafo(arquivo=arquivo)


def prim(grafo, inicio=1):
    num_vertices = grafo.qtdVertices()

    visitado = [False] * (num_vertices + 1)

    fila = []

    # Começamos pelo vértice escolhido
    visitado[inicio] = True

    # Coloca as arestas do vértice inicial na fila
    for v in grafo.vizinhos(inicio):
        peso = grafo.peso(inicio, v)
        heapq.heappush(fila, (peso, inicio, v))

    arvore = []
    peso_total = 0.0

    while fila and len(arvore) < num_vertices - 1:

        peso, u, v = heapq.heappop(fila)

        # Se os dois já estão na árvore, essa aresta
        # não serve
        if visitado[v]:
            continue

        # Adiciona a aresta
        visitado[v] = True
        arvore.append((u, v, peso))
        peso_total += peso

        # Adiciona novas arestas que saem de v
        for w in grafo.vizinhos(v):
            if not visitado[w]:
                peso_vw = grafo.peso(v, w)
                heapq.heappush(
                    fila,
                    (peso_vw, v, w)
                )

    return peso_total, arvore

def imprimir_resultado(peso_total, arvore):

    print(peso_total)

    arestas_saida = []

    for u, v, peso in arvore:
        arestas_saida.append(f"{u}-{v}")

    print(", ".join(arestas_saida))

peso_total, arvore = prim(grafo)

imprimir_resultado(peso_total, arvore)