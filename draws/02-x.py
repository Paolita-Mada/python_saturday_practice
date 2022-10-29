# el siguiente codigo imprime una matriz de 10x10
for i in range(1,11):
    line = ""
    for j in range(1,11):
        if(j == i) or (j + i == 11):
            line += '*'
        else:
            line += "-"
    print(line)