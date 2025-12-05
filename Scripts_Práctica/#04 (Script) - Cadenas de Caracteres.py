# Instrucción ->> Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son: 
# Palíndromos
# Anagramas
# Isogramas

def comparar_palabras(palabra1, palabra2):
    # Palíndromos
    pal1 = palabra1.lower() == palabra1.lower()[::-1]
    pal2 = palabra2.lower() == palabra2.lower()[::-1]
    # Anagrama
    anag = sorted(palabra1) == sorted(palabra2) and len(palabra1) == len(palabra2)
    # Isogramas
    iso1 = len(palabra1) == len(set(palabra1))
    iso2 = len(palabra2) == len(set(palabra2))

    # Palíndromo
    # ->> Evalúa si los parámetros se leen igual de izquierda a derecha como de derecha a izquierda
    if pal1 and pal2:
        print(f"{palabra1} y {palabra2} son palíndromos")
    elif pal1 and not pal2:
        print(f"{palabra1} es palíndromo, {palabra2} no lo es")
    elif not pal1 and pal2:
          print(f"{palabra1} no es palíndromo, {palabra2} sí lo es")
    # Anagrama
    # ->> Evalúa si los elementos en las dos listas son los mismos en distinto orden
    elif anag:
            print(f"{palabra1} y {palabra2} son anagramas")
    # Isograma
    # Evalúa si hay caracteres repetidos en las cadenas
    elif iso1 and iso2:
        print(f"{palabra1} y {palabra2} son isogramas")
    elif iso1 and not iso2:
         print(f"{palabra1} es isograma, {palabra2} no lo es")
    elif not iso1 and iso2:
         print(f"{palabra1} no es isograma, {palabra2} sí lo es")
    else:
         print("Ninguna aplica")

comparar_palabras("oso", "sos")
comparar_palabras("arroz", "zorra")
comparar_palabras("murcielago", "casa")
