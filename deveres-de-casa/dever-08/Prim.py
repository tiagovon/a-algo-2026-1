import heapq


def prim(grafo, inicio):
    """
    Algoritmo de Prim: encontra a Arvore Geradora Minima (MST).
    Retorna a lista de arestas (origem, destino, peso) em ordem de
    escolha e o custo total (soma dos pesos).
    """
    visitados = {inicio}
    mst = []
    custo_total = 0

    # Fila de prioridade com as arestas que saem do vertice inicial:
    # (peso, origem, destino)
    fila = [(peso, inicio, destino) for destino, peso in grafo[inicio]]
    heapq.heapify(fila)

    while fila and len(visitados) < len(grafo):
        peso, origem, destino = heapq.heappop(fila)   # aresta mais barata

        if destino in visitados:           # evita ciclo
            continue

        visitados.add(destino)             # conecta o novo vertice a MST
        mst.append((origem, destino, peso))
        custo_total += peso

        # Adiciona as arestas que partem do vertice recem-conectado
        for vizinho, p in grafo[destino]:
            if vizinho not in visitados:
                heapq.heappush(fila, (p, destino, vizinho))

    return mst, custo_total


# Grafo NAO-direcionado: cada aresta aparece nos dois sentidos.
# Arestas: A-B:2  A-C:6  A-D:3  B-D:5  C-D:4
grafo = {
    'A': [('B', 2), ('C', 6), ('D', 3)],
    'B': [('A', 2), ('D', 5)],
    'C': [('A', 6), ('D', 4)],
    'D': [('A', 3), ('B', 5), ('C', 4)],
}

mst, total = prim(grafo, 'A')

print("Arvore Geradora Minima (MST) pelo Algoritmo de Prim\n")
print("Arestas componentes (origem -> destino : peso):\n")
for origem, destino, peso in mst:
    print(f"  {origem} -> {destino} : {peso}")

print(f"\nNumero de arestas: {len(mst)}")
print(f"Custo total da MST (soma dos pesos): {total}")