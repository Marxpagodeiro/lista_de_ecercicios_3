#ler 10 numeros e i nformar a soma 
quant=0
soma=0
for i in range(10):
    num=float(input(f"Digite o {i+1}º número: "))
    if(num>=10 and num<=50):
        quant+= 1
    else:
        soma+=num
else:
    print(f"Quantidade de números entre 10 e 50: {quant}")
    print(f"Soma dos números fora do intervalo: {soma}")

    
    
    

