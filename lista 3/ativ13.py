#ler sexo,idade e nome
arm=1.50
cont=0
for i in range(3):
    nome = str(input(f"Digite o nome da pessoa {i+1}: "))
    sexo = str(input(f"Digite o sexo da pessoa {i+1} (M/F): "))
    altura = float(input(f"Digite a altura da pessoa em metros {i+1}: "))
    masc="M"
    femi="F"
    if(sexo==femi):
        cont+=1
print(f"A quantidade de mulheres é {cont} ")