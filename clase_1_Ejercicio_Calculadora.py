print()
x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))
print()
print("Su primer número es:", x)
print("Su segundo número es:", y)
print()
simbolo = input("Ingrese el símbolo de la operación que desea realizar (+, -, *, /, %): ")
print()
# -----------------------------------------------------------------------------------------------
if simbolo == "+":
    suma = x + y
    print("La suma de los números es:", suma)
# -----------------------------------------------------------------------------------------------
elif simbolo == "-":
    resta = x - y 
    print("La resta de los números es:", resta)
# -----------------------------------------------------------------------------------------------
elif simbolo == "/":
    if y != 0:
        division = x / y
        print("La división de los números es:", division)
    else:
        print("Error: No se puede dividir por cero.")
# -----------------------------------------------------------------------------------------------      
elif simbolo == "*":
    multiplicacion = x * y
    print("La multiplicación de los números es:", multiplicacion)
# ----------------------------------------------------------------------------------------------- 
elif simbolo == "%":
    if y != 0:
        modulo = x % y 
        print("El módulo de la división es:", modulo)
    else:
        print("Error: No se puede calcular el módulo con cero.")
else:
    print("Operador no válido.")
