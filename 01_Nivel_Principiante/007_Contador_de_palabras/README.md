🎟️ TICKET DE TRABAJO #007 (REDISEÑADO): Contador de Palabras 2.0

1. El Problema (User Story)
   Como desarrollador, quiero crear un sistema robusto para analizar la frecuencia de palabras en archivos .txt. Mi
   objetivo es demostrar dominio de la POO al encapsular la lógica de procesamiento de archivos.

2. Criterios de Aceptación (Definición de "Terminado")

Encapsulamiento: Toda la lógica debe estar dentro de la clase ContadorPalabras. Los atributos que manejen los datos del
archivo o el diccionario de conteo deben estar protegidos/privados.

Métodos de la clase: * Un constructor __init__ que reciba la ruta del archivo.

Un método privado para leer y limpiar el texto.

Un método público para procesar el conteo.

Un método para mostrar los resultados formateados.

Manejo de Errores: Implementa bloques try-except dentro de los métodos para capturar errores de lectura (archivo
inexistente, permisos, etc.).

3. Restricciones Técnicas (Nivel POO)

Prohibido: No uses variables globales.

Exigencia: Usa métodos de instancia y, si lo consideras necesario para alguna función de utilidad, un método estático (
@staticmethod).

Buenas prácticas: Documenta tus métodos con docstrings y utiliza f-strings para el formato de salida.