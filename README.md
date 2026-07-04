# 🌡️ Convertidor de Temperaturas en Python

Proyecto desarrollado en Python como parte de una serie de ejercicios prácticos para fortalecer los fundamentos del lenguaje mediante el uso de funciones, modularización y estructuras de control.

La aplicación permite convertir temperaturas entre las escalas Celsius y Fahrenheit desde la consola, validando además que los valores ingresados no sean inferiores al cero absoluto.

---

# 📌 Descripción

Este proyecto implementa un convertidor de temperaturas con un menú interactivo que permite realizar conversiones entre grados Celsius y Fahrenheit.

Cada tipo de conversión se encuentra implementado en un módulo independiente, promoviendo una mejor organización del código y facilitando su mantenimiento.

Como validación adicional, el programa comprueba que la temperatura ingresada no sea inferior al cero absoluto, evitando resultados físicamente imposibles.

---

# 🎯 Objetivos del Proyecto

* Practicar la creación y uso de funciones.
* Aplicar la modularización mediante múltiples archivos.
* Implementar un menú interactivo en consola.
* Utilizar estructuras de control con `match-case`.
* Aplicar fórmulas matemáticas para la conversión de temperaturas.
* Validar datos de entrada utilizando reglas del mundo real.

---

# 🚀 Características

✅ Conversión de Celsius a Fahrenheit.

✅ Conversión de Fahrenheit a Celsius.

✅ Menú interactivo.

✅ Arquitectura modular.

✅ Funciones independientes para cada conversión.

✅ Validación del cero absoluto.

✅ Resultados formateados con dos decimales.

---

# 🛠️ Tecnologías Utilizadas

* Python 3
* Funciones
* Modularización
* Importación de módulos
* `match-case`
* Bucles `while`
* Entrada y salida por consola
* Type Hints

---

# 📂 Estructura del Proyecto

```text
convertidor-temperaturas/
│
├── main.py
├── menu.py
├── celsius_a_fahrenheit.py
└── fahrenheit_a_celsius.py
```

### Descripción de archivos

| Archivo                   | Función                                         |
| ------------------------- | ----------------------------------------------- |
| `main.py`                 | Punto de entrada del programa.                  |
| `menu.py`                 | Gestiona el menú interactivo y la navegación.   |
| `celsius_a_fahrenheit.py` | Convierte temperaturas de Celsius a Fahrenheit. |
| `fahrenheit_a_celsius.py` | Convierte temperaturas de Fahrenheit a Celsius. |

---

# 🌡️ Fórmulas Utilizadas

## Celsius → Fahrenheit

```text
°F = (°C × 9/5) + 32
```

## Fahrenheit → Celsius

```text
°C = (°F − 32) × 5/9
```

---

# ⚙️ Instalación

## Clonar el repositorio

```bash
git clone https://github.com/Anthony140823/Convertidor-de-temperaturas.git
```

## Acceder al proyecto

```bash
cd RETO - CONVERTIDOR DE TEMPERATURAS
```

## Ejecutar

```bash
python main.py
```

---

# ▶️ Uso

Al iniciar la aplicación se mostrará el siguiente menú:

```text
=== CONVERTIDOR DE TEMPERATURAS ===

1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
3. Salir
```

### Ejemplo

```text
Ingresa una opción: 1

Ingresa un grado Celsius: 25

25.00°C equivalen a 77.00°F
```

---

# ❄️ Validación del Cero Absoluto

El programa incorpora una validación para evitar temperaturas inferiores al cero absoluto, ya que físicamente no pueden existir.

Valores mínimos permitidos:

| Escala     | Temperatura mínima |
| ---------- | -----------------: |
| Celsius    |         -273.15 °C |
| Fahrenheit |         -459.67 °F |

Si el usuario introduce un valor inferior, el programa mostrará un mensaje indicando que dicha temperatura no es válida.

---

# 🧠 Conceptos Aplicados

Durante el desarrollo de este proyecto se pusieron en práctica los siguientes conceptos:

* Funciones.
* Parámetros.
* Modularización.
* Importación de módulos.
* Menús interactivos.
* Bucles `while`.
* Estructuras `match-case`.
* Validación de datos.
* Operaciones matemáticas.
* Formateo de cadenas mediante f-strings.
* Type Hints.
* Organización de proyectos Python.

---

# 📈 Aprendizajes Obtenidos

Este proyecto permitió reforzar la organización del código mediante módulos independientes, comprender la reutilización de funciones y aplicar validaciones basadas en reglas del mundo real.

Además, ayudó a consolidar el uso de estructuras de control modernas en Python y la separación de responsabilidades entre los distintos archivos del proyecto.

---

# 🔮 Mejoras Futuras

Algunas mejoras que podrían implementarse en futuras versiones:

* Manejo de excepciones mediante `try-except`.
* Validación de entradas no numéricas.
* Conversión entre Kelvin, Rankine y otras escalas.
* Historial de conversiones realizadas.
* Interfaz gráfica utilizando Tkinter.
* Pruebas unitarias para las funciones de conversión.
* Empaquetar el proyecto como aplicación ejecutable.

---

# 👨‍💻 Autor

**Anthony JeanPaul Reyes Risco**

Desarrollador de software en formación, enfocado en fortalecer sus habilidades mediante proyectos prácticos y la construcción de un portafolio sólido en Python.

---

# 📄 Licencia

Este proyecto fue desarrollado con fines educativos y forma parte de mi portafolio personal de aprendizaje.
