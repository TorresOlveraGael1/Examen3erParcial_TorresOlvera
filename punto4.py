#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.

print(" ")
print("Torres Olvera Gael")
print(" ")

#Declarando las funciones principales
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"

#Solicitar los valores al usuario
try:
    valor1 = int(input("Ingrese el primer número entero: "))
    valor2 = int(input("Ingrese el segundo número entero: "))
    
    #Crear una instancia de la clase Calculadora
    calculadora = Calculadora(valor1, valor2)

    #Realizar las operaciones y mostrar los resultados
    print(f"Suma: {calculadora.suma()}")
    print(f"Resta: {calculadora.resta()}")
    print(f"Multiplicación: {calculadora.multiplicacion()}")
    print(f"División: {calculadora.division()}")

except ValueError:
    print("Por favor, ingrese valores enteros válidos.")