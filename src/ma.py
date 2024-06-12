#from menu import Menu
from collections import deque

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

    def getVertices(self):
        return self.vertices
    
    
    def getArestas(self):
        return self.arestas
    
    
    def getGrau(self):
        grauVertice = int(input("\n Digite o vértice que deseja consultar o grau: "))

        grau = 0
        for adjacencias in self.ma[grauVertice-1]:
            if adjacencias == 1:
                grau+=1
            
        return grau
        

    def DFS(self):

        if  self.direcionado:
            print("\nO grafo é direcionado, logo este teste não esta disponível")
            return False
    
        componente = 0
        visitados = [False]  * len(self.vertices)
        
        if not visitados[0]:
            componente+=1
            self.DFSVISIT(1, visitados)
        
        for source in range(1, len(self.vertices)+1):
            if not visitados[source - 1]:
                componente+=1
                self.DFSVISIT(source, visitados)

        if componente > 1:
            print(f"\nO grafo não é conéxo, possui {componente} componentes.")
            return False
        
        print("\nO grafo é conéxo")
        return True


        
    def DFSVISIT(self, source, visitados):
        pilha = deque()

        visitados[source-1] = True
        pilha.append(source)

        while pilha:
            u = pilha.pop()
            
            for adjacente, adjacencia in enumerate(self.ma[u-1]):
                if adjacencia == 1 and not visitados[adjacente]:
                    pilha.append(adjacente + 1)
                    visitados[adjacente] = True





