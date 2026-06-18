"""
=============================================================================
DESAFIO: BANCO DE DADOS DE CLIENTES  --  Classificacao por K-NN
=============================================================================

Objetivo:
    Classificar o perfil de investimento de um NOVO cliente como
    "Conservador" ou "Agressivo" a partir de uma base de treino rotulada.

Caracteristicas (features):
    x1 = Salario anual (em milhares de R$)
    x2 = Pontuacao de credito (0 a 100)

-----------------------------------------------------------------------------
PARADIGMA E FUNCIONAMENTO
-----------------------------------------------------------------------------
    K-NN (K-Vizinhos Mais Proximos) e um algoritmo de APRENDIZADO BASEADO EM
    INSTANCIAS (lazy learning): nao constroi um modelo na fase de treino;
    apenas armazena os exemplos rotulados. A classificacao de um novo ponto
    e feita "na hora", medindo a distancia ate os exemplos guardados e
    escolhendo a classe majoritaria entre os K vizinhos mais proximos.

    Complexidade de tempo (consulta): O(N * D)
        N = numero de exemplos de treino, D = numero de features.
        Aqui N=4 e D=2, mas em bases grandes esse custo por consulta e a
        principal limitacao do K-NN.

    Observacao sobre ESCALA das features:
        O K-NN com distancia euclidiana e sensivel a escala. Se uma feature
        variasse de 0 a 1.000.000 e outra de 0 a 100, a primeira dominaria a
        distancia. Neste problema as duas features tem faixas parecidas
        (~40-90 e 20-80), entao o resultado com dados crus ja e adequado;
        ainda assim, incluimos a opcao de normalizar para evidenciar o ponto.
=============================================================================
"""

import math

# Base de treino: (nome, salario, pontuacao_credito, classe)
TREINO = [
    ("Ana",    40, 20, "Conservador"),
    ("Bruno",  50, 35, "Conservador"),
    ("Carlos", 90, 80, "Agressivo"),
    ("Diana",  80, 65, "Agressivo"),
]


def distancia_euclidiana(a, b):
    """Distancia euclidiana entre dois pontos 2D."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def classificar(novo, k=3, normalizar=False):
    """
    Classifica 'novo' = (salario, pontuacao) usando K-NN.

    Retorna (classe_prevista, lista_de_vizinhos_ordenada).
    """
    treino = TREINO

    # Normalizacao min-max opcional (deixa toda feature na faixa [0, 1])
    if normalizar:
        salarios = [c[1] for c in TREINO]
        creditos = [c[2] for c in TREINO]
        s_min, s_max = min(salarios), max(salarios)
        c_min, c_max = min(creditos), max(creditos)

        def norm(p):
            return ((p[0] - s_min) / (s_max - s_min),
                    (p[1] - c_min) / (c_max - c_min))

        novo_p = norm(novo)
        treino = [(nome, *norm((sal, cred)), cls)
                  for (nome, sal, cred, cls) in TREINO]
    else:
        novo_p = novo

    # 1) Calcula a distancia do novo ponto ate cada exemplo de treino
    distancias = []
    for nome, sal, cred, cls in treino:
        d = distancia_euclidiana(novo_p, (sal, cred))
        distancias.append((d, nome, cls))

    # 2) Ordena pelos mais proximos e pega os K primeiros
    distancias.sort(key=lambda t: t[0])
    vizinhos = distancias[:k]

    # 3) Voto majoritario entre os K vizinhos
    votos = {}
    for d, nome, cls in vizinhos:
        votos[cls] = votos.get(cls, 0) + 1
    classe_prevista = max(votos, key=votos.get)

    return classe_prevista, distancias


def relatar(novo, k=3, normalizar=False):
    """Executa a classificacao e imprime o passo a passo."""
    titulo = f"Novo cliente: salario={novo[0]}, credito={novo[1]}  (k={k}"
    titulo += ", normalizado)" if normalizar else ")"
    print("-" * 60)
    print(titulo)

    classe, distancias = classificar(novo, k=k, normalizar=normalizar)

    print("Distancias (ordenadas do mais proximo ao mais distante):")
    for i, (d, nome, cls) in enumerate(distancias):
        marca = "  <-- vizinho K" if i < k else ""
        print(f"   {nome:7s}: {d:6.2f}  [{cls}]{marca}")

    print(f"=> Perfil previsto: {classe}\n")


if __name__ == "__main__":
    # Cliente de exemplo (TROQUE os valores conforme o enunciado real):
    novo_cliente = (70, 60)

    # K-NN com k=1 (vizinho mais proximo)
    relatar(novo_cliente, k=1)

    # K-NN com k=3 (voto majoritario) -- escolha tipica para evitar ruido
    relatar(novo_cliente, k=3)

    # Mesma classificacao com features normalizadas (confirma robustez)
    relatar(novo_cliente, k=3, normalizar=True)