def recursivo(n):
  if n == 1:
    result = 2
    return result
  else:
    result = 2*recursivo(n-1) +n*n
    return result

n = int(input("n"))

resultado = recursivo(n)
print(resultado)
