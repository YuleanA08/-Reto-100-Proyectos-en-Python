🎟️ TICKET DE TRABAJO #005: Juego del Ahorcado (Hangman)
1. El Problema (User Story)
Como jugador, quiero un clásico juego del Ahorcado en la terminal. Necesito que el sistema elija una palabra secreta de una lista predefinida y me permita adivinarla letra por letra. Quiero ver mi progreso (las letras que he acertado y los espacios en blanco) y tener un número limitado de vidas antes de "perder".

2. Criterios de Aceptación (Definición de "Terminado")
Tu programa DEBE cumplir con los siguientes casos de uso:

Palabra Secreta: El programa debe tener una lista de al menos 5 palabras ocultas y elegir una al azar cada vez que inicia el juego.

Estado Oculto: Al empezar, el programa debe mostrar la palabra oculta usando guiones bajos (ej: _ _ _ _ _ para "PERRO").

Mecánica de Juego:

El usuario ingresa una letra por turno.

Si la letra está en la palabra secreta, el tablero debe actualizarse revelando esa letra en todas sus posiciones correctas (ej: si adivina 'R', el tablero cambia a _ _ R R _).

Si la letra no está, el usuario pierde 1 vida (comienza con 6 vidas).

Manejo de Mayúsculas/Minúsculas: El juego no debe ser sensible a mayúsculas. Si la palabra es "Gato", debe dar igual si el usuario escribe 'G' o 'g'.

Condiciones de Fin de Juego:

Ganar: El usuario adivina todas las letras antes de quedarse sin vidas.

Perder: El contador de vidas llega a 0.

En ambos casos, el programa debe revelar cuál era la palabra secreta y preguntar si desea jugar de nuevo.

3. Restricciones Técnicas (Stack y Reglas)
Estructura de Datos: Necesitarás usar Listas para manejar el tablero oculto y un bucle while principal para mantener el juego andando hasta que se acaben las vidas o no queden guiones bajos.

POO: Todo debe estar dentro de una clase JuegoAhorcado.

💡 Tip de tu Tech Lead para empezar:

El mayor reto lógico aquí es cómo actualizar el tablero con los guiones bajos (_).

Cuando inicie el juego y elijas la palabra secreta, crea una lista paralela que tenga la misma cantidad de elementos, pero llena de guiones bajos.

Ej: palabra_secreta = "GATO", tablero = ["_", "_", "_", "_"]

Cuando el usuario ingrese una letra válida, usa enumerate() (¡que ya lo dominas!) para recorrer la palabra_secreta. Si la letra ingresada coincide con la letra en el índice i de la palabra secreta, ¡reemplaza el elemento en el índice i de tu tablero!