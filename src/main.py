from menu import Menu
from leituraArquivos import leituraGrafo


while True:
    
    print()
    nomeArquivo = str(input("Digite o nome do arquivo que contém o grafo: "))
    grafo = leituraGrafo(nomeArquivo)

    if grafo is not None:
        menu = Menu()

        menu.representacao()
        menu.insercaoRemocao()
        menu.verificacoes()
        menu.arvores()
        menu.algoritmos()


