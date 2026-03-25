import math

def calcular_f_recursivo(n):
    """
    Calcula o valor da função F(n) de forma recursiva.
    
    A função segue a regra: F(n) = 2 * F(n-1) + n^2, com F(1) = 2.
    Complexidade: O(n) em tempo (apesar da dica mencionar crescimento exponencial).
    """
    if n == 1:
        return 2
    
    return 2 * calcular_f_recursivo(n - 1) + (n ** 2)

def calcular_f_fechada(n):
    """
    Calcula o valor da função F(n) através da fórmula fechada.
    
    A fórmula resolvida para esta recorrência é:
    F(n) = 13 * 2^(n-1) - n^2 - 4n - 6.
    """
    # Utilizando a biblioteca math conforme solicitado nas dicas
    termo_exponencial = 13 * math.pow(2, n - 1)
    termo_quadratico = math.pow(n, 2)
    
    resultado = termo_exponencial - termo_quadratico - (4 * n) - 6
    return int(resultado)

def main():
    """
    Função principal para interação com o usuário.
    """
    try:
        # Solicita o valor de n ao usuário
        entrada = input("Digite o valor de n (inteiro positivo): ")
        n_usuario = int(entrada)

        if n_usuario < 1:
            print("O valor de n deve ser pelo menos 1.")
        else:
            # Cálculo recursivo
            res_recursivo = calcular_f_recursivo(n_usuario)
            
            # Cálculo pela fórmula fechada (Dica do slide 2)
            res_fechado = calcular_f_fechada(n_usuario)

            print(f"\nResultado por Recursão: {res_recursivo}")
            print(f"Resultado pela Fórmula Fechada: {res_fechado}")

    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()