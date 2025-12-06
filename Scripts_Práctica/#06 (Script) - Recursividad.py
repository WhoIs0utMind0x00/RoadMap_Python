# Instrucción ->> Calcular el factorial de un número concreto (la función recibe ese número)
# Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonnaci (la función recibe la posición)

# Valor a calcular factorial
num = 5

print("\n== Calcular factorial == ") # Título

# Función: Calcula el factorial de la variable [num]
def calcular_factorial(num):
    # Condición: Detiene la recursión si el número inicial llega a 1
    if num != 1:
        # Operación: Multiplica el valor de [num] por el el valor en la función - 1
        return num * calcular_factorial(num - 1)
    # Condición: El número inicial llegó a 1, detiene la recursión
    else:
        return 1

print(f"Factorial de 5 (5!): {calcular_factorial(num)}")

# Valor a calcular su posición en la Serie de Fibonacci
n = 8
print("\n == Calcular posición en la Serie de Fibonacci == ")   # Título
# Función: Calcula la posición de [num] en la Serie de Fibonacci
def calcular_fibonacci(n):
    # Condición: El índice 1 es 0, si el número inicial es 0, devuelve 0
    if n == 0:
        return 0
    # Condición: El índice 2 es 1, si el número inicial es 1, devuelve 1
    elif n == 1:
        return 1
    # Llama a la función restando 1 a [num] y sumando la función que resta 2 a [num]
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

print(f"Número {n} en la serie de Fibonacci: {calcular_fibonacci(n)}")
