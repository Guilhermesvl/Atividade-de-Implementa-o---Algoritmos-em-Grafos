import os
import re 

class ManipulacaoArquivo:
    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo

    def leituraGrafo(self):
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
        diretorio_atual = os.path.dirname(__file__)  # Diretório atual do script
        caminho_arquivo = os.path.join(diretorio_atual, "..", "testes", self.nomeArquivo)
        
        novaAresta = str(input('Insira a(s) nova(s) Aresta(s) separadas por vírgula (x,y):  '))
        
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

        indiceA = conteudo.find('A = {')
        arestas = conteudo[indiceA:].strip()

        arestas = arestas[:-2]

        if arestas.endswith(','):
            novasArestas = arestas +  novaAresta + '};'
        else:
            novasArestas = arestas + ',' + novaAresta + '};'

        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo[:indiceA] + novasArestas)