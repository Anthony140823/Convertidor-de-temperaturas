# 2. menu.py

# impotarción de modulos
from celsius_a_fahrenheit import convertir_a_fahrenheit
from fahrenheit_a_celsius import convertir_a_celsius

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
                grados_celsius = float(input("Ingresa un grado Celsius: "))
                convertir_a_fahrenheit(grados_celsius)
            case 2:
                grados_fahrenheit = float(input("Ingresa un grado Fahrenheit: "))
                convertir_a_celsius(grados_fahrenheit)
            case 3:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida")