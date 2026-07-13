🎟️ TICKET DE TRABAJO #004: Gestor de Tareas (To-Do List) en Terminal
1. El Problema (User Story)
Como usuario, necesito una aplicación en mi terminal que me permita organizar mi día. Quiero poder agregar nuevas tareas a una lista, ver todas las tareas que tengo pendientes y borrar las tareas que ya he completado.

2. Criterios de Aceptación (Definición de "Terminado")
Tu programa DEBE cumplir con los siguientes casos de uso:

Menú Interactivo: Al iniciar, el programa debe mostrar un menú con un bucle infinito que ofrezca 4 opciones:

Agregar tarea

Ver tareas pendientes

Eliminar tarea

Salir

Almacenamiento temporal: Las tareas deben guardarse en una lista de Python (no te preocupes por bases de datos o archivos de texto todavía, cuando el programa se cierre, las tareas se borrarán y está bien).

Ver Tareas: Si el usuario elige la opción 2, el sistema debe imprimir la lista de tareas numeradas (ej: 1. Comprar pan, 2. Estudiar Python). Si la lista está vacía, debe mostrar un mensaje avisando que no hay tareas.

Eliminar Tareas: Si el usuario elige la opción 3, el sistema debe preguntarle el número de la tarea que desea borrar.

Manejo de Errores (Robustez): * Si el usuario ingresa letras en lugar de números en el menú principal o al intentar eliminar una tarea, no debe crashear (ValueError).

Si el usuario intenta borrar la tarea número 10, pero solo hay 3 tareas en la lista, el programa debe atrapar el error (investiga qué error lanza Python cuando buscas en una lista un índice que no existe) y avisarle amistosamente.

3. Restricciones Técnicas (Stack y Reglas)
Estructura POO: Crea una clase GestorTareas. Debe tener un método __init__ donde inicialices tu lista de tareas vacía (ej. self.tareas = []).

Modularidad: Crea un método para cada acción (agregar_tarea, ver_tareas, eliminar_tarea) y un método principal (iniciar) que contenga el bucle while del menú.