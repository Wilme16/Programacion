#  P O O

class personas:
    def __init__(self, nombre, edad, altura, peso ):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        
    def imprimir (self):
        print(f"El nombre {self.nombre}, la edad {self.edad}")
        
objpersona = personas("hector","20","170","70")
objpersona.imprimir()