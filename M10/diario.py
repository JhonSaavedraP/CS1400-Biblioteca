# --- Diaro de      Digital ---

# Aqui tu funcion menu()
def menu ():
    print('1. Escribir')
    print('2. leer')
    print('3. Salir')  
    return input("Selecciona una opción: ") 

while True:
    opcion = menu()
    if opcion == '1':
        # Entrada de datos
        entrada = input("\nEscribe lo que sientes hoy: ")
        # Guardar en archivo (modo 'a' de append para no borrar lo anterior)
        with open("diario.txt", "a") as archivo:
            archivo.write(entrada + "\n")
        print("¡Entrada guardada con éxito!")

    elif opcion == '2':
        # Leer el archivo
        print("\n Tus Memorias")
        try:
            with open("diario.txt", "r") as archivo:
                print(archivo.read())
        except FileNotFoundError:
            print("El diario está vacío. Aún no has escrito nada.")

    elif opcion == '3':
        print("¡Hasta pronto!")
        break # Salir del bucle

    else:
        # El usuario ingresó algo que no es 1, 2 o 3
        print("Opción no válida, intenta de nuevo.")
        
        
    #Aqui tu if/elif/elif/else statement con las opciones del menu
    
    # Entrada de datos
    # Guardar en archivo
    # Leer el archivo 

    
    # Salir de tu ultimo elif con un break
    # else solo para mostrar al usuario que no funciono lo que intentaron ingresar.
