#Funcion para sumar
def sumar(a, b):
    return a + b

#Funcion para restar
def restar(a, b):
    return a - b

#Funcion para multiplicar
def multiplicar(a, b):
    return a * b

#Funcion para dividir
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"No se puede dividir por {e}" )