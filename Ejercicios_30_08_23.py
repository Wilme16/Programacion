#1. Escriba una función que muestre por consola un saludo personalizado. 
#Por ejemplo ‘¡Hola mundo!’


def saludo():
    a = input("Ingrese un saludo que quiera que salga por pantalla: ")
    return a

salida = saludo()

print("Su saludo es: ", salida)


print("-----------------------------------------------------------------------------")

#2. Escriba una función que reciba un nombre por parámetro y que luego 
#muestre en pantalla ¡Hola <nombre>!

def nombre():
    a = input("Ingrese un nombre que quiera que salga por pantalla: ")
    return a

salida = nombre()

print("Hola", salida)


print("-----------------------------------------------------------------------------")

#3. Cree una función que le pida al usuario su nombre y su edad, 
#luego muestre en pantalla los resultados

def nombre_edad ():
  a = str(input("Ingrese su nombre: "))
  b = int(input("Ingrese su edad: "))
  print() 
  print("Su nombre es: " , a)
  print("Su edad es: ", b)

nombre_edad()


print("-----------------------------------------------------------------------------")

#4. Definir una función que reciba n cantidad de números por 
#parámetros y que luego los sume, reste, mutiplique y divida.

def operaciones():
    # Se debe importar la biblioteca math para utilizar las funciones matemáticas
    import math
    
    a = int(input("Ingrese el número de números que quiere ingresar: "))
    numeros = []

    # Cambiamos el nombre de la variable del bucle para evitar conflictos
    for num in range(a):
        numero = float(input("Ingrese sus números: "))
        numeros.append(numero)

    b = input("Ingrese la operación que quiere llevar a cabo (+, -, *, /): ")

    if b == '+':
        resultado = sum(numeros)  # Usamos la función sum() para sumar los números

    elif b == '-':
        resultado = numeros[0] - sum(numeros[1:])  # Restamos los demás números al primero

    elif b == '*':
        resultado = math.prod(numeros)  # Usamos math.prod() para multiplicar los números

    elif b == '/':
        resultado = numeros[0]
        for i in range(1, len(numeros)):
            if numeros[i] == 0:
                print("Error: División por cero")
                return
            resultado /= numeros[i]  # Dividimos el primer número por los demás

    else:
        print("Operación no válida")
        return

    print("El resultado de la operación es:", resultado)

operaciones()