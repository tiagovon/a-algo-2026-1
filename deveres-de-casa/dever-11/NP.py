"""
=============================================================================
PROBLEMA DA SOMA DE SUBCONJUNTOS  (SUBSET SUM PROBLEM)
=============================================================================

Enunciado:
    Dado um conjunto de inteiros S e um valor alvo T, determinar se existe
    um subconjunto NAO-VAZIO de S cujos elementos somem exatamente T.

-----------------------------------------------------------------------------
CLASSE DE COMPLEXIDADE
-----------------------------------------------------------------------------
    O problema (na sua versao de decisao) e NP-COMPLETO.

      - Esta em NP: dado um certificado (um subconjunto candidato), verificar
        se ele soma T custa apenas O(n) -- basta somar os elementos. Ou seja,
        a VERIFICACAO e polinomial (e exatamente o que o enunciado descreve no
        cenario grande: "verificar uma resposta pronta leva fracoes de
        segundo").

      - E NP-Dificil: e um dos 21 problemas NP-completos de Karp; nao se
        conhece nenhum algoritmo deterministico de tempo polinomial que
        ENCONTRE a solucao. A busca exige, no pior caso, explorar o espaco
        exponencial de 2^n subconjuntos.

    Estar em NP + ser NP-Dificil  =>  NP-Completo.

-----------------------------------------------------------------------------
COMPLEXIDADE DE TEMPO
-----------------------------------------------------------------------------
    1) Forca-bruta / Backtracking:           O(2^n)
         Cada elemento gera 2 ramos (incluir / nao incluir).
         Para n=30 isso da 2^30 ~ 1.07 bilhao de combinacoes -- coerente com
         o enunciado. O branch-and-bound abaixo PODA ramos inviaveis e na
         pratica fica muito mais rapido, mas a complexidade de PIOR CASO
         continua O(2^n) (a poda nao altera a classe do problema).

    2) Programacao Dinamica (apenas inteiros NAO-NEGATIVOS):  O(n * T)
         Tabela booleana dp[soma]. ATENCAO: isso e tempo PSEUDO-POLINOMIAL --
         e polinomial no VALOR de T, mas exponencial no TAMANHO da entrada
         (T ocupa log2(T) bits). Por isso nao contradiz a NP-completude.
         Alem disso, falha diretamente com pesos negativos (cenario medio),
         a menos que se aplique um deslocamento (offset) no indice.

    Implementamos o backtracking com poda por ser geral (trata negativos
    naturalmente) e por evidenciar a natureza combinatoria do problema.
=============================================================================
"""

import random


def subset_sum(S, T):
    """
    Retorna um subconjunto NAO-VAZIO de S que soma exatamente T,
    ou None caso nao exista.

    Estrategia: Backtracking (incluir/excluir cada elemento) com poda por
    limites (branch-and-bound), valida tanto para inteiros positivos quanto
    negativos.
    """
    n = len(S)

    # Pre-calculo dos limites alcancaveis a partir de cada indice i:
    #   max_sufixo[i] = soma de TODOS os positivos em S[i:]   (incremento maximo)
    #   min_sufixo[i] = soma de TODOS os negativos em S[i:]   (incremento minimo)
    # A faixa de somas atingivel a partir do estado atual e:
    #   [soma_atual + min_sufixo[i] , soma_atual + max_sufixo[i]]
    max_sufixo = [0] * (n + 1)
    min_sufixo = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        max_sufixo[i] = max_sufixo[i + 1] + (S[i] if S[i] > 0 else 0)
        min_sufixo[i] = min_sufixo[i + 1] + (S[i] if S[i] < 0 else 0)

    def backtrack(i, soma_atual, escolhidos):
        # Solucao encontrada (subconjunto nao-vazio)
        if soma_atual == T and escolhidos:
            return list(escolhidos)

        # Esgotou os elementos sem atingir T
        if i == n:
            return None

        # PODA: se T esta fora da faixa que ainda da pra alcancar, abandona o ramo
        if soma_atual + max_sufixo[i] < T or soma_atual + min_sufixo[i] > T:
            return None

        # Ramo 1: incluir S[i]
        escolhidos.append(S[i])
        resultado = backtrack(i + 1, soma_atual + S[i], escolhidos)
        if resultado is not None:
            return resultado
        escolhidos.pop()

        # Ramo 2: excluir S[i]
        return backtrack(i + 1, soma_atual, escolhidos)

    return backtrack(0, 0, [])


def relatar(nome, S, T):
    """Executa o solver para um cenario e imprime o resultado formatado."""
    print(f"--- {nome} (n={len(S)}) ---")
    print(f"S = {S}")
    print(f"T = {T}")

    solucao = subset_sum(S, T)

    if solucao is None:
        print("Resultado: NAO existe subconjunto que some T.\n")
    else:
        # Sanidade: confirma que a solucao realmente soma T
        assert sum(solucao) == T, "ERRO: subconjunto invalido!"
        print(f"Resultado: EXISTE. Um subconjunto valido = {solucao}")
        print(f"           Verificacao: soma({solucao}) = {sum(solucao)}\n")


if __name__ == "__main__":
    # ---------------- Cenario Pequeno (n=4) ----------------
    relatar("Tamanho Pequeno", [2, 4, 6, 10], 16)

    # ---------------- Cenario Medio (n=8, com negativos) ----------------
    relatar("Tamanho Medio", [-5, -2, 1, 3, 7, 12, 15, 21], 0)

    # ---------------- Cenario Grande (n=30, inteiros de 5 digitos) ----------------
    random.seed(42)  # semente fixa => execucao reproduzivel
    S_grande = [random.randint(10000, 99999) for _ in range(30)]
    relatar("Tamanho Grande", S_grande, 500000)

    print("=" * 60)
    print("Classe do problema : NP-COMPLETO")
    print("Complexidade tempo : O(2^n) (backtracking / forca-bruta)")
    print("                     O(n*T) por PD, mas apenas pseudo-polinomial")
    print("=" * 60)