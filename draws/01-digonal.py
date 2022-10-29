# objetivo dibujar una linea diagonal en un cuadrado de 10 * 10

# el siguiente codigo imprime una matriz de 10x10
for i in range(1,11):
    line = ""
    for j in range(1,11):
        if(j == i):
            line += '*'
        else:
          line += "-"
    print(line)