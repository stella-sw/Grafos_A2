import sys
import grafo_dir_npond as G_bib

arquivo = sys.argv[1]
indice_s = int(sys.argv[2])

grafo = G_bib.Grafo(arquivo=arquivo)

def dfs(grafo: G_bib.Grafo):
    C = [False] * (grafo.qtdVertices() + 1)
    T = [float('inf')] * (grafo.qtdVertices() + 1)
    F = [float('inf')] * (grafo.qtdVertices() + 1)
    A = [None] * (grafo.qtdVertices() + 1)

    tempo = [0]

    for u in range(1, grafo.qtdVertices() + 1):
        if not C[u]:
            dfs_visit(grafo, u, C, T, A, F, tempo)

    return C, T, A, F

def dfs_visit(grafo: G_bib.Grafo, v, C, T, A, F, tempo):
    C[v] = True

    tempo[0] += 1
    T[v] = tempo[0]

    for u in grafo.vizinhos(v):
        if not C[u]:
            A[u] = v
            dfs_visit(grafo, u, C, T, A, F, tempo)

    tempo[0] += 1
    F[v] = tempo[0]

def dfs_visit_componente(grafo, v, C, T, A, F, tempo, componente):
    C[v] = True

    tempo[0] += 1
    T[v] = tempo[0]

    componente.append(v)

    for u in grafo.vizinhos(v):
        if not C[u]:
            A[u] = v
            dfs_visit_componente(grafo, u, C, T, A, F, tempo, componente)

    tempo[0] += 1
    F[v] = tempo[0]

def alg_Kosaraju_Sharir(grafo: G_bib.Grafo):
    # 1. DFS no grafo original
    C, T, A_linha, F = dfs(grafo)

    # 2. Criar o grafo transposto
    grafo_transposto = grafo.grafoTransposto()

    # 3. Ordenar os vértices pelo tempo de
    #    término da primeira DFS, do maior para o menor
    ordem = sorted(
        range(1, grafo.qtdVertices() + 1),
        key=lambda v: F[v],
        reverse=True
    )

    # 4. Segunda DFS no grafo transposto
    C_T = [False] * (grafo.qtdVertices() + 1)
    T_T = [float('inf')] * (grafo.qtdVertices() + 1)
    F_T = [float('inf')] * (grafo.qtdVertices() + 1)
    A_linha_T = [None] * (grafo.qtdVertices() + 1)

    tempo_T = [0]

    componentes = []

    for v in ordem:

        if not C_T[v]:

            componente = []

            dfs_visit_componente(
                grafo_transposto,
                v,
                C_T,
                T_T,
                A_linha_T,
                F_T,
                tempo_T,
                componente
            )

            componentes.append(componente)

    return componentes

componentes = alg_Kosaraju_Sharir(grafo)
for componente in componentes:
    print(",".join(map(str, componente)))