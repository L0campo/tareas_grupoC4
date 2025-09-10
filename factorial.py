import os
os.system ("cls")

m=1

n=int(input("ingrese un numero entero: "))

for i in range (n,0,-1):
    
    m=m*i


print(f"el resultado es: {m}")