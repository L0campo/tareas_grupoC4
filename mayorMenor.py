import os
os.system ("cls")

N = int(input("Ingrese cuántas cantidades: "))

menores = 0
iguales = 0
mayores = 0

for i in range(1, N + 1):
    numero = int(input(f"Ingrese la cantidad {i}: "))
    if numero < 0:
        menores += 1
    elif numero == 0:
        iguales += 1
    else:
        mayores += 1

print(f"\nCantidades menores a 0 = {menores}")
print(f"Cantidades iguales a 0 = {iguales}")
print(f"Cantidades mayores a 0 = {mayores}")