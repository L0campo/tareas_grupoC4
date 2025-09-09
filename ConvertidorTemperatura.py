import os
os.system ("cls")


print("bienvenido al programa de Convertidor de Temperatura")

menu=int(input("""escoja 1 para passar de Celsius-Fahrenheit
y 2 para pasar de Fahrenheit-Celsius: """))

if menu==1:
    cels=float(input("ingrese la temperatura en  Celsius:  "))
    fah= (cels* 9/5) +32
    print(f"la temperatura en Fahrenheit es: {fah} ")
elif menu==2:
    fahr=float(input("ingrese la temperatura en Fahrenheit:  "))
    celsi = (fahr - 32) * 5/9
    print(f"la temperatura en Celsius es: {celsi} ")
else :
    print("opcion no valida")
    

