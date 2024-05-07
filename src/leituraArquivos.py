import os
import re 

def leituraGrafo(nome_arquivo):
    diretorio_atual = os.path.dirname(__file__)  # Diretório atual do script
    caminho_arquivo = os.path.join(diretorio_atual, "..", "testes", nome_arquivo)
    
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


