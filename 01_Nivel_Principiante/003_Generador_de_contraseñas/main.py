import random
import string

class GenerarContrasena:
    def __init__(self):
        pass

    def constructor_contrasena(self):
        letras = string.ascii_letters  # Devuelve: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numeros = string.digits  # Devuelve: '0123456789'
        simbolos = string.punctuation  # Devuelve: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


        longitud = self.longitud_contra()
        caracteres_posibles = letras + numeros + simbolos
        password_final = ""

        for i in range(longitud):
            password_final += random.choice(caracteres_posibles)
        print(f"Tu nueva contraseña segura es: {password_final}")



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
                return numero_caracteres

prueba = GenerarContrasena()
prueba.constructor_contrasena()


