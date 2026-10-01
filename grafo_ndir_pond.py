class Grafo:
    def __init__(self, arquivo):
        num_vertices = 0
        with open(arquivo, 'r') as file:
            num_vertices = int(file.readline().strip().split()[1])
            self.Adj = [[[] for x in range (num_vertices+1)] for x in range(num_vertices+1)]
            self.V = ['']*(num_vertices+1)
            for i in range(num_vertices):
                num, rotulo = file.readline().strip().split(maxsplit=1)
                num = int(num)
                self.V[num] = rotulo
            file.readline()
            for line in file:
                line = line.strip()
                if not line:
                    continue
                u, v, w = line.split()
                u = int(u)
                v = int(v)
                w = float(w)
                self.Adj[u][v].append(w)
                self.Adj[v][u].append(w)
    def qtdVertices(self):
        return (len(self.Adj)-1)
    def qtdArestas(self):
        num_arestas = 0
        num_vertices = self.qtdVertices()
        for u in range(1, num_vertices+1):
            for v in range(u + 1, num_vertices+1):
                num_arestas += len(self.Adj[u][v])
        return num_arestas
    def grau(self, v):
        grau = 0
        for u in range(1, self.qtdVertices() + 1):
            grau += len(self.Adj[v][u])
        return grau
    def rotulo(self, v):
        return self.V[v]
    def vizinhos(self, v):
        return [u for u in range(1, self.qtdVertices() + 1) if self.haAresta(v, u)]
    def haAresta(self, u, v):
        return (len(self.Adj[u][v]) > 0)
    def peso(self, u, v):
        if self.haAresta(u, v):
            return min(self.Adj[u][v])
        return float('inf')