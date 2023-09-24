def criar_grafo():
    grafo = {}

    vertices, arestas = map(int, input().split())
    
    for vertice in range(vertices):
        grafo[chr(97 + vertice)] = []
    
    for aresta in range(arestas):
        inicio, fim = map(str, input().split())
        
        grafo[inicio].append(fim)
        grafo[fim].append(inicio) 

    return grafo


grafo = criar_grafo() 
print(grafo)
