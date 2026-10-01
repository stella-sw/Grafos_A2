from __future__ import annotations

class Grafo:
    def __init__(self, arquivo=None, num_vertices=None):
        if arquivo is not None:
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
                    u, v = line.split()
                    u = int(u)
                    v = int(v)
                    self.Adj[u][v].append(1)
        elif num_vertices is not None:
            self.Adj = [[[] for x in range (num_vertices+1)] for x in range(num_vertices+1)]
            self.V = ['']*(num_vertices+1)
        else:
            return
    def grafoTransposto(self) -> Grafo:
        num_vertices =self.qtdVertices() 
        grafo = Grafo(num_vertices=num_vertices)
        for u in range (1, num_vertices+1):
            for v in range(1, num_vertices+1):
                grafo.Adj[u][v] = self.Adj[v][u]
            grafo.V[u] = self.V[u]
        return grafo
    def qtdVertices(self):
        return (len(self.Adj)-1)
    def qtdArcos(self):
        num_arcos = 0
        num_vertices = self.qtdVertices()
        for u in range(1, num_vertices+1):
            for v in range(1, num_vertices+1):
                num_arcos += len(self.Adj[u][v])
        return num_arcos
    def grau(self, v):
        grau = 0
        for u in range(1, self.qtdVertices() + 1):
            grau += len(self.Adj[v][u])
        return grau
    def rotulo(self, v):
        return self.V[v]
    def vizinhos(self, v):
        return [u for u in range(1, self.qtdVertices() + 1) if self.haArco(v, u)]
    def haArco(self, u, v):
        return (len(self.Adj[u][v]) > 0)