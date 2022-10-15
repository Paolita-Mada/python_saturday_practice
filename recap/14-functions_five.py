# Crear una funcion que imprima los numeros divisibles por 3 hasta el numero n

def divisibles_by_three(n):
    print("###########")
    for number in range(1,n + 1):
        if number % 3 == 0:
            print(number)


divisibles_by_three(50)
# divisible_by_three(112)   


# crear una funcion que sume todos los numeros hasta el numero n

def sum_to(n):
    acc = 0

    print("#########")
    for number in range(1, n + 1):
        acc += number
    print(acc)

print(sum_up_to(10))

# crear una funcion que calcule el volumen de una esfera de radio r

import math

def ball_volume(r):
    volume = 4/3*math.pi*r**3
    return volume

result = ball_volume(15)
print(result)


# crear una funcion que entregue el volumen de una cilindro de radio r y altura h

import math

def cylinder_volumen(r,h):
    volume = math.pi*r**2*h
    return volume

result = cylinder_volumen(10,5)
print(result)
