for i in range(1,11):
    row = ''
    for j in range(1,11):
      if(i == 1) or (i == 10) or (j+i == 11):
        row += "*"
      else:
        row += " "
    print(row)           