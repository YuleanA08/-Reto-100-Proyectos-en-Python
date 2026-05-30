import random

class AdivinaNumero:
    def __init__(self):
        self.RANGO_MIN = 1
        self.RANGO_MAX = 10
        self.num_aleatorio = random.randint(self.RANGO_MIN, self.RANGO_MAX)

    def jugar_aleatorio(self):
        i = 0
        while True:
            i = i + 1
            num_usuario = self.pedir_numero()
            if self.num_aleatorio < num_usuario:
                print("El número secreto es MENOR")
            elif self.num_aleatorio > num_usuario:
                print("El número secreto es MAYOR")
            else:
                print(f"Encontraste el numero secreto que es {self.num_aleatorio} y te tomo {i} intentos")
                break

    def pedir_numero(self):
        while True:
            try:
                num_usuario = int(input(f"Ingrese un numero entre {self.RANGO_MIN} e {self.RANGO_MAX}: "))
            except ValueError:
                print(f"Ingrese un numero entre {self.RANGO_MIN} e {self.RANGO_MAX}")
                continue
            if num_usuario < self.RANGO_MIN or num_usuario > self.RANGO_MAX:
                print("Ingrese un numero entre 1 e 100")
            else:
                return num_usuario


mi_juego = AdivinaNumero()

mi_juego.jugar_aleatorio()