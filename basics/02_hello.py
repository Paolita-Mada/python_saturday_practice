# Las variables son nombres que apuntan a algun valor
# y el valor es de cierto tipo

name = "stranger"

# No pueden comenzar con numeros ni palabras reservadas
# Es muy aconsejable no utilizar mayusculas ni acentos.
# Para separar nombres largos, utilizar el "_"

long_name_variable = "Something"
longaniza = "Chillan"

print(long_name_variable, longaniza)

# Podemos saber el tipo (class) de variable con la funcion type

print(type(longaniza),type(name), type(long_name_variable))

# Otros tipos frecuentes

# int
number = 42
print(type(number))

# bool
is_real = True
not_real = False
print(type(is_real), type(not_real))

# float
decimal = 1.0
print(type(decimal))