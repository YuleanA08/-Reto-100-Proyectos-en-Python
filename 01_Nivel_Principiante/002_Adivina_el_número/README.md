### 🎟️ TICKET DE TRABAJO #002: Juego "Adivina el Número"

#### 1. El Problema (User Story)

Como usuario, quiero jugar contra la computadora a adivinar un número secreto. Necesito que el sistema elija un número al azar y me permita ingresar mis suposiciones por teclado. Para poder acercarme a la respuesta, el sistema debe darme pistas diciéndome si el número secreto es "mayor" o "menor" al que acabo de intentar, hasta que logre adivinarlo correctamente.

#### 2. Criterios de Aceptación (Definición de "Terminado")

Tu programa DEBE cumplir exactamente con los siguientes casos de uso para ser aprobado:

* **Generación Aleatoria:** Al iniciar, el programa debe generar en secreto un número entero aleatorio (por defecto, entre 1 y 100).
* **Feedback Inmediato:** Después de cada intento del usuario, el sistema debe imprimir "El número secreto es MAYOR" o "El número secreto es MENOR".
* **Conteo de Intentos:** El sistema debe rastrear cuántos intentos le tomó al usuario ganar. Al acertar, debe mostrar un mensaje de felicitación que incluya la cantidad de intentos realizados.
* **Manejo de Excepciones (Robustez):** Si el usuario ingresa letras, símbolos o deja el espacio en blanco (cualquier cosa que no sea un número entero), **el programa no debe crashear**. Debe atrapar el error, mostrar un mensaje amistoso (ej. *"Por favor, ingresa solo números enteros"*) y dejar que el usuario intente de nuevo sin sumarle un intento fallido.
* **Rejugabilidad:** Una vez que el usuario gane, el programa debe preguntarle si desea jugar otra vez (ej. "¿Jugar de nuevo? S/N"). Si dice que sí, el contador de intentos vuelve a cero y se genera un número nuevo.

#### 3. Restricciones Técnicas (Stack y Reglas)

* **Lenguaje:** Python puro.
* **Módulos:** Tienes que investigar y utilizar el módulo estándar `random` de Python.
* **Estructura de Código:** Prohibido escribir código en un solo bloque gigante (el estilo "spaghetti"). Debes empaquetar tu lógica en **al menos dos funciones**. (Por ejemplo: podrías tener una función que se encargue exclusivamente de pedir y validar que el input sea un número entero, y otra función que maneje la lógica principal del juego).
* **Constantes:** Los límites del número (1 y 100) deben estar declarados como variables constantes al principio de tu script (ej. `RANGO_MIN = 1`, `RANGO_MAX = 100`), de modo que si mañana queremos que el juego sea del 1 al 1000, solo tengamos que cambiar esas dos variables y no buscar por todo el código.

---