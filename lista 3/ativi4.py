#ler 20 numeros
for i in range(20):
    num=float(input(f"Digite o {i+1}º número: "))
    if(num %13 == 2):
        print(f"O numero {num} é um numero que dividido por 13 tem resto 2")
else:
    print("Esse programa acabou")