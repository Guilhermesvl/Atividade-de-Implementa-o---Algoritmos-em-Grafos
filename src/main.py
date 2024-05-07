from menu import Menu
from leituraArquivos import leituraGrafo

while True:

    print()
    nomeArquivo = str(input("Digite o nome do arquivo que contém o grafo: "))
    vertices, arestas = leituraGrafo(nomeArquivo)

    if vertices is not None and arestas is not None:

        menu = Menu(vertices, arestas)

        #menu.direcionado()
        menu.representacao()
        menu.insercaoRemocao()
        menu.verificacoes()
        menu.arvores()
        menu.algoritmos()


