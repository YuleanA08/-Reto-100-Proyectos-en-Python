🎟️ TICKET DE TRABAJO #003: Generador de Contraseñas Seguras
1. El Problema (User Story)
Como usuario preocupado por mi seguridad digital, necesito una herramienta que genere contraseñas complejas y aleatorias. A menudo uso contraseñas débiles porque me cuesta inventar combinaciones seguras. Necesito que el programa me pregunte qué longitud quiero que tenga mi contraseña y que la construya mezclando letras (mayúsculas y minúsculas), números y símbolos.

2. Criterios de Aceptación (Definición de "Terminado")
Tu programa DEBE cumplir exactamente con los siguientes casos de uso para ser aprobado:

Longitud Personalizada: El sistema debe preguntar al usuario cuántos caracteres desea que tenga la contraseña.

Validación de Longitud: Debes garantizar que el usuario ingrese un número entero. Además, la longitud mínima aceptada debe ser 8. Si el usuario ingresa un número menor (ej: 4), el programa debe advertirle que es inseguro y volver a pedir la longitud hasta que ingrese 8 o más.

Complejidad Requerida: La contraseña generada debe contener una mezcla aleatoria de:

Letras minúsculas (a-z)

Letras mayúsculas (A-Z)

Números (0-9)

Símbolos especiales (ej: !@#$%^&*())

Salida Clara: El programa debe imprimir la contraseña generada final en la terminal de forma clara (ej. "Tu nueva contraseña segura es: Xy7!pL9#").

3. Restricciones Técnicas (Stack y Reglas)
Lenguaje: Python puro.

Módulos permitidos: random y el módulo estándar string (te recomiendo investigar qué tiene dentro el módulo string, ¡te ahorrará escribir el abecedario a mano!).

Estructura: Nuevamente, no quiero código "spaghetti". Utiliza Programación Orientada a Objetos (crea una clase GeneradorContrasena). Debes tener al menos un método para pedir/validar la longitud y otro método independiente encargado exclusivamente de generar la contraseña.