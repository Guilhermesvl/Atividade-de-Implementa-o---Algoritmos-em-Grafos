from menu import Menu
from leituraArquivos import leituraGrafo

nomeArquivo = str(input("Digite o nome do arquivo que contém o grafo: "))
grafo = leituraGrafo(nomeArquivo)

menu = Menu()

menu.representacao()
menu.insercaoRemocao()
menu.verificacoes()
menu.arvores()
menu.algoritmos()
