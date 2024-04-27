# Atividade-de-Implementacao-Algoritmos-em-Grafos

## Sobre o projeto 
Este é um projeto idealizado pelo Professor Douglas Aquino T. Mendes, docente da disciplina de Algoritmos em Grafos da Universidade Federal de Lavras (UFLA) - 2024/01, desenvolvido pelos alunos Guilherme Henrique Silva e Bruno de Almeida, que aborda os seguintes requisitos:

#### Objetivo

Implementar algoritmos para análise de propriedades de grafos, avançando gradualmente à medida que a disciplina progride.

### Descrição

1. Os alunos serão desafiados a implementar um sistema
modular para análise de propriedades de grafos armazenados em arquivos de texto. A implementação será progressiva, com novas funcionalidades adicionadas conforme o avanço da disciplina. A estrutura básica consistirá em um menu interativo onde o usuário poderá selecionar a propriedade do grafo que desejam analisar; 

2. Os alunos são livres para decidir a linguagem de programação a ser utilizada;

3. Os alunos possuem 60 dias para implementar as funções sugeridas, e são livres para adicionar qualquer outra a qual considere relevante/interessante; 

4. Todas as funções devem possuir um comentário javadoc
   - /** Essa função recebe a entrada em tal formato e responde tal coisa */
     - https://pt.stackoverflow.com/questions/6733/para-que-serve-o-c%C3%B3digo-na-lingu
      agem-java;

 ### Exemplo de uso
 
O grafo a ser analizado estará em um arquivo .txt, e deve ser representado como no exemplo a baixo, seguindo asregras de chaves ‘{‘ ‘}’ para representar o conjunto, efinalizar com ponto e virgula ‘;’, as arestas só precisam ser representadas uma vez em caso de grafos bidirecionais:
V = {1,2,3,4,5}; A = {(1,2),(2,3),(3,1),(4,5)};
Onde V são os vértices e A são as arestas do grafo. Essa padronização será importante para os testes de avaliação.

### Etapas
a. Implementação básica:
   - O programa deve perguntar se o grafo é direcionado ou não.
     - Caso seja não direcionado, o programa deve adicionar as arestas.
   - O programa deve fazer a leitura de um arquivo .txt:
     - Identificar os vértices e arestas.
     - Retornar erro caso algo esteja incorreto na representação do grafo no arquivo.
       Exemplos:
         i. V = { 1, 2; A = {};
         ii. V = {1,2,3,4}; A = {12, 34};
         iii. V = {1,2,3}; A = {(1,8)}.
   - O programa deve ser modular, e ao chamar cada função disponível no menu, o programa deve mostrar o tempo que levou para executar a função.
     - [Link para vídeo explicativo](https://www.youtube.com/watch?v=9GaDSKZ3sM4)
     - Para comparar a eficiência de algoritmos com resultados equivalentes, como BFS e DFS em grafos esparsos e densos.
### Menu

  a. Representações
  
    i. Matriz de Adjacência
    ii. Lista de Adjacência
    iii. (Desafio) Representação gráfica
       1. [Link para vídeo explicativo](https://www.youtube.com/watch?v=PfT8_2sKReo)
      
  b. Remoções e Inserções
  
    i. Arestas     
      1. Remover
       2. Adicionar
      
    ii. Vértices
       1. Remover
       2. Adicionar (Ao finalizar essas operações, o arquivo txt deve ser atualizado)
      
  c. Verificações
  
    i. Quantidade de vértices
    ii. Quantidade de arestas
    iii. Grau de um vértice
    iv. O grafo é conexo?
    v. O grafo é fortemente conexo? (Essa opção só deve aparecer caso o grafo seja direcionado)
    vi. O grafo possui ciclos?
    vii. O grafo é Euleriano? (A resposta deve ser Euleriano, Semi-Euleriano ou Não)
  
  d. Árvores
  
    i. Busca em Largura
    ii. Busca em Profundidade
    iii. Geradora mínima
       1. Kruskal
       2. Prim

  e. Algoritmos
  
    i. Ordenar topologicamente
       1. Kahn
       2. DFS para ordem topológica
    ii. Identificar componentes fortes
       1. Kosaraju

