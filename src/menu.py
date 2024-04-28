class Menu:

    def representacao(self):
        print('-'*34)
        print('Representações ')
        print('Digite: ')
        print('     (i) Matriz de Adjacência')
        print('     (ii) Lista de Adjacência')
        print('     (iii) Representação gráfica')
        print('-'*34)
        entrada = str(input())


       
    def insercaoRemocao(self):
        print('-'*24)
        print('Remoções e Inserções: ')
        print('Digite: ')
        print('     (i) Arestas')
        print('     (ii) Vértices')
        entrada = str(input())

        if entrada == 'i':
            print()
            print("Você escolheu manipular Arestas")
            print('Digite: ')
            print('     (1) Remover')
            print('     (2) Adicionar')
            print('-'*34)
            entrada2 = str(input())

        if entrada == 'ii':
            print()
            print("Você escolheu manipular Vértices")
            print('Digite: ')
            print('     (1) Remover')
            print('     (2) Adicionar')
            print('-'*34)
            entrada2 = str(input())

    def verificacoes(self):
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


        

    



