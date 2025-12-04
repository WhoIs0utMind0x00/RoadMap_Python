# 2 --> Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones. Debes hacer print por consola del resultado de todos los ejemplos.

# ->> Estructura Condicional
# -> [if -elif]
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Bien, eres mayor de edad.")
elif edad >= 14 and edad < 18:
    print(f"Solo tienes {edad} años, aún no eres mayor de edad.")
elif edad >= 10 and edad < 14:
    print(f"Eres muy pequeño aún.")
else:
    print("Eres un niño todavía.")

# ->> Estructuras iterativas
# -> [while]
contador = 0
while contador < 11:
    print(f"Contando: {contador}...")
    contador += 1

# -> [for]
frutas = ['Manzana', 'Pera', 'Uva', 'Sandía']
for fruta in frutas:
    print(fruta)
