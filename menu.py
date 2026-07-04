# menu.py
def abrir_menu():
    while True:
        print('''\nCoversiones a realizar:
            1. Celsius a Fahrenheit
            2. Fahrenheit a Celsius
            3. Salir
        \n''')
        
        opcion = int(input("Ingresa una opción: "))

        match(opcion):
            case 1:
                pass
            case 2:
                pass
            case 3:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida")