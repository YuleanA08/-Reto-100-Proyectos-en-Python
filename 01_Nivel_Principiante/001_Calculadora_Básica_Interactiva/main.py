#Importancion de las funciones para operar
from funciones import sumar, restar, multiplicar, dividir

#Diccionario con los nombre de las funciones
operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir
}
def main():
    #Ciclo principal para hacer el recorrido y las validaciones necesarias
    while True:
        # Solicita el primer numero
        while True:
            try:
                numero1 = int(input("Digita tu primer numero: "))
                break
            except ValueError:
                print("Numero invalido")

        #Solicita el operador al usuario
        while True:
            operador = input("Ingrese operador entre +, -, *, /: ")
            if operador not in operaciones:
                print("Operador invalido")
            else:
                break

        # Solicita el segundo numero
        while True:
            try:
                numero2 = int(input("Digite tu segundo numero: "))
                break
            except ValueError:
                print("Numero invalido")

        """Se pasa la variable operador porque es la llave y se pone operaciones ya que es el diccionario donde se encuentra
        el valor eso nos retorna la funcion y ya numero1 y numero2 son los argumentos que ingresamos para ya se haga la funcion."""

        resultado = operaciones[operador](numero1, numero2)
        print(resultado)

        #Y para finalizar hace la pregunta si desea salir ya que si lo escribe se termina de ejecutar el programa.
        pregunta = input("Escribe salir para salir:").upper() == "salir"
        if pregunta == "salir":
            break

if __name__ == "__main__":
    main()