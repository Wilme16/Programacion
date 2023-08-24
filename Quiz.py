#1.Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas
#Luego muestre la lista por consola mediante un ciclo.

materias= int(input("Ingrese el numero de materias que ha cursado, las cuales va a ingresar: "))
numero_materias=[]

for num_materias in range (materias):
  materia= input("ingrese el nombre de la materia: ")
  nota = input("ingrese la nota de la matera: ")
  numero_materias.append((materia, nota))

print("Materias cursadas y sus notas")

for materia, nota in numero_materias:
  print("Materia:",materia,"nota:",nota)

print("--------------------------------------------------------------------------")


#2. Escriba un programa que almacene personas (input), luego que le muestre 
#por pantalla el mensaje de ‘Su nombre es ‘nombre’

personas= int(input("Ingrese el numero de personas que va añadir: "))
persona=[]

for num_persona in range(personas):
  nombre=input("Ingrese el nombre de la persona: ")
  persona.append(nombre)

for nombre in persona:
  print("El nombre de la persona es:",nombre)
  
print("--------------------------------------------------------------------------")

#3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
#símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

monedas = {"euro":"€", "Dolar": "$", "Yen":"¥" }

moneda = input("Ingrese una de las siguientes divisas: Euro, Dolar, Yen: ")
valor = float(input("Ingrese el valor que le va a dar la divisa en pesos: ")) 

if moneda in monedas:
  simbolo = monedas[moneda]
  print("Su moneda es:", simbolo, "Su valor es:", valor)

else:
  print("MONEDA NO ENOONTRADA")
  
print("--------------------------------------------------------------------------")

#4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
#decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados.
    
valor = (1,2,3,"Hola mundo",1,1.2)

for valores in valor:
  tipo = type(valores)
  print("El elemento que esta en la tupla es:", tipo) 