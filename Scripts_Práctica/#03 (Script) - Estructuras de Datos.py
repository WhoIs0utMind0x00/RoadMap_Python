# Instrucción ->> Crea una agenda de contactos por terminal.
# * - Debes implementar funcionalidades de búsqueda, inserción, actualización
# *   y eliminación de contactos.
# * - Cada contacto debe tener un nombre y un número de teléfono.
# * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
# *   y a continuación los datos necesarios para llevarla a cabo.
# * - El programa no puede dejar introducir números de teléfono no numéricos y con más
# *   de 11 dígitos (o el número de dígitos que quieras).
# * - También se debe proponer una operación de finalización del programa.

# Diccionario nombre(str):teléfono(int)
agenda = {"Contacto 1": 5512345678, "Contacto 2": 5523456781, "Contacto 3": 5556781234, "Contacto 4": 5513572468, "Contacto 5": 5534127856}
MAXIMO_DIGITOS = 10

# Menú principal
def seleccionar_opcion():
    print("==Menú principal==")
    print("> 1. Buscar contacto \n> 2. Agregar contacto\n> 3. Modificar contacto \n> 4. Eliminar contacto\n> 5. Ver contactos\n> 6. Salir del programa")
    opcion_seleccionada = int(input("Seleccione una opción: "))
    match opcion_seleccionada:
        case 1:
            buscar_contacto()
        case 2:
            agregar_contacto()
        case 3:
            modificar_contacto()
        case 4:
            eliminar_contacto()
        case 5:
            consultar_contactos()
        case 6:
            salir_programa()

# Opción 1 -> Buscar contacto
def buscar_contacto():
    print(" == Buscar contacto == \n")
    busqueda = input("Buscar contacto por nombre: ")
    if busqueda in agenda.keys():
        print(f"Número: {agenda[busqueda]}")
        buscar_menu()
    else:
        buscar_menu_error()

# Opción 2 -> Agregar nuevo contacto
def agregar_contacto():
    print("== Agregar nuevo contacto == \n")
    nombre_contacto = input("Nombre de contacto: ")
    tel_contacto = input("Número de teléfono (10 dígitos): ")
    if len(tel_contacto) == MAXIMO_DIGITOS and tel_contacto.isdigit():
        int(tel_contacto)
        agenda[nombre_contacto] = tel_contacto
        print("Contacto agregado\n")
        agregar_menu()
    else:
        agregar_menu_error()

# Opción 3 -> Modificar contacto
def modificar_contacto():
    print(" == Modificar contacto ==\n")
    busqueda = input("Buscar contacto: ")
    if busqueda in agenda.keys():
        print(f"Número actual: {agenda[busqueda]}")
        nuevo_numero = input("Nuevo número (10 dígitos): ")
        if len(nuevo_numero) == MAXIMO_DIGITOS and nuevo_numero.isdigit():
            int(nuevo_numero)
            agenda[busqueda] = nuevo_numero
            print("Contacto actualizado")
            modificar_menu()
        else:
            modificar_menu_error()
# Opción 4 -> Eliminar contacto
def eliminar_contacto():
    print(" == Eliminar contacto ==\n")
    busqueda = input("Nombre del contacto que desea eliminar: ")
    if busqueda in agenda.keys():
        confirmacion = input(f"¿Desea eliminar {busqueda} de la agenda? (y/n):")
        if confirmacion.lower() != "y":
            no_eliminar_menu()
        else:
            del agenda[busqueda]
            print("Contacto eliminado")
            eliminar_menu()
    else:
        eliminar_menu_error()

# Opción 5 -> Ver contactos
def consultar_contactos():
    print(" == Lista de contactos ==\n")
    for nombre, tel in agenda.items():
        print(f"{nombre}: {tel}")
    consultar_menu()

# Opción 6 -> Salir del programa
def salir_programa():
    respuesta = input("¿Está seguro que desea salir? (y/n): ")
    if respuesta.lower() != "y":
        seleccionar_opcion()
    else:
        exit()


# Menús dentro de funciones

# Menú dentro de "Buscar contacto"
def buscar_menu():
    print("\n> 1. Buscar otro contacto\n> 2. Volver al menú principal\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            buscar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()

# Menú dentro de "Buscar contacto"
def buscar_menu_error():
    print("Contacto no encontrado:(\n")
    print("\n> 1. Intentar de nuevo\n> 2. Volver al menú\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            buscar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()

# Menú dentro de "Agregar contacto"
def agregar_menu():
    print("\n> 1. Agregar otro contacto\n> 2. Volver al menú principal\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            agregar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()
# Menú dentro de "Agregar contacto"
def agregar_menu_error():
    print("Número inválido\n")
    print("\n> 1. Intentar de nuevo\n> 2. Volver al menú\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            agregar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()
# Menú dentro de "Modificar contacto"
def modificar_menu():
    print("\n> 1. Modificar otro contacto\n> 2. Volver al menú principal\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            modificar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()
# Menú dentro de "Modificar contacto"
def modificar_menu_error():
    print("Número inválido\n")
    print("\n> 1. Intentar de nuevo\n> 2. Volver al menú\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            modificar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()

# Menú dentro de "Eliminar contacto"
def eliminar_menu():
    print("\n> 1. Eliminar otro contacto\n> 2. Volver al menú principal\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            eliminar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()
# Menú dentro de "Eliminar contacto"
def eliminar_menu_error():
    print("Contacto no encontrado\n")
    print("\n> 1. Intentar de nuevo\n> 2. Volver al menú\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            eliminar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()
def no_eliminar_menu():
    print("No se eliminó ningún contacto")
    print("\n> 1. Intentar de nuevo\n> 2. Volver al menú\n> 3. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            eliminar_contacto()
        case 2:
            seleccionar_opcion()
        case 3:
            salir_programa()
# Menú dentro de "Consultar contactos"
def consultar_menu():
    print("> 1. Buscar contacto\n> 2. Agregar contacto\n> 3. Modificar contacto\n> 4. Eliminar Contacto\n> 5. Volver al menú principal\n> 6. Salir del programa")
    respuesta = int(input("Seleccione una opción: "))
    match respuesta:
        case 1:
            buscar_contacto()
        case 2:
            agregar_contacto()
        case 3:
            modificar_contacto()
        case 4:
            eliminar_contacto()
        case 5:
            seleccionar_opcion()
        case 6:
            salir_programa()
# Ejecución
seleccionar_opcion()
