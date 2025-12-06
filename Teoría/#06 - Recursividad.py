# ->> Recursividad <<-

# Variable con el valor inicial
num_inicial = 101 # Valor añadido para poder imprimir el número 100

# Función: Imprime todos los números del 100 al 0
print(" == Cuenta regresiva utilizando recursividad ==\n")
def recursive(num_inicial):
    # Operación: Resta 1 al número inicial por cada llamada a la función
    cuenta_regresiva = num_inicial - 1
    # Condición: Detiene la recursión si el número inicial llega a cero
    if num_inicial != 0:
        print(cuenta_regresiva) # Imprime cada valor en consola
        return recursive(num_inicial - 1) # Devuelve la llamada a la función
    # Condición: El número inicial llegó a 0, detiene la función usando un [return] vacío
    else:
        return

recursive(num_inicial)  # Salida esperada: 100, 99, 98, [...], 2, 1, 0