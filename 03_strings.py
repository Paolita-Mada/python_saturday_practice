# Los strings son cadenas de letras
# se pueden hacer con "" o ' '

str_one = "Micro"
str_two = "System"

# Juntar uno o mas string se denomina concatenar.
# en python se puede concatenar utilizando el operador ""
print(str_one + " " + str_two)

# Ojo: con la "," la funcion print NO
# concatena
print(str_one, str_two)

# Podemos tambien multiplicar un string con un int

print("Hello"*3)

str_three = "Bye"

result = str_three * 5

print(result)

# Existe la funcion len() que nos entrega el largo de un string
# Numero de caracteres
print(len(result))
