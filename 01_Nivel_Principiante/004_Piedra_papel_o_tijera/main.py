class GestorTareas:
    def __init__(self):
        self.tareas = []

    def iniciar(self):
        while True:
            try:
                inicial = int(input("1. Agregar tarea"
                    "\n2. Ver tareas pendientes"
                    "\n3. Eliminar tarea"
                    "\n4. Salir "
                    "\nIngresa el numero de acuerdo a lo que deseas: "))

                if inicial == 1:
                    self.agregar_tarea()
                elif inicial == 2:
                    self.ver_tareas()
                elif inicial == 3:
                    self.eliminar_tarea()
                else:
                    break
            except ValueError:
                print("Error: Debes escribir un número.")
                continue

    def agregar_tarea(self):
        tareanew = input("Ingrese su nueva tarea: ")
        self.tareas.append(tareanew)
        print(f"¡Tarea agregada: {tareanew}!")

    def ver_tareas(self):
        if len(self.tareas) == 0:
            print("No hay tareas")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"Tarea numero: {i+1}.{tarea}")

    def eliminar_tarea(self):
        try:
            num_tarea = int(input("Ingrese el numero de la tarea a eliminar: "))
            num_tarea = num_tarea - 1
            eliminada =self.tareas.pop(num_tarea)
            print(f"Eliminada numero: {num_tarea + 1}.{eliminada}")

        except ValueError:
            print("Error: Debes escribir un número.")

        except IndexError:
            print("Error: Ese número de tarea no existe en tu lista.")


mi_app = GestorTareas()
mi_app.iniciar()