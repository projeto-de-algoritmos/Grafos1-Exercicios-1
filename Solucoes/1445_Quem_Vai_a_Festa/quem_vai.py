import re

def criar_grafo() -> dict:
    grafo = {}

    str_pares = str(input())
    arestas = re.findall(r"[0-9]*,[0-9]*", str_pares)
    

    for aresta in arestas:
        inicio, fim = aresta.split(',')
        if inicio not in grafo:
            grafo[inicio] = []
        if fim not in grafo:
            grafo[fim] = []
        
        grafo[inicio].append(fim)
        grafo[fim].append(inicio) 

    return grafo

def dfs(grafo : dict, visitados : set, componente : list, vertice : set):
    
    if vertice not in visitados:
        visitados.add(vertice)
        componente.append(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs(grafo, visitados, componente, vizinho)

def vertices_conect(grafo : dict) -> list:
    
    visitados = set()
    componentes = []
    
    for vertice in grafo:
        if vertice not in visitados:
            componente = []
            dfs(grafo, visitados, componente, vertice)
            componentes.append(componente)
    
    return componentes

def mostra(componentes : list) -> int:
    
    for componente in componentes:
        if '1'  in componente:
            return(len(componente))
    return 1

def main():
    
    n = int(input())
    while n != 0:    
        grafo = criar_grafo()
        componentes = vertices_conect(grafo)
        print(mostra(componentes))
        n = int(input())

main()
