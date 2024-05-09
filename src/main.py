from menu import Menu
from leituraArquivos import ManipulacaoArquivo

while True:

    print()
    nomeArquivo = str(input("Digite o nome do arquivo que contém o grafo: ").lower())
    manipulacao = ManipulacaoArquivo(nomeArquivo)
    vertices, arestas = manipulacao.leituraGrafo()

    if vertices is not None and arestas is not None:

        menu = Menu(vertices, arestas)

        menu.representacao(vertices, arestas)
        menu.insercaoRemocao(nomeArquivo)
        menu.verificacoes()
        menu.arvores()
        menu.algoritmos()

        break


