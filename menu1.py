def main_menu():
    while True:
        print("Menu de operaciones")
        print("1. Suma de 'n' numeros")
        print("2. Producto entre 'n' numeros")
        print("3. Division entre 2 numeros")
        print("4. Calcular factorial de un numero")
        print("5. Tablas de multiplicar")
        print("6. Calculo del cuadrado y cubo de un numero")
        print("7. Promedio de una serie de numeros")
        print("8. Valores maximo y minimo")
        print("9. Salir")
        
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            suma_numeros()
        elif opcion == '2':
            producto_numeros()
        elif opcion == '3':
            division_numeros()
        elif opcion == '4':
            calcular_factorial()
        elif opcion == '5':
            tablas_multiplicar()
        elif opcion == '6':
            cuadrado_cubo()
        elif opcion == '7':
            promedio_numeros()
        elif opcion == '8':
            valores_max_min()
        elif opcion == '9':
            print("Saliendo del programa. Hasta luego")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def suma_numeros():
    numeros = input("Ingrese los numeros separados por espacios: ").split()
    numeros = [float(n) for n in numeros]
    print(f"La suma de los numeros es: {sum(numeros)}")

def producto_numeros():
    numeros = input("Ingrese los numeros separados por espacios: ").split()
    numeros = [float(n) for n in numeros]
    producto = 1
    for n in numeros:
        producto *= n
    print(f"El producto de los numeros es: {producto}")

def division_numeros():
    try:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print(f"El resultado de la division es: {num1 / num2}")
    except ValueError:
        print("Por favor, ingrese valores numericos validos.")

def calcular_factorial():
    try:
        num = int(input("Ingrese un numero entero: "))
        if num < 0:
            print("El factorial no esta definido para numeros negativos.")
        else:
            factorial = 1
            for i in range(1, num + 1):
                factorial *= i
            print(f"El factorial de {num} es: {factorial}")
    except ValueError:
        print("Por favor, ingrese un numero entero valido.")

def tablas_multiplicar():
 try:
     num = int(input("Ingrese el numero de la tabla de multiplicar: "))
         print(f"Tabla de multiplicar del {num}:")
     for i in range(1, 11):
         print(f"{num} x {i} = {num * i}")
     except ValueError:
         print("Por favor, ingrese un numero entero valido.")

def cuadrado_cubo():
 try:
     num = float(input("Ingrese un numero: "))
         print(f"El cuadrado de {num} es: {num**2}")
         print(f"El cubo de {num} es: {num**3}")
     except ValueError:
         print("Por favor, ingrese un numero valido.")
