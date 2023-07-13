
print("break")
for i in range(1,11):
    print(i)
    if i  == 5:
        break
    
 # en conclucion
    # break: rompe el ciclo
    # continue: continua con el ciclo
    
# el break se coloca al final del ciclo
# el continue se coloca al inicio del ciclo
print("continue")
for j in range(1,11):
    if j == 5:
        continue
    print(j)