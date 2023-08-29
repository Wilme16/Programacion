#1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas
#Luego muestre la lista por consola mediante un ciclo.

materias = int(input("Ingrese el número de materias que ha cursado: "))

materias_notas = []

for Materias in range(materias):
  materia = input("Ingrese el nombre de la materia: ")
  nota = float(input("Ingrese la nota de la materia: "))
  materias_notas.append((materia, nota))

print("Materias cursadas y sus notas:")

for materia, nota in materias_notas:
  print("Materia:", materia, "nota:", nota)

print("--------------------------------------------------------------------------")

#2. Escriba un programa que almacene personas (input), luego que le muestre 
#por pantalla el mensaje de ‘Su nombre es ‘nombre’

personas = int(input("Ingrese el número de personas que va añadir: "))

nombres = []

for Personas in range(personas):
  nombre = input("Ingrese el nombre de la persona: ")
  nombres.append(nombre)   #Que en la lista nombres se agrega cada valor que se añada en la variable nombre

print("Los nombres de las personas son:")

for nombre in nombres:
  print("Nombre: " , nombre)

print("--------------------------------------------------------------------------")

#3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
#símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

monedas = {"euro": "€", "Dolar": "$", "Yen": "¥"}

moneda = input("Ingrese una de las siguientes divisas: Euro(€), Dolar($), Yen(¥): ")

try:
  divisa = float(input("Ingrese el valor de la divisa: "))
  
except ValueError:
  print("El valor de la divisa debe ser un número.")
  exit()

if moneda == monedas["euro"]:
  a = divisa * 4500
  print("Su moneda es:", moneda,", El valor de su divisa en pesos es: ",a)

  
elif moneda == monedas["Dolar"]:
  b = divisa * 4000
  print("Su moneda es:", moneda,", El valor de su divisa en pesos es: ",b)
  
  
elif moneda == monedas["Yen"]:
  c = divisa * 28.30
  print("Su moneda es:", moneda,", El valor de su divisa en pesos es: ",c)
  
  
else:
  print("DIVISA NO EXISTENTE")
  
print("--------------------------------------------------------------------------")

#4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
#decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados.

valor = (1,2,3,"Hola mundo",1,1.2)

lista = type(valor)

for valores in valor:
  tipo = str(type(valores))
  print("Los elementos que estan en la lista son de tipo: ", tipo)





