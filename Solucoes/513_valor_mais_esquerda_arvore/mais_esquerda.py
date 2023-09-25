from collections import deque
import re

def criar_grafo(arvore: list) -> dict:
    grafo = {}

    for vertices in arvore:
        if vertices not in grafo and vertices != 'null':
            grafo[vertices] = []
        
    for vertices in range(len(arvore)):
        if arvore[vertices] == 'null':
            continue
        if vertices > 0 and arvore[vertices - 1] == 'null':
            if ((2*(vertices-1))+1) < (len(arvore)):
                grafo[arvore[vertices]].append(arvore[(2*(vertices-1))+1])
                grafo[arvore[(2*(vertices-1))+1]].append(arvore[vertices])
            if ((2*(vertices-1))+2) < (len(arvore)):
                grafo[arvore[vertices]].append(arvore[(2*(vertices-1))+2])
                grafo[arvore[(2*(vertices-1))+2]].append(arvore[vertices])
        else:
            if ((2*vertices)+1) < (len(arvore)) and arvore[((2*vertices)+1)] != 'null':
                grafo[arvore[vertices]].append(arvore[(2*vertices)+1])
                grafo[arvore[(2*vertices)+1]].append(arvore[vertices])
            if ((2*vertices)+2) < (len(arvore)) and arvore[((2*vertices)+2)] != 'null':
                grafo[arvore[vertices]].append(arvore[(2*vertices)+2])
                grafo[arvore[(2*vertices)+2]].append(arvore[vertices])

    return grafo

def bfs(grafo: dict, raiz: str) -> list:
    visitados = set()
    fila = deque()
    niveis = [] 
    sub =[]
    conta_nivel = 0

    fila.append(raiz)
    visitados.add(raiz)
    sub.append(raiz)
    niveis.append(sub)
    
    conta_nivel += 1 

    while fila:
        vertice = fila.popleft()
        sub = []
        
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)
                sub.append(vizinho)
        
        if vertice not in niveis[conta_nivel -1]:
            niveis[conta_nivel -1] += sub
        else:
            niveis.append(sub)
            conta_nivel += 1 

    
    return niveis

def main():
    
    entrada = str(input())
    arvore = re.findall(r'\[(.*?)\]', entrada)[0].split(',')
    grafo = criar_grafo(arvore)
    niveis = bfs(grafo, arvore[0])

    print(niveis[-2][0])


main()
