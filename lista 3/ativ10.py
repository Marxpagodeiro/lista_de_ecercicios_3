#fatorial
M=int(input("Digite um numero positivo e inteiro M : "))
N=int(input("Digite um numero positivo e inteiro N : "))
soma=0
fat_N=1
fat_M=1
if(N>0 or M>0):
    if (N!=0):
        for i in range(N,0,-1):
            fat_N=fat_N*i
    print(f"{N}! = {fat_N:.2f}")
    if (M!=0):
        for j in range(M,0,-1):
            fat_M=fat_M*j
    print(f"{M}! = {fat_M:.2f}")
    soma=fat_N+fat_M
    print(f"A soma dos fatorias de M e N é: {soma:.2f}")
else:
    print("O programa não pode rodar. Erro: N e M devem ser inteiros positivos")
