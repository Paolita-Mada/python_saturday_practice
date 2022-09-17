# La funcion principal para manejar archivos es open()
# Esta funcion recibe dos parametros, el nombre del archivo y el modo
# Los modos son:

# r: para leer y da error si el archivo no existe
# a: para realizar append (agregar al final). Si el archivo no existe, lo crea
# w: para recibir. Elimina el contenido anterior si existe.

file = open("file_handling/example.txt", "r")
print(file.read())

# a la funcion read podemos pasar un numero y va a imprimir esa cantidad de caracteres
print(file.read(54))

# tambien existe la funcion readline(), que les linea por linea
print("Ejemplo de readline()")
print(file.readline())
print(file.readline())

# Debemos cerrar el archivo luego de usarlo
file.close()
