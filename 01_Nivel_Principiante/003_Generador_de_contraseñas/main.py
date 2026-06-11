import random

class GenerarContrasena:
    def __init__(self):
        pass

    def constructor_contrasena(self):
        pass

    def longitud_contra(self):
        while True:
            try:
                numero_caracteres = int(input("Introduce un numero: "))
            except ValueError:
                print("Introduce un numero")
                continue
            if numero_caracteres < 8:
                print("Su contraseña seria muy insegura")
            else:
                break

prueba = GenerarContrasena()
prueba.longitud_contra()


