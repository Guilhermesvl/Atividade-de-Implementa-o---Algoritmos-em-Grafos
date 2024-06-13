from collections import deque

class LA:
    def __init__(self, vertices, arestas, direcionado):
        self.vertices = vertices
        self.arestas = arestas
        self.la = [[]  for _ in range(len(self.vertices))]
        self.direcionado = direcionado

    
    def addAdjacencia(self):
        setAdjacencias = [set() for _ in range(len(self.vertices))] #remover duplicatas

        for u, v in self.arestas:
            setAdjacencias[u-1].add(v-1)

            if not self.direcionado:
                setAdjacencias[v-1].add(u-1)
        
        #cconvertendo de volta para list
        self.la = [list(adj) for adj in setAdjacencias]


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
    
    
    def getGrau(self):
        grauVertice = int(input("\n Digite o vértice que deseja consultar o grau: "))
       
        grau = sum(1 for _ in self.la[grauVertice - 1])

        return grau
    
    def BFS(self):
        if self.direcionado:
            print("\nO grafo é direcionado, logo este teste não esta disponível")
            return False

        componente = 0
        visitados = [False] * len(self.vertices)
        fila = deque()

        for source in range(len(self.vertices)):
            if not visitados[source]:
                componente+=1
                visitados[source-1] = True
                fila.append(source)

                while fila:
                    u = fila.popleft()
                    for adjacencia in self.la[u]:
                        if not visitados[adjacencia]:
                            visitados[adjacencia] = True
                            fila.append(adjacencia)
            
        if componente > 1:
            print(f"\nO grafo não é conéxo, possui {componente} componentes.")            
            return False
        
        print("\nO grafo é conéxo")
        return True


