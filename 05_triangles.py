import time
# Este programa ayuda a saber si podemos hacer un triangulo
# dadas tres longitudes

print("Hola. te voy a ayudar con eso de los triangulos")
l1 = int(input("Ingresa la longitud uno\n"))
l2 = int(input("Ingresa la longitud dos\n"))
l3 = int(input("Ingresa la longitud tres"))

print("Las longitudes entregadas hasta el momento son:")

print(l1,l2,l3)

if(l1 <= l2+l3):
    print("Vamos bien, revisemos los otros casos")
    time.sleep(0.5)
    if(l2 <= l1+l3):
        print("Seguimos bien, veamos el tercero")
        time.sleep(0.5)
        if(l3 <= l2+l1):
            print("Si es posible el triangulo")        
else:
    print("No es posible el triangulo")
else:
    print("No es posible el triangulo")
else:
    print("No es posible el triangulo:,"l1, "No es menor que",12 "+", 13)
