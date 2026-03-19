"""
Trabalho de Análise de Algoritmos

Verificar se um array é palíndromo utilizando recursão.

Autor: Tiago
"""


def verificar_palindromo(array: list) -> bool:
    """
    Verifica se um array é um palíndromo usando recursão.

    Parâmetros
    ----------
    array : list
        Lista de elementos a ser verificada.

    Retorno
    -------
    bool
        True se for palíndromo, False caso contrário.
    """

    if len(array) == 0 or len(array) == 1:
        return True

    if array[0] == array[-1]:
        return verificar_palindromo(array[1:-1])

    return False


def main() -> None:
    """
    Função principal para testar os exemplos.
    """

    ARRAY1 = [0, 1, 2, 3, 2, 1, 0]
    ARRAY2 = ["a", "b", "b", "a"]
    ARRAY3 = ["a", "b", "c", "b", "a"]
    ARRAY4 = ["a", "b", "c", "f", "b", "a"]

    arrays = [ARRAY1, ARRAY2, ARRAY3, ARRAY4]

    for indice, array in enumerate(arrays, start=1):
        resultado = verificar_palindromo(array)

        if resultado:
            print(f"array{indice}: {array} -> É palíndromo")
        else:
            print(f"array{indice}: {array} -> Não é palíndromo")


if __name__ == "__main__":
    main()