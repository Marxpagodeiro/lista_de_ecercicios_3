#fibonacci
a, b = 0, 1
soma = 0
for i in range(20):
    soma += a
    a, b = b, a + b
print(f"A soma dos 20 primeiros termos da série de Fibonacci é: {soma}")