# 3. celsius_a_fahrenheit.py

def convertir_a_fahrenheit(grados_celsius:float):
    if(grados_celsius >= -273.15):
        grados_fahrenheit= (grados_celsius * (9/5)) + 32
        print(f'{grados_celsius:.2f}°C equivalen a {grados_fahrenheit:.2f}°F')
    else:
        print("¡NO EXISTE TEMPERATURA MÁS BAJA QUE EL CERO ABSOLUTO!")