#from menu import Menu

class MA:
    def __init__ (self, vertices, arestas, direcionado):
        self.vertices = vertices
        self.arestas = arestas
        self.ma = [[0] * len(self.vertices) for _ in range(len(self.vertices))]
        self.direcionado = direcionado


    def addAdjacencia(self):
        for u, v in self.arestas:
            self.ma[u-1][v-1] = 1
            
            if not self.direcionado:
               self.ma[v-1][u-1] = 1


    def mostraMatriz(self):
        print()
        print('Matriz de Adjacência: ')
        for i in range(len(self.vertices)):
            print(self.ma[i])