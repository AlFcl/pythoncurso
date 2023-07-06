#while  
#es un bubcle que se repite mientras la condicion sea verdadera
#while condicion:
#    bloque de instrucciones
#el iterador se incrementa o decrementa dentro del bloque de instrucciones
#para que en algun momento la condicion sea falsa y se salga del bucle
#si no se incrementa o decrementa el iterador, se crea un bucle infinito
#y el programa se queda colgado
contador = 1

while contador <= 10:
    print(f"Estoy en el numero: {contador}")
    contador += 1
    
    #el while se ejecuta hasta que la condicion sea falsa
    #siempre hay que tener cuidado de no crear un bucle infinito
    
print("-------------------------------------------")


n = int(input("numero: "))
i = 0

while i <= 12:
    i += 1
    
    print (f"{n} x {i} = {n*i}")
    
    
    
    
    
    
