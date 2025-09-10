import os
os.system ("cls")

a, b = 0, 1
print(a, b, end=" ")

for i in range(8):  
    
    c = a + b
    print(c, end=" ")
    a, b = b, c