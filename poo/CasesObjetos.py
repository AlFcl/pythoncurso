class Champ ():
    Name= ""
    Region= " "
    Role= ""
    Race= ""
    Habilities= ""

Campeon1= Champ()
Campeon1.Name= "Aatrox"

print(Campeon1.Name)


# * en conclusion, los objetos son como variables pero con mas propiedades, y se pueden crear muchas instancias de un objeto
# * y cada instancia puede tener diferentes valores en sus propiedades
# * y se pueden crear objetos dentro de objetos
# $ para poder

class Mapa():
    Nombre= ""
    Region= ""
    Tipo= ""
    Tamaño= ""
    Campeones= Champ()
    #def __init__ que es el constructor, es el que se ejecuta cuando se crea un objeto de la clase
    # que es un contructor? es un metodo que se ejecuta cuando se crea un objeto de la clase
    # self es una referencia al objeto que se esta creando
    # self es como un this en java
    # self es un parametro obligatorio en el constructor
    # self es el primer parametro del constructor
    # self se puede llamar como uno quiera, pero por convencion se llama self

    def __init__(self, Nombre, Region, Tipo, Tamaño, Campeones):
        
        self.Nombre= Nombre
        self.Region= Region
        self.Tipo= Tipo
        self.Tamaño= Tamaño
        self.Campeones= Campeones
    # __str__ es un metodo que se ejecuta cuando se quiere imprimir el objeto
    def __str__(self):
        return "Nombre: "+self.Nombre+", Region: "+self.Region+", Tipo: "+self.Tipo+", Tamaño: "+self.Tamaño+", Campeones: "+self.Campeones.Name
    
    
Mapa1= Mapa("Rift del invocador", "Runaterra", "5v5", "Grande", Campeon1)



print(Mapa1)
    