#leitor de numeros 
M=int(input("Digite um numero positivo e inteiro M : "))
N=int(input("Digite um numero positivo e inteiro N : "))
if(N<=M):
    if(N > 0 and M > 0):
        for i in range(N,M+1):
            print(i)
        else:
            print("O programa terminou")
else:
    print("O programa deu errado")