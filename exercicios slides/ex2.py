frase=str(input("Digite uma frase: "))
cont_vogal=0

for i in frase:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        cont_vogal=cont_vogal+1
print("Quantidades de vogais é",cont_vogal)