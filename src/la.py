class LA:
    def __init__(self, vertices, arestas, direcionado):
        self.vertices = vertices
        self.arestas = arestas
        self.la = [[]  for _ in range(len(self.vertices))]
        self.direcionado = direcionado

    
    def addAdjacencia(self):
        for u, v in self.arestas:
            self.la[u-1].append(v-1)

            if not self.direcionado:
                self.la[v-1].append(u-1)


    def mostraLista(self):
        for i in range(len(self.vertices)):
            print(f'{i + 1}: ', end = ' ')
            for j in self.la[i]:
                print(f'{j+1} -> ', end = '')
            print()

    def getVertices(self):
        return self.vertices
    
    
    def getArestas(self):
        return self.arestas