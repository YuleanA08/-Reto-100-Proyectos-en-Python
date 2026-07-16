🎟️ TICKET DE TRABAJO #006: Conversor de Unidades (Universal)
1. El Problema (User Story)
Como usuario, necesito una herramienta rápida para convertir diferentes unidades de medida. A veces confundo las millas con los kilómetros, o los grados Celsius con los Fahrenheit, por lo que requiero un sistema centralizado que me permita seleccionar qué tipo de conversión deseo hacer y obtener el resultado de forma precisa.

2. Criterios de Aceptación
Tu programa DEBE cumplir con los siguientes casos de uso:

Menú de Selección de Categoría: El programa debe ofrecer al menos tres categorías de conversión:

Longitud (Kilómetros a Millas y viceversa)

Temperatura (Celsius a Fahrenheit y viceversa)

Peso (Kilogramos a Libras y viceversa)

Validación de Datos:

El sistema debe verificar que el valor numérico ingresado sea un número real (puedes usar float en lugar de int para permitir decimales).

Debe manejar errores si el usuario ingresa texto en lugar de números.

Interfaz amigable: Después de mostrar el resultado, el programa debe preguntar si quieres realizar otra conversión o salir.

3. Restricciones Técnicas
Clase Base: Crea una clase ConversorUnidades.

Modularidad: Cada tipo de conversión (longitud, temperatura, peso) debe estar en un método independiente dentro de la clase.

Encapsulamiento de lógica: El método iniciar debe encargarse del bucle principal y del menú, delegando los cálculos específicos a los métodos de conversión.

💡 Tip de tu Tech Lead:
Para manejar los cálculos, recuerda las fórmulas básicas:

Km a Millas: millas = km * 0.621371

Celsius a Fahrenheit: f = (c * 9/5) + 32

Kg a Libras: libras = kg * 2.20462

¿Te sientes cómodo empezando a estructurar la clase ConversorUnidades y los métodos para cada categoría? ¡Es un excelente ejercicio para practicar la separación de responsabilidades en tu código!