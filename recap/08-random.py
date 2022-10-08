import random
import time

# el modulo tiene varios funciones para trabajar con numeros aleatorios.
# la funcion choice es una de las mas usadas eligiendo un elemento al azar desde una lista

fruits = ['manzana','pera','frutilla','piña' ]

# imprimir una fruta al azar
print('Redoble de tambores....')

for i in range(1.4):
    print(".")
    time.sleep(0.5)

print('Tu fruta es: ')
print(random.choice(fruits))
