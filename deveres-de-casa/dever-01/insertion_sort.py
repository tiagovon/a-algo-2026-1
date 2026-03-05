"""
Dever de casa: Comparação de desempenho entre Insertion Sort (O(n²))
e sorted() do Python (Timsort, O(n log n)).

O programa gera listas aleatórias com tamanhos definidos, mede o tempo
de execução de cada algoritmo e imprime os resultados no terminal.
"""


import random
import time
from typing import List


LIST_SIZES = [1000, 5000, 10000, 20000, 50000]


def insertion_sort(numbers: List[int]) -> List[int]:
    """
    Ordena uma lista de inteiros usando o algoritmo Insertion Sort.

    O Insertion Sort percorre a lista e, para cada elemento, insere-o na posição
    correta dentro da parte já ordenada.

    """
    n = len(numbers)

    for i in range(1, n):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers


def benchmark_sorting_algorithms(size: int) -> None:
    """
    Gera uma lista aleatória e mede o tempo de execução do Insertion Sort e do sorted().

    """
    random_numbers = [random.randint(1, size) for _ in range(size)]

    insertion_input = random_numbers.copy()
    python_sorted_input = random_numbers.copy()

    start_insertion = time.time()
    insertion_sort(insertion_input)
    end_insertion = time.time()

    start_sorted = time.time()
    sorted(python_sorted_input)
    end_sorted = time.time()

    insertion_time = end_insertion - start_insertion
    sorted_time = end_sorted - start_sorted

    print(f"Tempo do Insertion Sort com n={size}: {insertion_time:.6f} s")
    print(f"Tempo do sorted()      com n={size}: {sorted_time:.6f} s")
    print("-" * 50)


def main() -> None:
    """Executa os testes para todos os tamanhos definidos em LIST_SIZES."""
    for size in LIST_SIZES:
        benchmark_sorting_algorithms(size)


if __name__ == "__main__":
    main()