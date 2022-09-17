import time
# Este programa ayuda a saber si podemos hacer un triangulo
# dadas tres longitudes

print("Hola. te voy a ayudar con eso de los triangulos")
l1 = int(input("Ingresa la longitud uno\n"))
l2 = int(input("Ingresa la longitud dos\n"))
l3 = int(input("Ingresa la longitud tres"))

print("Las longitudes entregadas hasta el momento son:")

print(l1,l2,l3)

if(l1 <= l2+l3) and (l2 <= l1+l3) and (l3 <= l2+l1):
    print("si es posible el triangulo con ",l1,l2,l3)
else:
    long_stick = find_max(l1,l2,l3)
    other_sticks = other_sticks(l1,l2,l3)
    print("No es posible formar un triàngulo:",l1,l2,l3,"No cumple la condiciòn")
       
