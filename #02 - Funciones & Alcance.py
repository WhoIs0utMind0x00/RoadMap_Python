def contar_apariciones(a, b):
        conteo_tres = 0
        conteo_cinco = 0
        conteo_ambos = 0
        conteo_numero = 0
        # Itera en el rango numérico 1 - 100
        for n in range(1, 101):
            if n % 3 == 0 and n % 5 == 0:   # Filtra múltiplos en común de 3 y 5
                print(a + b)                # Imprime el valor de los parámetros [a] y [b] concatenados
                conteo_ambos += 1
            elif n % 3 == 0:                # Filtra múltiplos de 3
                print(a)                    # Imprime el valor del parámetro [a]
                conteo_tres += 1
            elif n % 5 == 0:                # Filtra múltiplos de 5
                print(b)                    # Imprime el valor del parámetro [b]
                conteo_cinco += 1
            else:
                print(n)                    # Imprime los números que no cumplen ninguna función anterior
                conteo_numero += 1
        # Imprime estadísticas
        print("Cantidad total de caracteres impresos:", conteo_tres + conteo_cinco + conteo_ambos + conteo_numero)
        print(f"Cantidad de veces que se imprimió {a}:", conteo_tres)
        print(f"Cantidad de veces que se imprimió {b}:", conteo_cinco)
        print(f"Cantidad de veces que se imprimió {a + b}:", conteo_ambos)
        return conteo_numero                # Devuelve el conteo de los números impresos

apariciones = contar_apariciones("X", "O")
print("Cantidad de veces que se imprimió un número:", apariciones)
