def longitud():
    pregunta = int(input("Deseas hacer la conversion de:"
                         "\n1. Kilómetros a Millas"
                         "\n2. Millas a Kilómetros"
                         "\nIngresa el numero de acuerdo a lo que deseas: "))
    if pregunta == 1:
        km = float(input("Introduce el valor del Kilómetros: "))
        millas = km * 0.621371
        print(f"La cantidad de {km}, en millas es {millas}")
    else:
        millas = float(input("Introduce el valor del millas: "))
        kilometros = millas * 1.60934
        print(f"La cantidad de {millas}, en kilómetros es {kilometros}")


def temperatura():
    pregunta = int(input("Deseas hacer la conversion de:"
                         "\n1. Celsius a Fahrenheit"
                         "\n2. Fahrenheit a Celsius"
                         "\nIngresa el numero de acuerdo a lo que deseas: "))
    if pregunta == 1:
        celsius = float(input("Introduce la Temperatura en Celsius: "))
        fahrenheit = celsius * 1.8 + 32
        print(f"La Temperatura en Celsius es de {celsius}, y en Fahrenheit es de {fahrenheit}")
    else:
        fahrenheit = float(input("Introduce la Temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) / 1.8
        print(f"La Temperatura en Celsius es de {fahrenheit}, y en Fahrenheit es de {celsius}")


def peso():
    pregunta = int(input("Deseas hacer la conversion de:"
                         "\n1. Kg a Libras"
                         "\n2. Libras a Kg"
                         "\nIngresa el numero de acuerdo a lo que deseas: "))
    if pregunta == 1:
        kg = float(input("Introduce el en Kilogramos: "))
        libras = kg * 2.20462
        print(f"El peso en kilogramo es de {kg}, y en libras es de {libras}")
    else:
        libras = float(input("Introduce el valor del libras: "))
        kg = libras * 0.453592
        print(f"El peso en libras es de {libras}, y en libras es de {kg}")
