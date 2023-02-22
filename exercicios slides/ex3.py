#leitor de numeros 
N=int(input("Digite um numero positivo e inteiro N : "))
if(N>0):
    for i in range(2,N+1,2):
        print(i)
    else:
        print("O programa terminou")
else:
    print("O programa não pode rodar")