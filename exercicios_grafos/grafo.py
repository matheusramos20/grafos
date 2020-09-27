from operator import itemgetter
import collections

arquivo = open('texto.txt', 'r')


lista_adj = []
grafo = dict()

for linha in arquivo:
    linha = linha.strip()#ou .replace()
    vertices = linha.split(';')
    vertice1 = vertices[0]
    vertice2 = vertices[1]
    #print(vertices)
    if not vertice1 in grafo:
        grafo[vertice1] = list()
    grafo[vertice1].append(vertice2)
    
    if not vertice2 in grafo:
        grafo[vertice2] = list()
    grafo[vertice2].append(vertice1)    

grafo =collections.OrderedDict(sorted(grafo.items()))
print(grafo)

visitados = []
ordem = []

def busca_profunda(vertice):
    if vertice in visitados:
        return
    
    visitados.append(vertice)
    ordem.append(vertice)
    lista_adj = grafo[vertice]
    for adjacente in lista_adj:
        busca_profunda(adjacente)

for vertice in grafo:
    busca_profunda(vertice) 


print(f"Busca em profundidade: {ordem}")


arquivo.close()