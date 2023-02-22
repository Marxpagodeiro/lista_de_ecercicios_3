#tamanho da arvores
jequitiba_altura = 1.50
jaqueira_altura = 1.10
jabuticabeira_altura = 2.98

for i in range(25):
    jequitiba_altura += 0.01
    jaqueira_altura += 0.02

print(f"Altura do Jequitibá após 25 anos: {jequitiba_altura:.2f}")
print(f"Altura da Jaqueira após 25 anos: {jaqueira_altura:.2f}")
print(f"Altura da Jabuticabeira após 25 anos: {jabuticabeira_altura:.2f}")
if (jequitiba_altura>jaqueira_altura and jequitiba_altura>jabuticabeira_altura):
    print("O Jequitibá terá a maior altura após 25 anos.")
elif (jaqueira_altura>jequitiba_altura and jaqueira_altura>jabuticabeira_altura):
    print("A Jaqueira terá a maior altura após 25 anos.")
else:
    print("A Jabuticabeira terá a maior altura após 25 anos.")

