import os
import re 

class ManipulacaoArquivo:
    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo

    def leituraGrafo(self):
        """
        Lê os vértices e arestas de um arquivo de texto e os retorna.

            * retornando None, caso a leitura não seja bem
            executada, para que o programa permita que o Menu
            continue em execução até o usuário digitar um .txt válido


        :return: uma tupla separada para os vértices e arestas do grafo.
        :rtype: tuple
        :param b: O segundo número a ser somado.
        :raises FileNotFoundError: Se o arquivo não for encontrado.
        :raises ValueError: Se o formato do arquivo for inválido.
        """

        diretorio_atual = os.path.dirname(__file__)  # Diretório atual do script
        caminho_arquivo = os.path.join(diretorio_atual, "..", "testes", self.nomeArquivo)
        
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()

            # Encontrando vértices
            vertices_match = re.search(r'V\s*=\s*{([^}]*)}', conteudo)
            if vertices_match:
                vertices_str = vertices_match.group(1)
                vertices = [int(v) for v in vertices_str.split(',')]
            else:
                raise ValueError("Formato de vértices inválido")

            # Encontrando arestas
            arestas_match = re.search(r'A\s*=\s*{([^}]*)}', conteudo)
            if arestas_match:
                arestas_str = arestas_match.group(1)
                arestas = re.findall(r'\((\d+),(\d+)\)', arestas_str)
                arestas = [(int(a[0]), int(a[1])) for a in arestas]
            else:
                raise ValueError("Formato de arestas inválido")

            
            print("Informações lidas: ")
            print('Vértices: ', vertices)
            print('Arestas: ', arestas)

            return vertices, arestas
            
        
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado.")
            return None, None
        except ValueError as e:
            print("Erro:", e)
            return None, None
        


    def escreverAresta(self):
        """
        Adiciona uma nova aresta ao arquivo de grafo.

        :raises FileNotFoundError: Se o arquivo não for encontrado.
        """
         
        diretorio_atual = os.path.dirname(__file__)  # Diretório atual do script
        caminho_arquivo = os.path.join(diretorio_atual, "..", "testes", self.nomeArquivo)
        
        novaAresta = str(input('Insira a(s) nova(s) Aresta(s) separadas por vírgula (x,y):  '))
        
        #Abre o arquivo e armazena o conteúdo do arquivo na variável
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

        #Encontrando a parte do arquivo que corresponde as Arestas
        indiceA = conteudo.find('A = {')
        arestas = conteudo[indiceA:].strip()

        #Remove os dois últimos elementos: };
        arestas = arestas[:-2]

        #Escreve as novas Arestas
        if arestas.endswith(','):
            novasArestas = arestas +  novaAresta + '};'
        else:
            novasArestas = arestas + ',' + novaAresta + '};'

        #Abre o arquivo para escrever
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo[:indiceA] + novasArestas)
        

    def removerAresta(self):
        """
        Remove uma aresta de cada vez do arquivo de grafo.

        :raises FileNotFoundError: Se o arquivo não for encontrado.
        """
        
        diretorio_atual = os.path.dirname(__file__)  # Diretório atual do script
        caminho_arquivo = os.path.join(diretorio_atual, "..", "testes", self.nomeArquivo)

        #Abre o arquivo e armazena o conteúdo do arquivo na variável        
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        
        removeAresta = str(input('Digite a aresta que deseja remover (x,y): '))
        
        #Encontrando a parte do arquivo que corresponde as Arestas
        indiceA = conteudo.find('A = {')
        arestas = conteudo[indiceA:].strip()

        #Encontrando a aresta para apagar
        arestas = arestas.replace(removeAresta + ',', '') 
        arestas = arestas.replace(',' + removeAresta, '')

        #Abre o arquivo para escrever 
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo[:indiceA] + arestas)
        

    def escreverVertice(self):
        """
        Adiciona novo(s) vértice(s) ao arquivo de grafo.

        :raises FileNotFoundError: Se o arquivo não for encontrado.
        """
         
        diretorio_atual = os.path.dirname(__file__)  # Diretório atual do script
        caminho_arquivo = os.path.join(diretorio_atual, "..", "testes", self.nomeArquivo)
        
        novoVertice = str(input('Insira o(s) novo(s) Vértice(s) separados por vírgula x,:  '))
        
        #Abre o arquivo e armazena o conteúdo do arquivo na variável
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

        #Encontrando a parte do arquivo que corresponde os Vértices
        indiceA = conteudo.find('A = {')
        arestas = conteudo[indiceA:].strip()

        indiceV = conteudo.find('V = {')
        vertices = conteudo[:indiceA-1].strip()

        #Remove os dois últimos elementos: };
        vertices = vertices[:-2]

        #Escreve as novos Vértices
        if vertices.endswith(','):
            novosVertices = vertices +  novoVertice + '}; '
        else:
            novosVertices = vertices + ',' + novoVertice + '}; '

        print(conteudo[:indiceV] + novosVertices)

        #Abre o arquivo para escrever
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo[:indiceV] + novosVertices + arestas + ' ') 

        