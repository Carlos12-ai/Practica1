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
    print(f"El producto de los numeros es: {producto}")