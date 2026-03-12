"""
Trabalho de Análise de Algoritmos

Implementação do cálculo de fatorial utilizando recursão
e medição do tempo de execução para diferentes valores de n.

Autor: Tiago
"""

import time
import sys

# Constante para aumentar o limite de recursão
MAX_RECURSION_LIMIT = 2000

sys.setrecursionlimit(MAX_RECURSION_LIMIT)


class FatorialRecursivo:
    """
    Classe responsável por calcular o fatorial de um número
    utilizando recursão.
    """

    def calcular_fatorial(self, numero: int) -> int:
        """
        Calcula o fatorial de um número de forma recursiva.

        Parâmetros
        ----------
        numero : int
            Número inteiro para cálculo do fatorial.

        Retorno
        -------
        int
            Resultado do fatorial.
        """

        # Caso base
        if numero == 0 or numero == 1:
            return 1

        # Chamada recursiva
        return numero * self.calcular_fatorial(numero - 1)


def medir_tempo_execucao(numero: int) -> float:
    """
    Mede o tempo de execução do cálculo do fatorial.

    Parâmetros
    ----------
    numero : int
        Número usado no cálculo do fatorial.

    Retorno
    -------
    float
        Tempo de execução em segundos.
    """

    calculadora = FatorialRecursivo()

    inicio = time.time()

    calculadora.calcular_fatorial(numero)

    fim = time.time()

    return fim - inicio


def main() -> None:
    """
    Função principal do programa.

    Executa o cálculo do fatorial e mede o tempo de execução
    para diferentes valores de entrada.
    """

    valores_teste = [10, 100, 500, 1000]

    for numero in valores_teste:
        tempo_execucao = medir_tempo_execucao(numero)

        print(
            f"n = {numero} -> tempo de execução: "
            f"{tempo_execucao:.10f} segundos"
        )


if __name__ == "__main__":
    main()