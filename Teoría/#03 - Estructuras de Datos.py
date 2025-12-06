# ->> Estructuras de Datos <<-

#  Listas
lista = [1, 2, 3, 4, 5, "Seis"]
# Tuplas
tupla = ("a", "b", "c", "d", "e")
# Conjuntos
conjunto = {2, 4, 6, 8, "Diez"}
# Diccionarios
diccionario = {"Usuario": "Abibi", "Teléfono": "55 1234 5678", "Lenguaje de programación": "Python"}

# append() -> Agrega un elemento al final de la lista ->> lista.append("Nuevo elemento")
lista.append("Siete")
print(lista)
# insert() -> Agrega un elemento en una posición específica ->> lista.insert(1, "Nuevo elemento")
lista.insert(0, 0)
print(lista)
# del() -> Elimina un elemento mediante su índice ->> del lista[2]
del lista[7]
print(lista)
# remove() -> Elimina un elemento mediante su valor ->> lista.remove("elemento")
lista.remove("Seis")
print(lista)
# sort() -> Ordena valores ->> lista.sort()
lista.sort()
print(lista)
