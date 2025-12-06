# Instrucción ->> Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente
# Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia
# Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales.
# A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
# Comprueba también que se ha conservado el valor original en las primeras

# 1 ->> Paso por valor
print("\n == Paso por valor == ") # Título (Divide los scripts en consola)
# Variables originales
a = 50
b = 100

# Función -> intercambia dos valores (paso por valor)
def switch_value(a, b):
    return b, a # Retorna los valores intercambiados

# Asigna los valores retornados a nuevas variables
a_switch, b_switch = switch_value(a, b) 

# Imprime valores originales e intercambiados
print(f"Originales:\na = {a}\nb = {b}") 
print(f"Intercambiadas:\n a = {a_switch}\n b = {b_switch}")

# 2 ->> Paso por referencia
print("\n == Paso por referencia ==") # Título
# Variables originales
x = [5, 10]
y = [20, 25]

# Imprime los valores iniciales de las variables

print(f"Valores iniciales:\n x = {x}\ny = {y}")

# Función -> Intercambia contenido de las variables (paso por referencia)
def switch_reference(x, y):
    x[0], x[1], y[0], y[1] = y[0], y[1], x[0], x[1]
    return x, y

# Llama a la función
switch_reference(x, y)

# Imprime los valores retornados por la función
print(f"Valores intercambiados:\nx = {x}\ny = {y}")
