# La siguiente lista contiene las notas por estudiantes
# Se pide crear una nueva lista con el nombre y el promedio de notas
grades = [['pri',5,7,6,8,7],['pao', 6,7,4,5,6],['clau',3,5,6,4,6],['char',6,7,4,5,6],['silvi',10,8,7,9,9]]

result = []
for student in grades:
    average_info = []
    average_info.append(student[0])

    sum = 0 # suma de notas
    for grade in student:   # recorre internamente al estudiante
        if(type(grade) is int):
          sum += grade
    average_info.append(sum/(len(student)-1))

    result.append(average_info)
    
    print(result)