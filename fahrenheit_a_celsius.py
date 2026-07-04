# 4. fahrenheit_a_celsius.py

def convertir_a_celsius(grados_fahrenheit:float):
    if(grados_fahrenheit >= -459.67):
        grados_celsius= (grados_fahrenheit - 32) * (5/9)
        print(f'{grados_fahrenheit:.2f}°F equivalen a {grados_celsius:.2f}°C')
    else:
        print("¡NO EXISTE TEMPERATURA MÁS BAJA QUE EL CERO ABSOLUTO!")