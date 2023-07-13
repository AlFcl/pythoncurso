# crear una lsta luego llenarla con numeros solicitado
# crear segunda funcion que ordene los numero de la primera

def llenarLista():
    lista = []
    for i in range(5):
        lista.append(int(input("Ingrese un numero: ")))
    return lista

def ordenarLista(lista):
    lista.sort()
    return lista


