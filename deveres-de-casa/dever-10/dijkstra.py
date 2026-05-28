import heapq


def dijkstra(grafo, inicio):
    """
    Algoritmo de Dijkstra a partir de 'inicio'.
    Retorna:
      - dist: distancia minima ate cada no
      - pred: predecessor de cada no (para reconstruir o caminho)
      - tabela: registro passo a passo (uma linha por no visitado)
    """
    # Inicializacao: distancia 0 para a origem e infinito para o resto
    dist = {no: float('inf') for no in grafo}
    pred = {no: None for no in grafo}
    dist[inicio] = 0

    visitados = set()
    tabela = []

    # Linha de inicializacao da tabela (copia do estado inicial)
    tabela.append(("Inicializacao", dict(dist), dict(pred), set()))

    # Fila de prioridade: (distancia, no)
    fila = [(0, inicio)]

    while fila:
        d, no = heapq.heappop(fila)

        if no in visitados:        # ja fechado -> ignora entradas antigas da fila
            continue
        visitados.add(no)          # "fecha" o no de menor distancia

        # Relaxa todos os vizinhos do no atual
        for vizinho, peso in grafo[no]:
            nova_dist = d + peso
            if nova_dist < dist[vizinho]:   # achou caminho mais curto
                dist[vizinho] = nova_dist
                pred[vizinho] = no
                heapq.heappush(fila, (nova_dist, vizinho))

        # Registra o estado da tabela apos visitar este no
        tabela.append((f"Visita {no}", dict(dist), dict(pred), set(visitados)))

    return dist, pred, tabela


def reconstruir_caminho(pred, inicio, destino):
    """Reconstroi o caminho do inicio ao destino seguindo os predecessores."""
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        if atual == inicio:
            break
        atual = pred[atual]
    caminho.reverse()
    # So e valido se realmente comeca na origem
    return caminho if caminho and caminho[0] == inicio else None


def imprimir_tabela(grafo, tabela):
    nos = sorted(grafo)
    largura = 14

    # Cabecalho
    cabecalho = "Passo (no visitado)".ljust(22) + "".join(str(n).center(largura) for n in nos)
    print(cabecalho)
    print("-" * len(cabecalho))

    # Linhas
    for nome, dist, pred, visitados in tabela:
        linha = nome.ljust(22)
        for n in nos:
            d = dist[n]
            d_txt = "inf" if d == float('inf') else str(d)
            p = pred[n]
            p_txt = "-" if p is None else str(p)
            visto = " v" if n in visitados else ""   # 'v' marca no ja fechado
            celula = f"{d_txt} ({p_txt}){visto}"
            linha += celula.center(largura)
        print(linha)


# Grafo direcionado: cada no -> lista de (vizinho, peso)
# Arestas: (0,1)=4 (0,2)=1 (2,1)=2 (1,3)=1 (2,4)=5 (3,4)=1
grafo = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (4, 5)],
    3: [(4, 1)],
    4: [],
}

ORIGEM = 0
DESTINO = 4

dist, pred, tabela = dijkstra(grafo, ORIGEM)

print("TABELA PASSO A PASSO  ->  distancia (predecessor), 'v' = no ja visitado\n")
imprimir_tabela(grafo, tabela)

caminho = reconstruir_caminho(pred, ORIGEM, DESTINO)

print("\n" + "=" * 50)
print(f"Caminho minimo de {ORIGEM} ate {DESTINO}: " + " -> ".join(map(str, caminho)))
print(f"Custo minimo total: {dist[DESTINO]}")
print("=" * 50)