import sys
import grafo_ndir_pond as G_bib

arquivo = sys.argv[1]
origem = int(sys.argv[2])

grafo = G_bib.Grafo(arquivo=arquivo)


def find(pai, v):
    if pai[v] != v:
        pai[v] = find(pai, pai[v])
    return pai[v]

def union(pai, rank, u, v):
    raiz_u = find(pai, u)
    raiz_v = find(pai, v)

    if raiz_u == raiz_v:
        return False

    if rank[raiz_u] < rank[raiz_v]:
        pai[raiz_u] = raiz_v
    elif rank[raiz_u] > rank[raiz_v]:
        pai[raiz_v] = raiz_u
    else:
        pai[raiz_v] = raiz_u
        rank[raiz_u] += 1

    return True

def lista_arestas(grafo):
    arestas = []

    n = grafo.qtdVertices()

    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):

            if grafo.haAresta(u, v):
                peso = grafo.peso(u, v)
                arestas.append((peso, u, v))

    return arestas

def kruskal(grafo:G_bib.Grafo):
    num_vertices = grafo.qtdVertices()

    arestas = lista_arestas(grafo)

    # Ordena pelo peso
    arestas.sort()

    # Cada vértice começa em um conjunto diferente
    pai = [i for i in range(num_vertices + 1)]
    rank = [0] * (num_vertices + 1)

    arvore = []
    peso_total = 0.0

    for peso, u, v in arestas:

        if union(pai, rank, u, v):
            arvore.append((u, v, peso))
            peso_total += peso

            # Uma árvore geradora possui n - 1 arestas
            if len(arvore) == num_vertices - 1:
                break

    return peso_total, arvore

def imprimir_resultado(peso_total, arvore):

    print(peso_total)

    arestas_saida = []

    for u, v, peso in arvore:
        arestas_saida.append(f"{u}-{v}")

    print(", ".join(arestas_saida))

peso_total, arvore = kruskal(grafo)

imprimir_resultado(peso_total, arvore)