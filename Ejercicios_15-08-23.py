#1. Escriba un programa que almacene la cadena de caracteres contraseña en una 
# variable, para luego preguntarle al usuario por la contraseña. 
#Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con 
# la guardada en variable.

# Almacena la contraseña en una variable

contraseña_ = "wilmer"

# Pide al usuario que ingrese la contraseña
contraseña_a_ingresar = input("Por favor, ingrese la contraseña: ")

# Compara las contraseñas
if contraseña_a_ingresar == contraseña_a_ingresar:
    print("¡Contraseña correcta!")
else:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
print("--------------------------------------------------------------------")
#2. Realice un programa que le pida al usuario dos números por teclado y muestre por 
# consola su división. Si el divisor es cero el programa debe mostrar un error y solicitar
#nuevamente el numero.

while True:
    try:
        num_1 = int(input("Por favor ingrese su primer número: "))
        num_2 = int(input("Por favor ingrese su segundo número: "))
        
        if num_2 != 0:
            resultado = num_1 / num_2
            print("El resultado de la división es:", resultado)
            break
        else:
            print("Error: No se puede dividir por cero. Intente nuevamente.")
    except ValueError:
        print("Error: Ingrese números válidos.")
print("--------------------------------------------------------------------------")
#3. Escriba un programa que le pida al usuario por teclado un numero entero y 
# muestre en consola si es par o impar.

try:
    numero = int(input("Por favor ingrese un número entero: "))
    
    if numero % 2 == 0:
        print("El número", numero, "es par.")
    else:
        print("El número", numero, "es impar.")
except ValueError:
    print("Error: Ingrese un número entero válido.")

print("-------------------------------------------------------------------------------------------")
#4. Escriba que mediante un vector  de 5 item, lea cada item y evalué el ingreso a menores de 
# edad, si la persona tiene menos de 19 años el programa le debe mostrar 
#en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!

edades = []

for i in range(5):
    while True:
        try:
            edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
            break
        except ValueError:
            print("Ingrese un valor numérico válido.")

    edades.append(edad)

for edad in edades:
    mensaje = "No puede ingresar." if edad < 19 else "¡Bienvenido!"
    print(mensaje)


