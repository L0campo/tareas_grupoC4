import os
os.system ("cls")

año=int(input("escriba el año que consideres bisiesto: "))



if año% 4 ==0 and año% 100 !=0 or año% 400==0:
    print("es un año bisiesto")
else :
    print("no es un año bisiesto")