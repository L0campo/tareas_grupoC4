import os

menuinicio=("""Menu:
\n1.sumar
\n2.restar
\n3.factorial
\n4.combinatorias
\n5.triangulo de pascal
\n6.celsius a farentheit
\n7. farentheit a celsius
\n0. salida""")

isActive=True

while isActive:
    os.system("cls")
    print(menuinicio)
    opcion=int(input("\n selecione una opcion 0-7: "))

    match opcion:

        case 0:
            print("gracias por usar nuestros servicos")
            os.system("pause")
            isActive = False

        case 1:
            print("\nSUMA")
            can=int(input("ingrese cuantos datos desea sumar: "))
            suma=0
            for i in range(can):
               n=int(input(f"ingrese la cantidad {i+1}: "))
               suma=suma+n
               
            
            print(f"el resultado de la suma es de: {suma}")
            os.system("pause")
        case 2:
            print("\nMENOR")
            ret=int(input("ingrese cuantos numeros desea restar: "))
            resta=int(input("ingrese la cantidad 1: "))
            for i in range(1,ret):
               
               nu=int(input(f"ingrese la cantidad {i+1}: "))
               

               resta=resta-nu
            print(f"el resultado de la resta es de: {resta} ")
            os.system("pause")
        case 3:
            print("\nfactorial")

            f=int(input("ingrese el numero que desea factorial: "))

            m=1
            
            for i in range(f,0,-1):
                m=i*m

            print(f"el resultado es: {m}")
            os.system("pause")
        case 4:
            print("combinatorias")
            N=int(input("ingrese cuantas cantidades"))
            menores = 0
            iguales = 0
            mayores = 0

            for i in range (1,N+1):
                
                
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
            os.system("pause")
        case 5:
          print("triangulo de pascal")
          n=int(input("ingresa la cantidad de filas que desea: "))

          for lineas in range(n):
            num=1
            print(" " *(n-lineas), end="" )
            for i in range(lineas+1):
              print(num, end=" ")
              num=num* (lineas-i)//(i+1)
            print()
          os.system("pause")
        case 6:
            print("celsius a farentheit")
            cels=float(input("ingrese la temperatura en  Celsius:  "))
            fah= (cels* 9/5) +32
            print(f"la temperatura en Fahrenheit es: {fah} ")
            os.system("pause")
        case 7:
            print("farentheit a celsius")
          
            fahr=float(input("ingrese la temperatura en Fahrenheit:  "))
            celsi = (fahr - 32) * 5/9
            print(f"la temperatura en Celsius es: {celsi} ")
            os.system("pause")
        case _:
          print("opcion invalida")
          os.system("pause")
          
          
          
          
          
        
          


            
            










                


         
           
