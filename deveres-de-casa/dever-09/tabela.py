def bellman_ford(nos, arestas, inicio, num_iteracoes=None):
    """
    Algoritmo de Bellman-Ford a partir de 'inicio'.
    'arestas' e uma lista de (origem, destino, peso).
    Retorna:
      - dist, pred: distancias minimas e predecessores
      - tabela: estado (dist, pred) apos cada iteracao
      - tem_ciclo_negativo: True/False
    """
    # Por padrao faz |V| - 1 iteracoes (garantia teorica do algoritmo)
    if num_iteracoes is None:
        num_iteracoes = len(nos) - 1

    # Inicializacao: origem = 0, resto = infinito
    dist = {no: float('inf') for no in nos}
    pred = {no: None for no in nos}
    dist[inicio] = 0

    tabela = [("Inicializacao", dict(dist), dict(pred))]

    # A cada iteracao percorremos TODAS as arestas tentando relaxar
    for i in range(1, num_iteracoes + 1):
        houve_mudanca = False
        for origem, destino, peso in arestas:
            if dist[origem] != float('inf') and dist[origem] + peso < dist[destino]:
                dist[destino] = dist[origem] + peso
                pred[destino] = origem
                houve_mudanca = True
        tabela.append((f"Iteracao {i}", dict(dist), dict(pred)))
        # Otimizacao: se uma iteracao nao muda nada, ja convergiu
        if not houve_mudanca:
            # Preenche as iteracoes restantes repetindo o estado estavel
            for j in range(i + 1, num_iteracoes + 1):
                tabela.append((f"Iteracao {j}", dict(dist), dict(pred)))
            break

    # Verificacao de ciclo negativo: uma passada EXTRA.
    # Se ainda for possivel relaxar alguma aresta, existe ciclo negativo.
    tem_ciclo_negativo = False
    for origem, destino, peso in arestas:
        if dist[origem] != float('inf') and dist[origem] + peso < dist[destino]:
            tem_ciclo_negativo = True
            break

    return dist, pred, tabela, tem_ciclo_negativo


def imprimir_tabela(nos, tabela):
    nos_ord = sorted(nos)
    largura = 12

    cabecalho = "Iteracao".ljust(16) + "".join(str(n).center(largura) for n in nos_ord)
    print(cabecalho)
    print("-" * len(cabecalho))

    for nome, dist, pred in tabela:
        linha = nome.ljust(16)
        for n in nos_ord:
            d = dist[n]
            d_txt = "inf" if d == float('inf') else str(d)
            p = pred[n]
            p_txt = "-" if p is None else str(p)
            linha += f"{d_txt} ({p_txt})".center(largura)
        print(linha)


# Grafo direcionado de 5 vertices (0..4)
nos = [0, 1, 2, 3, 4]

# Arestas: (origem, destino, peso) -- peso -1 em 3->4 e o negativo
arestas = [
    (0, 1, 5),
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 1),
    (3, 4, -1),
]

ORIGEM = 0

# O enunciado pede Iteracao 1, 2 e 3 -> forcamos 3 iteracoes
dist, pred, tabela, ciclo_neg = bellman_ford(nos, arestas, ORIGEM, num_iteracoes=3)

print("TABELA POR ITERACAO  ->  distancia (predecessor)\n")
imprimir_tabela(nos, tabela)

print("\n" + "=" * 45)
if ciclo_neg:
    print("Existe um CICLO NEGATIVO no grafo.")
    print("(As distancias minimas nao sao confiaveis.)")
else:
    print("NAO existe ciclo negativo no grafo.")
    print("\nDistancias minimas a partir do vertice", ORIGEM, ":")
    for n in sorted(nos):
        print(f"  vertice {n}: {dist[n]}  (veio de {pred[n]})")
print("=" * 45)