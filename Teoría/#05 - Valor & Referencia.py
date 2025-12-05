# Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato
# Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y como se comportan en cada caso en el momento de ser modificados

# ->> Paso por valor
x = 10                          # Inicializo la variable [x]
def funcion(entrada):           
    entrada = 0                 # Dentro de la función hacemos que la variable [entrada] valga 0
funcion(x)                      # Dentro de la función se crea una copia local de [x]
print(x)                        # La variable original no es afectada, imprime su valor inicial

