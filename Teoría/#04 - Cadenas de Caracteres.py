# ->> Operaciones con Cadenas de Caracteres <<-

# OPERADORES BÁSICOS
# Concatenación -> Unir dos o más cadenas usando el operador [+]
concatenacion = "Texto" + " " + "concatenado"
# Multiplicación -> Repetir una cadena un número entero de veces usando el operador [*]
multiplicacion = "abc" * 3

# MÉTODOS COMUNES
# .upper() -> Devuelve la cadena en mayúsculas
minus_mayus = "minúscula a mayúscula"
print(minus_mayus.upper())
# .lower() -> Devuelve la cadena en minúsculas
mayus_minus = "MAYÚSCULA A MINÚSCULA"
print(mayus_minus.lower())
# .strip() -> Elimina los espacios en blanco al inicio y al final de la cadena
elimina_espacios = "  Sin espacios      "
print(elimina_espacios.strip())
# .replace([Texto a reemplazar], [Texto de reemplazo])
cadena = "El perro está durmiendo"
print(cadena.replace("durmiendo", "comiendo"))
# .split([delimitador]) ->  Divide la cadena en una lista de subcadenas usando el delimitador especificado
vocales = "a,e,i,o,u"
print(vocales.split(","))
# .join(lista) -> Une los elementos de una lista usando la cadena como separador
lista = ["a", "b", "c", "d", "e"]
print("-".join(lista))
# .format() -> Interpolación de cadenas
# Utilizando el método [.format()]
nombre = "Juan"
print("Hola, {}".format(nombre))
# Utilizando [f] antes de la cadena
print(f"Hola, {nombre}")
# .len() -> Mide la cantidad de caracteres en la cadena
cadena = "longitud"
print(len(cadena))

# ACCESO Y MANIPULACIÓN CON CORCHETES
# Indexación -> Acceder a un carácter específico por su posición (iniciando en 0)
indexar = "Índice"
print(indexar[0])
# Slicing -> Extraer una subcadena especificando un rango de índices [inicio:fin:paso]
print("Slicing"[1:4])       # Imprime "lic"
print("Slicing"[::-1])      # Imprime gnicilS