import networkx as nx
import matplotlib.pyplot as plt 

class RepresentacaoGrafica:
    def __init__(self, vertices, arestas, direcionado):
        self.vertices = vertices
        self.arestas = arestas
        if direcionado:
            self.representacao = nx.DiGraph()
        else:
            self.representacao = nx.Graph()

    def addAdjacencia(self):
       self.representacao.add_edges_from(self.arestas)

    def mostra(self):
        nx.draw(self.representacao, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)
    
        plt.show(block = False)

    def getVertices(self):
        return self.vertices
    
    
    def getArestas(self):
        return self.arestas

    def getGrau(self):
        grauVertice = int(input("\n Digite o vértice que deseja consultar o grau: "))
        grau = grauVertice-1

        return nx.degree(self.representacao, grau)