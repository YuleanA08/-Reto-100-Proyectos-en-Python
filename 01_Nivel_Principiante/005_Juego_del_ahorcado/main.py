import random

class JuegoAhorcado:
    def __init__(self):
        self.vidas = 6
        self.palabras_posibles = ["PYTHON", "PROGRAMA", "COMPUTADORA", "TECLADO", "INTERNET"]
        self.letras_intentadas = []
        self.palabra_secreta = random.choice(self.palabras_posibles)
        self.tablero = ["-"]*len(self.palabra_secreta)

    def mostrar_estado(self):
        print(f"\nVidas restantes: {self.vidas}")
        print(f"Tablero:" + " ".join(self.tablero))

    def jugar(self):
        while self.vidas > 0 and "-" in self.tablero:
            self.mostrar_estado()
            letra = input("Palabra: ").upper()

            if letra in self.letras_intentadas:
                print(f"¡Ya intentaste con esta letra: {letra}! Prueba otra")
                continue

            # 2. Si el código llega a esta línea, significa que la letra es NUEVA.
            # Por lo tanto, debemos anotarla en nuestra libreta para recordarla.
            self.letras_intentadas.append(letra)

            if letra in self.palabra_secreta:
                print("Adivinaste una letra")
                # Recorremos la palabra secreta letra por letra, guardando su índice (su posición)
                for i, letra_secreta in enumerate(self.palabra_secreta):
                    # Si la letra que escribió el usuario es igual a la letra secreta en esta posición...
                    if letra == letra_secreta:
                        # ¡Reemplazamos el guion bajo en ese mismo índice del tablero por la letra!
                        self.tablero[i] = letra
            else:
                self.vidas -= 1
                print(f"La letra {letra} no se encuentra en la palabra secreta")
        if self.vidas == 0:
            print(f"¡Perdiste! La palabra era {self.palabra_secreta}")
        else:
            print(f"¡Felicidades! Adivinaste la palabra: {self.palabra_secreta}")


while True:
    print("\n--- ¡BIENVENIDO AL JUEGO DEL AHORCADO! ---")

    mi_juego = JuegoAhorcado()
    mi_juego.jugar()

    respuesta = input("\n¿Deseas jugar de nuevo? (s/n): ").strip().lower()
    if respuesta != 's':
        print("¡Gracias por jugar! Hasta luego.")
        break  # Rompemos el bucle infinito y el programa termina.