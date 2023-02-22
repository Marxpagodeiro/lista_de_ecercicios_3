#leitor de numeros multiplos 3 e 5
N=int(input("Digite um numero positivo e inteiro N : "))
for i in range(1,N+1):
    if((i%3)==0 or (i%5)==0 or i==1):
        print(i)    

