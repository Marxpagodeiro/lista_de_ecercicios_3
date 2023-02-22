#numeros inteiros pares m e n
M=int(input("Digite um numero positivo e inteiro M : "))
N=int(input("Digite um numero positivo e inteiro N : "))
if(N<=M):
    for i in range(N,M+1,2):
        print(i)
    else:
        print("O programa terminou")
else:
    print("O programa não pode rodar")