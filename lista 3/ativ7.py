#taboada
N=int(input("Digite um numero positivo e inteiro N : "))
result=0
if (N>0):
    for i in range(11):
        result=i*N
        print(f"{N} X {i} = {result}")
else:
     print("O programa não pode rodar. Erro: N deve ser inteiro e positivo")