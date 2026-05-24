🎟️ TICKET #001: Calculadora Básica Interactiva
1. El Problema (User Story):
Como usuario de la terminal, quiero poder ingresar dos números y elegir una operación matemática básica para obtener el resultado rápidamente, sin que el programa se cierre si cometo un error al teclear.

2. Criterios de Aceptación (Lo que debe cumplir para ser aprobado):

El programa debe soportar cuatro operaciones: Suma (+), Resta (-), Multiplicación (*) y División (/).

Manejo de errores 1: Si el usuario intenta dividir por cero, el programa no debe "explotar" (Crash). Debe imprimir un mensaje amigable indicando que no es posible y pedir los datos de nuevo.

Manejo de errores 2: Si el usuario ingresa letras o símbolos raros en lugar de números, el programa debe atrapar el error (usando try/except) y avisar que solo se permiten números.

Ciclo de vida: La calculadora debe ejecutarse dentro de un bucle (while). Después de cada cálculo, debe preguntar si el usuario quiere hacer otro cálculo o si desea escribir "salir" para terminar el programa.

3. Restricciones Técnicas (El reto del Tech Lead):

PROHIBIDO usar la función nativa eval().

Regla de Arquitectura: Ya que estás estudiando diccionarios, DEBES usar un diccionario para organizar las operaciones matemáticas. En lugar de hacer una cadena interminable de if / elif / elif / else para saber qué operación eligió el usuario, debes mapear el símbolo matemático a la lógica de la operación.

Modulariza tu código: Trata de usar funciones separadas para cada operación matemática (ej. def sumar(a, b):).

4. Timebox (Límite de tiempo recomendado):

1 a 2 horas máximo.