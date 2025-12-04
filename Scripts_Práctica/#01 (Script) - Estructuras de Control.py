# Instrucción ->> Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3

# Itera sobre los números dentro del rango 10 - 55
for i in range(10, 56):
        if i != 16 and i % 3 != 0:      # Omite el número 16 y los múltiplos de 3
            if i % 2 == 0:              # Filtra solo los pares
                print(i)                # Imprime los números pares excepto 16 y múltiplos de 3