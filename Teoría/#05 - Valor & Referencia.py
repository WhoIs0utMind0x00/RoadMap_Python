# Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato
# Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y como se comportan en cada caso en el momento de ser modificados

# ->> Paso por valor (Diferente ID)
x = 10                          # Inicializo la variable [x]
print(id(x))            # ID: 2056
def funcion(entrada):           
    entrada = 0                 # Dentro de la función hacemos que la variable [entrada] valga 0
    print(id(entrada))  # ID: 1736
funcion(x)                      # Dentro de la función se crea una copia local de [x]
print(x)                        # La variable original no es afectada, imprime su valor inicial (10)


# ->> Paso por referencia (Mismo ID)
x = [10, 20, 30]                # Ahora, [x] es una lista, la función pasa [x] como referencia
print(id(x))            # ID: 0176
def funcion(entrada):           
    entrada.append(40)          #  Al pasar por referencia, la función modifica la variable original
    print(id(entrada)) # ID: 0176
funcion(x)
print(x)                        # Imprime la variable modificada ([10, 20, 30, 40])
