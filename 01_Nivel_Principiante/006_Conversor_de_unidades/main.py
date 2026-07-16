import categorias_unidades


class ConversorUnidades:
    def __init__(self):
        pass

    def iniciar(self):
        while True:
            try:
                inicial = int(input("---- Este es un conversor de Unidades ----"
                                    "\nEstas son las categorías: "
                                    "\n1. Longitud"
                                    "\n2. Temperatura"
                                    "\n3. Peso"
                                    "\nIngresa el numero de acuerdo a lo que deseas: "))
                if inicial == 1:
                    categorias_unidades.longitud()
                elif inicial == 2:
                    categorias_unidades.temperatura()
                elif inicial == 3:
                    categorias_unidades.peso()
                else:
                    break

            except ValueError:
                print("Ingresa un numero valido")
                continue

            pregunta = input("Deseas hacer otra conversion: s/n").strip().lower()
            if pregunta != "s":
                print("¡Vuelva cuando lo desee!")
                break


mi_conversor = ConversorUnidades()
mi_conversor.iniciar()
