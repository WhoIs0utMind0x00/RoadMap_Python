# ->> Operadores <<-

# 1 --> Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits
# ->> Aritméticos
print("\nAritméticos")
suma = 2 + 1                # Suma el valor del primer número al valor del segundo número
resta = 6 - 3               # Resta el valor del segundo número al valor del primer número
multiplicacion = 3 * 2      # Multiplica el valor del primer número por el valor del segundo
division = 3 / 2            # Divide el valor del primer número por el valor del segundo número y devuelve la parte entera del cociente y el decimal (si aplica)
division_entera = 3 // 2    # Divide el valor del primer número por el valor del segundo número y devuelve solo la parte entera del cociente sin decimal
modulo = 10 % 3             # Divide el valor del primer número por el valor del segundo y devuelve el residuo de la división
potencia = 2 ** 3           # Eleva el valor del primer número a la potencia del valor del segundo número

# ->> Operadores lógicos
# -> and: Devuelve True si ambos elementos son True
print("\nOperador and")
print(True and True)        # Imprime True
print(True and False)       # Imprime False
print(False and True)       # Imprime False
print(False and False)      # Imprime False
# -> or: Devuelve True si al menos uno de los elementos son True
print("\nOperador or")
print(True or True)         # Imprime True
print(True or False)        # Imprime True
print(False or True)        # Imprime True
print(False or False)       # Imprime False
# -> not: Devuelve True si es False y viceversa
print("\nOperador not")
print(not True)             # Imprime False
print(not False)            # Imprime True
print(not not not not True) # Imprime True

# ->> Operadores de comparación (Devuelven valores booleanos)
# -> Igual a (==)
print("\n(==)")
print(3 == 4)           # Devuelve False
print(3 == 3)           # Devuelve True
print("Hola" == "hola") # Devuelve False
# -> Distinto a (!=)
print("\n(!=)")
print(3 != 4)           # Devuelve True
print(3 != 2 + 1)       # Devuelve False
print("Hola" != "hola") # Devuelve True
# -> Mayor que (>)
print("\n(>)")
print(10 > 5)           # Devuelve True
print(5 > 10)           # Devuelve False
# -> Menor que (<)
print("\n(<)")
print(10 < 5)           # Devuelve False
print(5 < 10)           # Devuelve True
# -> Mayor o igual que (>=)
print("\n(>=)")
print(10 >= 9)          # Devuelve True
print(10 >= 10)         # Devuelve True
print(9 >= 10)          # Devuelve False
# -> Menor o igual que (<=)
print("\n(<=)")
print(10 <= 20)         # Devuelve True
print(20 <= 20)         # Devuelve True
print(20 <= 10)         # Devuelve False

# ->> Operadores de asignación
# -> Operador (=)
x = 7       # Asigna un valor a la variable (x=7)
# -> Operador (+=)
x += 7      # Suma el nuevo valor de la variable a la variable original (x = x + 7 -> x = 14)
# -> Operador (-=)
x -= 7      # Resta el nuevo valor de la variable al valor anterior de la variable (x = x - 7 -> x = 7)
# -> Operador (*=)
x *= 7      # Multiplica el nuevo valor de la variable por el valor anterior de la variable (x = x * 7 -> x = 49)
# -> Operador (/=)
x /= 7      # Divide el valor anterior de la variable por el nuevo valor de la variable (x = x / 7 -> x = 7)
# -> Operador (%=)
x %= 4      # Divide el valor anterior de la variable por el nuevo valor de la variable y devuelve solo el residuo (x = x % 4 -> x = 3.0)
# -> Operador (//=)
x //= 2     # Divide el valor anterior de la variable por el nuevo valor de la variable y devuelve solo la parte entera del cociente (x = x // 2 -> x = 1.0)
# -> Operador (**=)
x **= 2      # Eleva el valor anterior de la variable a la potencia del nuevo valor de la variable (x = x ** 2 -> x = 1)

# ->> Operadores de identidad
# -> [is]: Devuelve [True] si ambas variables apuntan al mismo objeto, y [False] en caso contrario
# -> [is not]: Devuelve [True] si las variables apuntan a objetos diferentes y [False] si apuntan al mismo objeto
x = [1, 2, 3]
y = x           # Ahora [y] apunta al mismo objeto que [x]
z = [1, 2, 3]   # [z] es un nuevo objeto, aunque con el mismo valor de [x]
print(x is y)       # Devuelve [True] porque ambas variables apuntan al mismo objeto
print(x is z)       # Devuelve [False] porque [x] y [z] son objetos diferentes aunque sus valores sean iguales
print(x == z)       # Devuelve [True] porque los valores de [x] y [z] son iguales
print(x is not y)   # Devuelve [False] porque [x] y [y] apuntan al mismo objeto
print(x is not z)   # Devuelve [True] porque [x] y [z] son distintos objetos

# ->> Operadores de pertenencia
# -> [in]: Devuelve [True] si el valor especificado está presente en la secuencia, de lo contrario, devuelve [False]
# -> [not in]: Devuelve [True] si el valor especificado no está presente en la secuencia, de lo contrario, devuelve [False]
lista = [1, 2, 3, 4]
cadena = "hola"
# >> Ejemplo con [in]
print(2 in lista)               # Salida: True
print("ho" in cadena)           # Salida: True
print(5 in lista)               # Salida: False

# >> Ejemplo con [not in]
print(5 not in lista)           # Salida: True
print("adiós" not in cadena)    # Salida: True
print(3 not in lista)           # Salida: False

# ->> Operadores de bits
# -> Operador (&=) [and]
# >> Si ambos bits son 1, el resultado será 1; de lo contrario será 0
a = 0b101010
a &= 0b111111  # Realiza la comparación [and] bit a bit entre dos variables y almacena su resultado en la primera (A &= B -> A = A & B)
print(bin(a))  # Imprime 0b101010
# -> Operador (|=) [or]
# >> Si cualquiera de los bits es 1, el bit resultante es 1. Solo si ambos bits son 0, el bit resultante es 0]
a = 0b101010
a |= 0b111111  # Realiza el operador [or] elemento a elemento entre dos variables y almacena su resultado en la primera (A |= B -> A = A | B)
print(bin(a))  # Imprime 0b111111
# -> Operador (>>=) [Desplazamiento a la derecha]
# >> Mueve los bits de un número binario hacia la derecha un número específico de posiciones (A = A >> [cantidad de posiciones a desplazar])
a = 0b001100
a >>= 2  # Recorre los bits 2 posiciones a la derecha (0b101010 -> 0b1010)
print(bin(a))  # Imprime 0b1010

a = 0b001100
a <<= 2  # Recorre los bits 2 posiciones a la izquierda (0b001100 -> 0b110000)
print(bin(a))  # Imprime 0b110000

