class ContadorPalabras:
    def __init__(self, ruta_archivo):
        self.contador = {}
        self.ruta = ruta_archivo

    def _leer_y_limpiar(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read().lower().replace(',', '').replace('.', '')
                return contenido
        except FileNotFoundError:
            print(f"Error: El archivo '{self.ruta}' no fue encontrado.")
            return None  # Retornamos None si falla para que el programa no colapse

    def procesar_conteo(self):
        pass

    def __mostrar_resultados(self):
        pass


mi_contador = ContadorPalabras('frases.txt')
limpiar = mi_contador._leer_y_limpiar()
print(limpiar)
