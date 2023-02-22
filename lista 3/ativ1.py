#soma dos multiplos de 7
soma_multi=0
for i in range(100,501):
    if( i%7==0):
        soma_multi+=i
else:
    print(f"A soma de todos os multiplos de 7 entre 100 e 500 é {soma_multi}")