#conversor de temperatura
print("Fahrenheit\tCelsius")
for f in range(32, 213):
    c = (f - 32) * 5/9
    print(f"{f}\t\t{c:.2f}")