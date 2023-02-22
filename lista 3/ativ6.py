#não multiplos de 3 e 7
M=int(input("Digite um numero positivo e inteiro M : "))
N=int(input("Digite um numero positivo e inteiro N : "))
soma=0
if(N<M or N>0 or M>0):
    for i in range(N,M+1):
        if (i%3!=0 and i%7!=0):
            soma+=i
    print(f"A soma dos numeros do intervalo de N e M que não são multiplos de 3 e 7 é {soma}")
else:
    print("O programa não pode rodar. Erro: N e M devem ser inteiros positivos e N < M")