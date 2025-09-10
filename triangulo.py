import os
os.system ("cls")

n=int(input("ingresa la cantidad de filas que desea: "))

for lineas in range(n):
    num=1
    print(" " *(n-lineas), end="" )
    for i in range(lineas+1):
        print(num, end=" ")
        num=num* (lineas-i)//(i+1)
    print()