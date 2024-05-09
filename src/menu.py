from ma import MA
from la import LA
from representacaoGrafica import RepresentacaoGrafica
from leituraArquivos import ManipulacaoArquivo
import matplotlib.pyplot as plt 

class Menu:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas


    def direcionado(self):
        """
        Pergunta ao usuário se o grafo é direcionado e retorna booleano.

        :return: True se o grafo é direcionado, False caso não seja.
        :rtype: bool
        """
        print()
        print('-'*34)
        print('Antes de representarmos, me diga ')
        print('o Grafo é direcionado? (Sim/Não): ')

        direcionado = str(input().lower().replace('~', ''))
        
        if direcionado == 'sim':
            return True
        else:
            return False
        

    def representacao(self, vertices, arestas):
        """
        Permite que o usuário escolha entre as três tipos de representação sugeridas do grafo.

        :param vertices: Lista de vértices do grafo.
        :param arestas: Lista de arestas do grafo.
            * Para que sempre receba os vértices e arestas atualizados, 
                    caso o arquivo .txt seja modificado

        :return: Nenhum retorno.
        """
        print()
        print('-'*34)
        print('Representações ')
        print('Digite: ')
        print('     (i) Matriz de Adjacência')
        print('     (ii) Lista de Adjacência')
        print('     (iii) Representação gráfica')
        print('-'*34)
        entrada = str(input())

        if entrada == 'i':

            ma = MA(vertices, arestas, self.direcionado())
            ma.addAdjacencia()
            ma.mostraMatriz()

        if entrada == 'ii':

            la = LA(vertices, arestas, self.direcionado())
            la.addAdjacencia()
            la.mostraLista()

        if entrada == 'iii':
            plt.close()
            representacao = RepresentacaoGrafica(vertices, arestas, self.direcionado())
            representacao.addAdjacencia()
            representacao.mostra()

    


    def insercaoRemocao(self, nomeArquivo):
        """
        Permite que o usuário escolha fazer alterações nos vértices e arestas do arquivo texto.
        
        :return: Nenhum retorno.
        """
        print("\n\n")
        entradaAUX = str(input('Deseja fazer alterações nos vértices e/ou arestas? ').lower()
                             .replace('~', ''))
        if entradaAUX == 'sim':
        
            while True:
                print()
                print('-'*24)
                print('Remoções e Inserções: ')
                print('Digite: ')
                print('     (i) Arestas')
                print('     (ii) Vértices')
                print('     (iii) Encerrar operação')
                entrada = str(input())

                if entrada == 'i':
                    print()
                    print("Você escolheu manipular Arestas")
                    print('Digite: ')
                    print('     (1) Remover')
                    print('     (2) Adicionar')
                    print('-'*34)
                    entrada2 = str(input())

                    manipulaAresta = ManipulacaoArquivo(nomeArquivo)
                    
                    if entrada2 == '1':
                        manipulaAresta.removerAresta()
                        if encerrouInsercao():
                            vertices, arestas = manipulaAresta.leituraGrafo()
                            if vertices is not None and arestas is not None:
                                self.representacao(vertices, arestas)

                    if entrada2 == '2':
                        manipulaAresta.escreverAresta()
                        if encerrouInsercao():
                            vertices, arestas = manipulaAresta.leituraGrafo()
                            print(vertices, arestas)
                            if vertices is not None and arestas is not None:
                                self.representacao(vertices, arestas)
                            
                if entrada == 'ii':
                    print()
                    print("Você escolheu manipular Vértices")
                    print('Digite: ')
                    print('     (1) Remover')
                    print('     (2) Adicionar')
                    print('-'*34)
                    entrada2 = str(input())

                    manipulaVertice = ManipulacaoArquivo(nomeArquivo)

                    if entrada2 == '1':
                        manipulaVertice.removerVertice()
                        if  encerrouInsercao():
                            vertices, arestas = manipulaVertice.leituraGrafo()
                            if vertices is not None and arestas is not None:
                                self.representacao(vertices, arestas)

                    if entrada2 == '2':
                        manipulaVertice.escreverVertice()
                        if encerrouInsercao():
                            vertices, arestas = manipulaVertice.leituraGrafo()
                            if vertices is not None and arestas is not None:
                                self.representacao(vertices, arestas)
                        
                if entrada == 'iii':
                    print('Pŕoxima Operação: ')
                    break

    def verificacoes(self):
        print()
        print('-'*34)
        print('Verificações: ')
        print('Digite: ')
        print('     (i) Quantidade de vértices')
        print('     (ii) Quantidade de arestas')
        print('     (iii) Grau de um vértice')
        print('     (iv) O grafo é conexo?')
        print('     (v) O grafo é fortemente conexo?')
        print('     (vi) O grafo possui ciclos?')
        print('     (vii) O grafo é Euleriano?')
        print('-'*34)
        entrada3 = str(input())


    def arvores(self):
        print()
        print('-'*34)
        print('Árvores: ')
        print('Digite: ')
        print('     (i) Busca em Largura')
        print('     (ii) Busca em Profundidade')
        print('     (iii) Geradora Mínima')
        entrada4 = str(input())

        if entrada4 == 'iii':
            print('Digite: ')
            print('     (1) Kahn')
            print('     (2) Prim')

            entrada5 = str(input())
        print('-'*34)

    def algoritmos(self):
        print()
        print('-'*34)
        print('Algoritmos: ')
        print('Digite: ')
        print('     (i) Ordenar topologicamente')
        print('     (ii) Identificar componentes fortes')

        entrada6 = input()

        if entrada6 == 'i':
            print('Digite: ')
            print('     (1) Kahn')
            print('     (2) DFS para ordem topológica')

            entrada7 = input()

        elif entrada6 == 'ii':
            print('Digite: ')
            print('     (1) Kosaraju')

            entrada8 = input()

        print('-'*34)

def encerrouInsercao():
    '''
    Verifica se as inserções foram encerradas pelo usuário.
        *Foi criada para não ter que digitar a mesma coisa quatro vezes

    :return: True se as inserções foram encerradas, False caso contrário.
    :rtype: bool
    
    '''
    print()
    encerrou = str(input('As inserções já acabaram? (Sim/Não): ').lower().replace('~', ''))

    if encerrou == 'nao':
        return False
    else: 
        return True   

    



