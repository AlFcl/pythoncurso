edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    
    print("Eres menor de edad")
    
    
# ver si es vocal

letra = input("Ingresa una letra: ")

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Es una vocal")
    
else:

        
    print("No es una vocal")
    
# valor absoluto

numero = int(input("Ingresa un número entero: "))

valor_absoluto = abs(numero)

print("El valor absoluto de", numero, "es", valor_absoluto)


#ver si riman

palabra1 = input("Ingresa una palabra: ")
palabra2 = input("Ingresa otra palabra: ")

if palabra1[-3:] == palabra2[-3:]:
    print("Las palabras riman")
    
else:
    
    print("Las palabras no riman")
    