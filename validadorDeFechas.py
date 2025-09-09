import os
os.system ("cls")

dia=int(input("escriba el dia que  desea para validar su existencia: "))
mes=int(input("escriba el mes que  desea para validar su existencia : "))
año=int(input("escriba el año que  desea para validar su existencia : "))

mes31=[1, 3 ,5 , 7, 8, 10, 12]
mes30=[4, 6, 9, 11]


if 31>=dia and mes in mes31:
    print(f"dia {dia}, mes {mes}, año {año}")
elif dia<=30 and mes in mes30:
    print(f"dia {dia}, mes {mes}, año {año}")
elif dia==28 and mes==2:
    print(f"dia {dia}, mes {mes}, año {año}")
elif dia==29 and año% 4 ==0 and año% 100 !=0 or año% 400==0:
    print(f"dia {dia}, mes {mes}, año {año}")
else:
    print("fecha invalida")