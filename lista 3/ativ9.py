#imprimir valor de S
N=int(input("Digite um numero positivo e inteiro N : "))
S = 0
for i in range(1,N+1):
    S += 1 / i
print(f"O valor de S é: {S:.2f}")