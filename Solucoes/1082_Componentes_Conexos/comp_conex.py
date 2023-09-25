def criar_grafo() -> dict:
    grafo = {}

    vertices, arestas = map(int, input().split())
    
    for vertice in range(vertices):
        grafo[chr(97 + vertice)] = []
    
    for aresta in range(arestas):
        inicio, fim = map(str, input().split())
        
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

def main():
    
    n = input()
    
    for tc in range(int(n)):

        grafo = criar_grafo() 
        componentes = vertices_conect(grafo)
        conectados = 0
        
        print(f'Case #{tc + 1}:')
        for componente in componentes:
            componente = sorted(componente)
            if len(componente) >= 1:
                conectados += 1
            print(','.join(map(str,componente)) + ',')
        
        print(f"{conectados} connected components\n")
        #print('\n')

main()
