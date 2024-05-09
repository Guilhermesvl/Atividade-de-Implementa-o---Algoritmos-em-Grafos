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


