import heapq


def prim(grafo, inicio):
    """
    Algoritmo de Prim: encontra a Arvore Geradora Minima (MST).
    Retorna a lista de arestas escolhidas (em ordem de instalacao)
    e o custo total minimo.
    """
    visitados = {inicio}                  # cidades ja conectadas a rede
    mst = []                              # arestas escolhidas (a rota dos cabos)
    custo_total = 0

    # Fila de prioridade com as arestas que saem do ponto inicial.
    # Cada item e: (peso, cidade_origem, cidade_destino)
    fila = [(peso, inicio, destino) for destino, peso in grafo[inicio]]
    heapq.heapify(fila)

    # Enquanto houver arestas e ainda faltar conectar alguma cidade
    while fila and len(visitados) < len(grafo):
        peso, origem, destino = heapq.heappop(fila)   # pega a aresta mais barata

        if destino in visitados:          # ja conectada -> evita ciclo
            continue

        # Conecta a cidade de destino a rede
        visitados.add(destino)
        mst.append((origem, destino, peso))
        custo_total += peso

        # Adiciona na fila as novas arestas que partem da cidade conectada
        for vizinho, p in grafo[destino]:
            if vizinho not in visitados:
                heapq.heappush(fila, (p, destino, vizinho))

    return mst, custo_total


# Grafo: cada cidade aponta para seus vizinhos (vizinho, distancia em Km)
grafo = {
    'A': [('B', 4), ('C', 4)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 5), ('E', 6)],
    'D': [('B', 5), ('C', 5), ('E', 3), ('F', 4)],
    'E': [('C', 6), ('D', 3), ('F', 2)],
    'F': [('D', 4), ('E', 2)],
}

rota, total = prim(grafo, 'A')

print("Rota dos cabos a serem instalados (em ordem):\n")
for origem, destino, peso in rota:
    print(f"  {origem} --> {destino}: {peso} Km")

print(f"\nQuantidade total minima de cabos utilizados: {total} Km")