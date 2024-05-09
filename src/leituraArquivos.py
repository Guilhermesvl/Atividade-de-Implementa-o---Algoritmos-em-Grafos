import os
import re 

class ManipulacaoArquivo:
    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo

    def leituraGrafo(self):
        """
        Lê os vértices e arestas de um arquivo de texto e os retorna.

        :return: Uma tupla separada para os vértices e arestas do grafo.
        :rtype: tuple
        :raises FileNotFoundError: Se o arquivo não for encontrado.
        :raises ValueError: Se o formato do arquivo for inválido ou se houver vértices ou arestas duplicadas.
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
                vertices = list(set([int(v) for v in vertices_str.split(',')]))
                if len(vertices) != len(vertices_str.split(',')):
                    raise ValueError("Vértices duplicados encontrados")
            else:
                raise ValueError("Formato de vértices inválido")

            # Encontrando arestas
            arestas_match = re.search(r'A\s*=\s*{([^}]*)}', conteudo)
            if arestas_match:
                arestas_str = arestas_match.group(1)
                arestas = re.findall(r'\((\d+),(\d+)\)', arestas_str)
                arestas = [(int(a[0]), int(a[1])) for a in arestas]
                
                # Verificar se todas as arestas são únicas
                if len(set(arestas)) != len(arestas):
                    raise ValueError("Arestas duplicadas encontradas")

                # Verificar se todos os vértices nas arestas foram definidos
                vertices_set = set(vertices)
                for a in arestas:
                    if a[0] not in vertices_set or a[1] not in vertices_set:
                        raise ValueError("Aresta contém vértice não definido")

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

    
    def removerVertice(self):
        """
        Remove um vértice de cada vez do arquivo de grafo.

        :raises FileNotFoundError: Se o arquivo não for encontrado.
        """
        
        diretorio_atual = os.path.dirname(__file__)  # Diretório atual do script
        caminho_arquivo = os.path.join(diretorio_atual, "..", "testes", self.nomeArquivo)

        #Abre o arquivo e armazena o conteúdo do arquivo na variável        
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        
        removeVertice = str(input('Digite o vértice que deseja remover x: '))
        #Encontrando a parte do arquivo que corresponde aos Vértices
        indiceVInicio = conteudo.find('V = {')
        indiceVFim = conteudo.find('}', indiceVInicio)

        #Encontrando a parte do arquivo que corresponde as Arestas
        indiceAInicio = conteudo.find('A = {')
        indiceVFim = conteudo.find('}', indiceAInicio)

        arestas = conteudo[indiceAInicio:indiceAInicio + 1]           
        vertices = conteudo[indiceVInicio:indiceVFim + 1]

        #Encontrando o vértice para apagar
        vertices = vertices.replace(removeVertice + ',', '') 
        vertices = vertices.replace(',' + removeVertice, '')

        #Abre o arquivo para escrever 
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo[:indiceVInicio] + vertices + conteudo[indiceAInicio:])